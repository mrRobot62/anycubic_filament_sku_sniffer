#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
anycubic_variants.py

Region-aware Scraper für Anycubic-Produktseiten.

Features:
- Liest eine oder mehrere URLs und extrahiert Varianten-Infos (je nach Region unterschiedliche HTML-Quellenstrukturen)
- Region-Schalter (--region de|us|en), default: de
  - de: scannt initData: { ... } (Shopify-Frontendstruktur)
  - us/en: scannt var meta = { ... } (Shopify-Theme-Meta)
- Haupttabelle (Product, Price, Color, SKU[, Source])
- Optional zweite Tabelle (Unique Colors) mit (Color, ID, Products)
- Ausgabe als PrettyTable/Fallback oder Markdown (--md)
- Fortschritt: "Lese URL: …"
- --out speichert identische Ausgabe in Datei

Beispiele:
  python anycubic_variants.py --url "https://de.anycubic.com/products/..." --md --out result.md
  python anycubic_variants.py --region us --urls-file urls.txt --with-source
"""

import argparse
import json
import re
import sys
from typing import Optional, Dict, Any, List, Tuple, Set, Callable

import requests


# ==========================
# Hilfsfunktionen (allgemein)
# ==========================
def clean_color_name_from_title(title: str) -> str:
    """
    Extrahiert den Farbnamen robust aus Titeln wie:
      "Black / 1KG / US", "1KG / Black / EU", "Blue/0.5KG/UK"
    Ignoriert Gewichts-, Regions- und Packungs-/Stückzahl-Tokens.
    """
    if not isinstance(title, str):
        return ""

    # In Teile splitten, egal ob " / " oder "/"
    parts = [p.strip() for p in re.split(r'\s*/\s*', title) if p.strip()]
    if not parts:
        return ""

    def is_weight(tok: str) -> bool:
        t = tok.replace(" ", "").lower()
        # z.B. 1KG, 0.5KG, 500G, 1lb, 2lbs
        return bool(re.match(r'^\d+(\.\d+)?(kg|g|lb|lbs)$', t))

    def is_region(tok: str) -> bool:
        t = tok.strip().upper()
        # häufige Regions-/Ländercodes in Anycubic-Titeln
        return t in {"US", "EU", "UK", "AU", "CA", "DE", "FR", "ES", "IT", "JP"}

    def is_packaging(tok: str) -> bool:
        t = tok.lower()
        # grobe Heuristik für Packungs-/Stückzahlhinweise
        return ("pack" in t) or ("pcs" in t) or ("spool" in t)

    # Wähle den ersten Token, der nicht Gewicht/Region/Packung ist
    for tok in parts:
        if not (is_weight(tok) or is_region(tok) or is_packaging(tok)):
            return tok

    # Fallback: erster Teil
    return parts[0]


def extract_color_id_from_sku(sku: str) -> str:
    """
    Farb-ID = letzte 2 Zeichen der Kennzeichnung vor dem Bindestrich.
    SKU: <kennzeichnung>-<id>, z. B. AHPLBK-105 -> BK
    - <kennzeichnung>: 5-7 alphanumerisch, die letzten 2 alphanumerischen Zeichen = Farbcode
    - '-'
    - <id>: 2-4 alphanumerisch (oft 3 Ziffern oder Buchstabe + 3 Ziffern)
    """
    if not isinstance(sku, str) or '-' not in sku:
        return ""
    kennz, _id = sku.split('-', 1)
    kennz = kennz.strip()
    if len(kennz) < 2:
        return ""
    color_id = kennz[-2:].upper()
    if not re.fullmatch(r'[A-Za-z0-9]{2}', color_id):
        return ""
    return color_id


def currency_for_region(region: str) -> str:
    """Fallback-Währungszuordnung pro Region."""
    mapping = {
        'de': 'EUR',
        'us': 'USD',
        'en': 'USD',   # global/EN-Store häufig USD
    }
    return mapping.get(region.lower(), '')


def format_price(amount: Any, currency: str) -> str:
    """Formatiert Preis + Währung robust."""
    if isinstance(amount, (int, float)):
        return f"{float(amount):.2f} {currency}".strip()
    return f"{amount} {currency}".strip()


# ==================================
# HTML-Block-Extractor (balanciert)
# ==================================

def _extract_balanced_object(html: str, pattern_before_brace: str) -> Optional[str]:
    """
    Findet ein Auftreten von pattern_before_brace (Regex) gefolgt von '{'
    und extrahiert den vollständig balancierten JSON-Objektstring (mit String-/Escape-Handling).
    """
    m = re.search(pattern_before_brace, html)
    if not m:
        return None
    start_brace = m.end() - 1
    i = start_brace
    depth = 0
    in_str = False
    str_char = ''
    escaped = False
    while i < len(html):
        ch = html[i]
        if in_str:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == str_char:
                in_str = False
        else:
            if ch in ('"', "'"):
                in_str = True
                str_char = ch
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return html[start_brace:i + 1]
        i += 1
    return None


# ========================
# Regionale Scanner (Parser)
# ========================

def scan_region_de(html: str, source_url: Optional[str], with_source: bool) -> Tuple[List[List[str]], Dict[str, Dict[str, Set[str]]]]:
    """Parser für Region 'de' (initData)."""
    json_str = _extract_balanced_object(html, r'initData\s*:\s*{')
    if not json_str:
        raise RuntimeError("Konnte den 'initData' Block nicht finden.")
    try:
        initdata = json.loads(json_str)
    except json.JSONDecodeError as e:
        preview = json_str[:300].replace('\n', ' ')
        raise RuntimeError(f"initData JSON-Fehler: {e} | Auszug: {preview} ...") from e

    variants = initdata.get('productVariants')
    if not isinstance(variants, list):
        raise RuntimeError("In initData fehlt 'productVariants' als Liste.")

    rows: List[List[str]] = []
    color_agg: Dict[str, Dict[str, Set[str]]] = {}
    currency = (initdata.get('shop') or {}).get('paymentSettings', {}).get('currencyCode', '') or 'EUR'

    for v in variants:
        product_title = (v.get('product') or {}).get('title') or ''
        price_obj = v.get('price') or {}
        amount = price_obj.get('amount')
        curr = price_obj.get('currencyCode') or currency
        color_title_raw = v.get('title') or ''
        color = clean_color_name_from_title(color_title_raw)
        sku = v.get('sku') or ''

        row = [product_title, format_price(amount, curr), color or color_title_raw, sku]
        if with_source:
            row.append(source_url or '')
        rows.append(row)

        cid = extract_color_id_from_sku(sku)
        if cid:
            bucket = color_agg.setdefault(cid, {'names': set(), 'products': set()})
            if color:
                bucket['names'].add(color)
            if product_title:
                bucket['products'].add(product_title)

    return rows, color_agg


def scan_region_us_en(html: str, source_url: Optional[str], with_source: bool, region: str) -> Tuple[List[List[str]], Dict[str, Dict[str, Set[str]]]]:
    """
    Parser für 'us' und 'en' Regionen (var meta).
    Struktur:
      var meta = {
        "product": {
          "variants": [
            { "id":..., "price":1799, "name":"PLA Basic - Black / 1KG / US", "public_title":"Black / 1KG / US", "sku":"AHPLBK-105" },
            ...
          ]
        }
      }
    Preis: meist Cent -> /100
    Product-Name: aus variant.name vor ' - ' (z. B. "PLA Basic")
    Color: aus public_title vor '/' (z. B. "Black")
    """
    json_str = _extract_balanced_object(html, r'var\s+meta\s*=\s*{')
    if not json_str:
        raise RuntimeError("Konnte den 'var meta' Block nicht finden.")
    try:
        meta = json.loads(json_str)
    except json.JSONDecodeError as e:
        preview = json_str[:300].replace('\n', ' ')
        raise RuntimeError(f"meta JSON-Fehler: {e} | Auszug: {preview} ...") from e

    product = meta.get('product') or {}
    variants = product.get('variants')
    if not isinstance(variants, list):
        raise RuntimeError("In meta.product fehlt 'variants' als Liste.")

    rows: List[List[str]] = []
    color_agg: Dict[str, Dict[str, Set[str]]] = {}
    curr = currency_for_region(region)

    for v in variants:
        name = v.get('name') or ''
        product_title = name.split(' - ', 1)[0].strip() if ' - ' in name else (product.get('title') or product.get('type') or '')
        public_title = v.get('public_title') or ''
        color = clean_color_name_from_title(public_title)
        price_raw = v.get('price')
        if isinstance(price_raw, (int, float)):
            amount = float(price_raw) / 100.0
        else:
            try:
                amount = float(int(str(price_raw))) / 100.0
            except Exception:
                amount = price_raw
        sku = v.get('sku') or ''

        row = [product_title, format_price(amount, curr), color or public_title, sku]
        if with_source:
            row.append(source_url or '')
        rows.append(row)

        cid = extract_color_id_from_sku(sku)
        if cid:
            bucket = color_agg.setdefault(cid, {'names': set(), 'products': set()})
            if color:
                bucket['names'].add(color)
            if product_title:
                bucket['products'].add(product_title)

    return rows, color_agg


# -----------------------------------------
# Registry / Scanner Switch (modular)
# -----------------------------------------

RegionScanner = Callable[[str, Optional[str], bool], Tuple[List[List[str]], Dict[str, Dict[str, Set[str]]]]]

def make_us_en_scanner(region: str) -> RegionScanner:
    """Wrapper, um die Region (für Währung etc.) an den US/EN-Scanner zu binden."""
    return lambda html, src, ws: scan_region_us_en(html, src, ws, region)

SCANNERS: Dict[str, RegionScanner] = {
    "de": scan_region_de,
    "us": make_us_en_scanner("us"),
    "en": make_us_en_scanner("en"),
}

def scan_region(html: str, source_url: Optional[str], with_source: bool, region: str) -> Tuple[List[List[str]], Dict[str, Dict[str, Set[str]]]]:
    """
    Wählt anhand der Region den passenden Scanner aus.
    Fallback auf 'de', falls ungültige oder unbekannte Region.
    """
    region_l = (region or '').lower().strip()
    scanner = SCANNERS.get(region_l, SCANNERS["de"])
    return scanner(html, source_url, with_source)


# ==========================
# Ausgabe-Renderer (Tabellen)
# ==========================

def format_table_pretty(rows: List[List[str]], headers: List[str]) -> str:
    try:
        from prettytable import PrettyTable  # type: ignore
        t = PrettyTable()
        t.field_names = headers
        for r in rows:
            t.add_row(r)
        return str(t)
    except Exception:
        col_widths = [len(h) for h in headers]
        for r in rows:
            for i, c in enumerate(r):
                col_widths[i] = max(col_widths[i], len(str(c)))
        def fmt_row(cols):
            return " | ".join(str(c).ljust(w) for c, w in zip(cols, col_widths))
        sep = "-+-".join("-" * w for w in col_widths)
        out = [fmt_row(headers), sep]
        out.extend(fmt_row(r) for r in rows)
        return "\n".join(out)


def _md_escape(cell: str) -> str:
    if cell is None:
        return ""
    s = str(cell).replace("|", r"\|")
    s = s.replace("\n", " ").replace("\r", " ")
    return s


def format_table_md(rows: List[List[str]], headers: List[str], title: Optional[str] = None) -> str:
    parts: List[str] = []
    if title:
        parts.append(f"### {title}")
        parts.append("")
    header_line = "| " + " | ".join(_md_escape(h) for h in headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in headers) + " |"
    parts.append(header_line)
    parts.append(sep_line)
    for r in rows:
        parts.append("| " + " | ".join(_md_escape(c) for c in r) + " |")
    return "\n".join(parts)


def format_output(rows_main: List[List[str]], headers_main: List[str],
                  rows_unique: Optional[List[List[str]]], headers_unique: Optional[List[str]],
                  use_md: bool) -> str:
    if use_md:
        blocks: List[str] = [format_table_md(rows_main, headers_main, title="Varianten")]
        if rows_unique is not None and headers_unique is not None:
            blocks.append("")
            blocks.append(format_table_md(rows_unique, headers_unique, title="Eindeutige Farben"))
        return "\n".join(blocks)
    else:
        out = [format_table_pretty(rows_main, headers_main)]
        if rows_unique is not None and headers_unique is not None:
            out.append("\nEindeutige Farben:\n")
            out.append(format_table_pretty(rows_unique, headers_unique))
        return "\n".join(out)


# ==========================
# Fetch + Orchestrierung
# ==========================

def fetch_html(url: str, timeout: int = 20) -> str:
    print(f"Lese URL: {url}")
    try:
        resp = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Mozilla/5.0 (compatible; anycubic-region-scraper/1.0)"
        })
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        raise RuntimeError(f"Fehler beim Laden der Seite {url}: {e}") from e


def load_urls_from_file(path: str) -> List[str]:
    urls: List[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
    return urls


def main():
    parser = argparse.ArgumentParser(description="Extrahiere productVariants aus Anycubic-Seiten (region-abhängig) und erzeuge Tabellen.")
    parser.add_argument("--region", default="de", choices=["de", "us", "en"], help="Seiten-Region: de (Default), us oder en")
    parser.add_argument("--url", action="append", help="Zu lesende URL. Kann mehrfach angegeben werden.")
    parser.add_argument("--urls-file", help="Datei mit URLs (eine pro Zeile; '#' = Kommentar).")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP Timeout in Sekunden (Default: 20)")
    parser.add_argument("--with-source", action="store_true", help="Zusätzliche Spalte 'Source' mit der Quell-URL ausgeben.")
    parser.add_argument("--out", help="Dateiname für Ausgabe (Tabelle(n) wird/werden zusätzlich gespeichert).")
    parser.add_argument("--md", action="store_true", help="Tabellen als Markdown ausgeben (und speichern).")
    parser.add_argument("--unique-colors", dest="unique_colors", action="store_true", default=True, help="Am Ende eine Unique-Colors-Tabelle ausgeben (Standard).")
    parser.add_argument("--no-unique-colors", dest="unique_colors", action="store_false", help="Unique-Colors-Tabelle unterdrücken.")
    args = parser.parse_args()

    urls: List[str] = []
    if args.url:
        urls.extend(args.url)
    if args.urls_file:
        try:
            urls.extend(load_urls_from_file(args.urls_file))
        except Exception as e:
            print(f"Fehler beim Lesen der URL-Datei: {e}", file=sys.stderr)
            sys.exit(1)

    if not urls:
        print("Bitte eine oder mehrere URLs mit --url oder --urls-file angeben.", file=sys.stderr)
        sys.exit(1)

    headers_main = ["Product", "Price", "Color", "SKU"]
    if args.with_source:
        headers_main.append("Source")

    all_rows: List[List[str]] = []
    global_color_agg: Dict[str, Dict[str, Set[str]]] = {}
    had_errors = False

    for u in urls:
        try:
            html = fetch_html(u, timeout=args.timeout)
            rows, color_agg = scan_region(html, source_url=u if args.with_source else None, with_source=args.with_source, region=args.region)
            all_rows.extend(rows)
            for cid, payload in color_agg.items():
                g = global_color_agg.setdefault(cid, {'names': set(), 'products': set()})
                g['names'].update(payload.get('names', set()))
                g['products'].update(payload.get('products', set()))
        except Exception as e:
            had_errors = True
            print(str(e), file=sys.stderr)

    if not all_rows and had_errors:
        sys.exit(2)

    # Unique Colors aufbereiten (optional)
    rows_unique = None
    headers_unique = None
    if args.unique_colors and global_color_agg:
        rows_unique = []
        for cid in sorted(global_color_agg.keys()):
            names = sorted(global_color_agg[cid].get('names', set()), key=lambda s: s.lower())
            products = sorted(global_color_agg[cid].get('products', set()), key=lambda s: s.lower())
            color_display = ", ".join(names) if names else "(unbekannt)"
            products_display = ", ".join(products)
            rows_unique.append([color_display, cid, products_display])
        headers_unique = ["Color", "ID", "Products"]

    final_text = format_output(all_rows, headers_main, rows_unique, headers_unique, use_md=args.md)
    print(final_text)

    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(final_text + "\n")
            print(f"\n✅ Ausgabe gespeichert unter: {args.out}")
        except Exception as e:
            print(f"Fehler beim Schreiben der Ausgabedatei: {e}", file=sys.stderr)
            sys.exit(3)


if __name__ == "__main__":
    main()

# Deep dive into SKU interpretation (demystify?)
This document summarizes the **personal interpretation of the SKU prefixes** used by Anycubic to encode filament type, subtype, and sometimes series characteristics. Maybe there are some misinterpretations.

It’s based on cross-referencing packaging, NFC dumps, and SKU naming consistency.

## 🧩 General SKU format
| Segment | Meaning | Example | Comment |
|----------|----------|----------|----------|
| **A** | Series / generation prefix (optional) | `A` in `AHPLBK-105` | Usually stands for *Anycubic* or a series ID |
| **H** | Core filament prefix | `H` | Present in all filament SKUs = `H` Header/Hotend ?|
| **<Subcode>** | Material group and subtype | `PLP` | Defines material (PLA, PETG, TPU, etc.) |
| **<ColorCode>** | 2–3 letter color code | `BK`, `GY`, `PO` | Matches the official color abbreviation |
| **-<Number>** | Version or revision code | `-105` | Usually 101–107; internal versioning or batch |

> `H`=Hotend maybe these SKUs are for FDM-Filaments. Will check if resin have simlar codings
---

## 🧩 Special Series Codes

| Series | Prefix | Notes |
|---------|---------|-------|
| **PLA Special / Limited** | `HPL16–HPL19` | Numbered limited edition colors (Spring Leaf, Tropical Turquoise, etc.) |
| **PLA Silk Dual/Tri-Color** | `AHSC07–AHSC18` | Color index defines gradient combination |
| **PLA Glow** | `HFGxx` | “FG” = Fluorescent Glow – phosphorescent pigments |
| **PLA Matte** | `HYGxx` | “YG” reused from internal “Young Gloss” series |
| **PLA Galaxy** | `AHXKxx` | “XK” stylized for “Extra Sparkle” / “Kaleidoscope” |
| **PLA Metal** | `HJSxx` | “Jet Shine” metallic finish |

## 🧩 Key Prefix Component Meanings

| Code | Likely Meaning | Verified | Explanation |
|------|----------------|-----------|-------------|
| **A** | Anycubic / Series A | x | Brand or product generation prefix |
| **H** | Head / Hotend material tag | x | Appears in all SKUs |
| **PL** | PLA Basic | x | Polylactic Acid |
| **PLP** | PLA+ | x | “PLA Plus” enhanced variant |
| **HS** | High Speed | x | Fast printing formulation |
| **LS** | Limestone / Stone | x | Used for Marble effect |
| **SC** | Silk Color | x | Glossy silk PLA |
| **XK** | eXtra Kaleidoscope / Sparkle | ? | Galaxy series with glitter |
| **JS** | Jet Shine | x | Metallic pigment line |
| **YG** | Young Gloss (Matte) | ? | Internal label for matte surface series |
| **FG** | Fluorescent Glow | x | Glow-in-the-dark |
| **PE** | PETG | x | Polyethylene Terephthalate Glycol |
| **AS** | ASA | x | Acrylic Styrene Acrylonitrile |
| **AB** | ABS | x | Acrylonitrile Butadiene Styrene |
| **TP** | TPU | x | Thermoplastic Polyurethane |
| **PLxx** | Special PLA | x | Numeric color indexes (16–19) |

## Breakdown by Material Type

### 🧵 PLA (Basic)
- **Examples:** `AHPLBK-105`, `AHPLGY-105`  
- **Code:** `PL`  
- **Interpretation:**  
  - `A` = optional prefix  
  - `H` = header  
  - `PL` = PLA Basic  
- **Structure:** `AH` + `PL` + `<Color>` + `-###`  
  - *Refill version:* `AHPLBK-A106` → extra `A` before number = refill roll

---

### 🧵 PLA+
- **Examples:** `AHPLPVO-102`, `AHPLPBK-A108`  
- **Code:** `PLP`  
- **Interpretation:** `PLP` = PLA Plus  
- **Structure:** `AH` + `PLP` + `<Color>` + `-###`  
  - *Refill version:* `-A108`

---

### 🧵 PLA High Speed
- **Examples:** `AHHSBK-102`, `HHSRE-101`  
- **Code:** `HS`  
- **Interpretation:** `HHS` = PLA High Speed  
- **Structure:** `[A]HHS` + `<Color>` + `-###`

---

### 🧵 PLA Marble
- **Examples:** `AHLSBR-101`, `AHLSMW-101`  
- **Code:** `LS`  
- **Interpretation:** “LS” likely means *Limestone* or *Stone look*  
- **Structure:** `AHLS` + `<Color>` + `-###`

---

### 🧵 PLA Silk
- **Examples:** `AHSCPU-102`, `HSCGY-101`  
- **Code:** `SC`  
- **Interpretation:** `SC` = Silk  
- **Dual/Tri-Color:** numeric color IDs (`AHSC07-102`) → predefined multicolor mix index  
- **Structure:** `AHSC` + `<ColorCode | MixID>` + `-###`

---

### 🧵 PLA Galaxy
- **Examples:** `AHXKGL-101`, `AHXKGP-101`  
- **Code:** `XK`  
- **Interpretation:** `XK` = Galaxy (Sparkle Series)  
- **Structure:** `AHXK` + `<Color>` + `-###`

---

### 🧵 PLA Metal
- **Examples:** `HJSMC-101`, `HJSMO-101`  
- **Code:** `JSM`  
- **Interpretation:** `HJS` = PLA Metal (Shiny Jet Metal)  
- **Structure:** `HJS` + `<Color>` + `-###`

---

### 🧵 PLA Matte
- **Examples:** `HYGBK-101`, `HYGPU-102`  
- **Code:** `HYG`  
- **Interpretation:** `HYG` = Matte PLA Series  
- **Structure:** `HYG` + `<Color>` + `-###`

---

### 🧵 PLA Glow / Luminous
- **Examples:** `HFGGR-101`, `HFGBL-101`  
- **Code:** `HFG`  
- **Interpretation:** `HFG` = Fluorescent Glow Series  
- **Structure:** `HFG` + `<Color>` + `-###`

---

### 🧵 PLA Special / Limited
- **Examples:** `HPL16-101`, `HPL17-105`  
- **Code:** `HPL`  
- **Interpretation:** Numeric color codes (16–19) represent special edition color sets  
- **Structure:** `HPL<Number>-###`

---

### 🧵 PETG
- **Examples:** `AHPEBK-101`, `AHPETB-101`  
- **Code:** `PE`  
- **Interpretation:** `AHPE` = PETG  
  - `T` = Transparent variant  
- **Structure:** `AHPE[T?]` + `<Color>` + `-###`

---

### 🧵 ASA
- **Examples:** `HASBK-101`, `HASRE-101`  
- **Code:** `AS`  
- **Interpretation:** `HAS` = ASA (Acrylic Styrene Acrylonitrile)  
- **Structure:** `HAS` + `<Color>` + `-###`

---

### 🧵 ABS
- **Examples:** `HABBK-102`, `HABGY-102`  
- **Code:** `AB`  
- **Interpretation:** `HAB` = ABS (Acrylonitrile Butadiene Styrene)  
- **Structure:** `HAB` + `<Color>` + `-###`

---

### 🧵 TPU
- **Examples:** `HTPBK-101`, `HTPCO-101`  
- **Code:** `TP`  
- **Interpretation:** `HTP` = TPU (Thermoplastic Polyurethane)  
- **Structure:** `HTP` + `<Color>` + `-###`

---

## Special Observations

| Phenomenon | Explanation |
|-------------|--------------|
| **Missing “A” prefix** | Newer rolls omit the `A` prefix entirely |
| **Refill marker** | `-A###` = refill version |
| **Dual/Tri-Color Silk** | Two-digit IDs (07–18) define specific color blends |
| **Transparent PETG** | Additional `T` between `PE` and color |
| **Glow series (HFG)** | “FG” likely stands for *Fluorescent Glow* |
| **Matte series (HYG)** | Dedicated code for the matte PLA lineup |
| **PLA Special (HPLxx)** | Uses numeric IDs instead of color abbreviations |

---

## Master Prefix Map

| Prefix | Meaning | Filament Type |
|---------|----------|---------------|
| **AHPL** | PLA Basic |
| **AHPLP** | PLA Plus |
| **AHHS** | PLA High Speed |
| **AHLS** | PLA Marble |
| **AHSC / HSC** | PLA Silk |
| **AHXK** | PLA Galaxy |
| **HJS** | PLA Metal |
| **HYG** | PLA Matte |
| **HFG** | PLA Glow / Luminous |
| **HPL** | PLA Special Edition |
| **AHPE** | PETG |
| **HAS** | ASA |
| **HAB** | ABS |
| **HTP** | TPU |

---

## Meaning of Letter Blocks

| Code Block | Meaning | Comment |
|-------------|----------|----------|
| **A** | Anycubic / Series A | Optional |
| **H** | Main filament header | Always present |
| **PL** | PLA Basic | Polylactic Acid |
| **PLP** | PLA Plus | Enhanced PLA |
| **HS** | High Speed PLA | Optimized for fast printing |
| **LS** | Marble (Stone look) | Textured appearance |
| **SC** | Silk | Glossy finish |
| **XK** | Galaxy | Sparkle series |
| **JS** | Metal (Jet Shine) | Metallic pigment |
| **YG** | Matte | Matte PLA |
| **FG** | Glow / Luminous | Fluorescent or glow-in-dark |
| **PE** | PETG | Polyethylene Terephthalate Glycol |
| **AS** | ASA | Acrylic Styrene Acrylonitrile |
| **AB** | ABS | Acrylonitrile Butadiene Styrene |
| **TP** | TPU | Thermoplastic Polyurethane |
| **HPLxx** | PLA Special Edition | Numeric color identifiers |

---

# SKU-Conclusion
- A? → optional “Anycubic” prefix
- H → main Header or perhaps a reference to the hotend (because of product type: filament)
- subcode → material type identifier
- color → color code (2–3 letters or with numeric suffix)
- A?num → optional serial or refill number

The Anycubic SKU structure is consistent and logically organized:
- AH = brand + filament prefix
- The subcode precisely identifies the material family and subtype
- Variants like Glow, Marble, Matte, and Galaxy have unique, fixed subcodes
- Refill versions always include an extra “A” before the numeric code

My subjective impression is that the color codes are not exactly unique but depend on the sub-type.

For this project I used **ChatGPT** for researching and interpretation




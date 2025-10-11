# How to use the sniffer :-)

## Parameters
- `--url` : which AC side shoud be sniffed. Possible to use this parameter several times
- `--region`: however between US/EN & DE websides there are different source codes which are searched for SKUs. German is default `--region de`, `--region us`, `--region en`
- `--with-source`: if set, the URL is printed in the table as well
- `--out`: create an output file 
- `--md`: instead of PrettyTable use Markdown table
- `--unique-colors`: create a second table with unique color-codes (part of SKU) for all Filaments. Hu. AC use same color-code but name them differently.

uhhh, source code comments and help were written in German - sorry guys - I forgot to write in english

**BTW:** if somebody is interested in: Anycubic use Shopify as e-commerce software

# Simple US-Example with three US-Websides
- output into a file
- use markdown as output table
- print url inside table
- create a unique-color table additionally

anycubic-nfc-filament % pythonac_filament_sku_sniffer.py \
--url "https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--with-source --out result_en_md2.txt --unique-colors --region us --md

# All US-Filaments (English names)
python ac_filament_sku_sniffer.py \
--url "https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--with-source --out result_en.txt --unique-colors --region us

# All DE-Filaments (German names)
python ac_filament_sku_sniffer.py \
--url "https://de.anycubic.com/products/pla-filament?variant=32866809217101" \
--url "https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-basic-spezial-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--with-source --out result.txt

# Example Output (US/EN-Names)

> **NOTE:** Do not wonder about same color several times. Reason is, that it is possible to order on US-Sides but ship to coutries outside US like EU/UK/OTHERS with different prices

## Markdown-Table
### Varianten

| Product | Price | Color | SKU | Source |
| --- | --- | --- | --- | --- |
| PLA Basic | 17.99 USD | Black | AHPLBK-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Black | AHPLBK-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Black | AHPLBK-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Black | AHPLBK-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Texture Gray | AHPLGY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Texture Gray | AHPLGY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Texture Gray | AHPLGY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Gray | AHPLGE-106 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Gray | AHPLGE-106 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Gray | AHPLGE-106 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Gray | AHPLGE-106 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | White | AHPLBW-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | White | AHPLBW-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | White | AHPLBW-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | White | AHPLBW-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Clear | AHPLCL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Clear | AHPLCL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Clear | AHPLCL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Clear | AHPLCL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Texture Silver | AHPLSL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Texture Silver | AHPLSL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Texture Silver | AHPLSL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Texture Silver | AHPLSL-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Classic Green | AHPLCG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Classic Green | AHPLCG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Classic Green | AHPLCG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Classic Green | AHPLCG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Blue (Navy blue) | AHPLDB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Blue (Navy blue) | AHPLDB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Blue (Navy blue) | AHPLDB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Blue (Navy blue) | AHPLDB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Purple | AHPLPO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Purple | AHPLPO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Purple | AHPLPO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Purple | AHPLPO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Orange | AHPLVO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Orange | AHPLVO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Orange | AHPLVO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Orange | AHPLVO-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Red | AHPLRR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Red | AHPLRR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Red | AHPLRR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Red | AHPLRR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Yellow | AHPLVY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Yellow | AHPLVY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Yellow | AHPLVY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Yellow | AHPLVY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Pink | AHPLSP-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Pink | AHPLSP-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Pink | AHPLSP-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Pink | AHPLSP-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Beige | AHPLLB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Beige | AHPLLB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Beige | AHPLLB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Beige | AHPLLB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | FLash Green | AHPLGF-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | FLash Green | AHPLGF-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | FLash Green | AHPLGF-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | FLash Green | AHPLGF-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Dark Brown | AHPLKB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Dark Brown | AHPLKB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Dark Brown | AHPLKB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Dark Brown | AHPLKB-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Magenta | AHPLMG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Magenta | AHPLMG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Magenta | AHPLMG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Magenta | AHPLMG-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Brown | AHPLBR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Brown | AHPLBR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Brown | AHPLBR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Brown | AHPLBR-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Bronze | AHPLBZ-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Bronze | AHPLBZ-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Bronze | AHPLBZ-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Bronze | AHPLBZ-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Cyan | AHPLCY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 19.43 USD | Cyan | AHPLCY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 21.07 USD | Cyan | AHPLCY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic | 17.99 USD | Cyan | AHPLCY-105 | https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Texture Grey | AHHSGY-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Texture Grey | AHHSGY-103 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Texture Grey | AHHSGY-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Texture Grey | AHHSGY-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Black | AHHSBK-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Black | AHHSBK-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Black | AHHSBK-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Black | HHSBK-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Bright White | AHHSBW-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Bright White | AHHSBW-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Bright White | AHHSBW-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Bright White | HHSWH-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Vibrant Orange | AHHSVO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Vibrant Orange | AHHSVO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Vibrant Orange | HHSOR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Vibrant Orange | HHSOR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Blue | AHHSDB-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Blue | AHHSDB-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Blue | AHHSDB-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Blue | HHSBL-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Green | AHHSCG-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Green | AHHSCG-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Green | HHSGR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Green | HHSGR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Red | AHHSBR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Red | AHHSBR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Red | AHHSBR-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Red | HHSRE-101 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Strawberry Pink | AHHSSP-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Strawberry Pink | AHHSSP-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Strawberry Pink | AHHSSP-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Strawberry Pink | AHHSSP-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Purple | AHHSPO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Purple | AHHSPO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Purple | AHHSPO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Purple | AHHSPO-102 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Yellow | AHHSVY-103 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 20.51 USD | Yellow | AHHSVY-103 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 19.83 USD | Yellow | AHHSVY-103 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA High Speed | 18.99 USD | Yellow | AHHSVY-103 | https://store.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Black | AHPLPBK-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Black | AHPLPBK-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Black | AHPLPBK-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Black | AHPLPBK-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Texture Grey | AHPLPGY-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Texture Grey | AHPLPGY-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Texture Grey | AHPLPGY-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Texture Grey | AHPLPGY-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Bright White | AHPLPBW-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Bright White | AHPLPBW-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Bright White | AHPLPBW-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Bright White | AHPLPBW-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Green Flash | AHPLPGF-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Green Flash | AHPLPGF-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Green Flash | AHPLPGF-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Green Flash | AHPLPGF-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Vibrant Orange | AHPLPVO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Vibrant Orange | AHPLPVO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Vibrant Orange | AHPLPVO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Vibrant Orange | AHPLPVO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Purple Opulence | AHPLPPO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Purple Opulence | AHPLPPO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Purple Opulence | AHPLPPO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Purple Opulence | AHPLPPO-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Dazzling Blue | AHPLPDB-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Dazzling Blue | AHPLPDB-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Dazzling Blue | AHPLPDB-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Dazzling Blue | AHPLPDB-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Silver | AHPLPSL-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Silver | AHPLPSL-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Silver | AHPLPSL-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Silver | AHPLPSL-102 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Vibrant Yellow | AHPLPVY-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Vibrant Yellow | AHPLPVY-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Vibrant Yellow | AHPLPVY-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Vibrant Yellow | AHPLPVY-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Light Blue | AHPLPLB-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Light Blue | AHPLPLB-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Light Blue | AHPLPLB-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Light Blue | AHPLPLB-101 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Bright Red | AHPLPBR-106 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Bright Red | AHPLPBR-106 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Bright Red | AHPLPBR-106 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Bright Red | AHPLPBR-106 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Brown | AHPLPBR-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Brown | AHPLPBR-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Brown | AHPLPBR-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Brown | AHPLPBR-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Peach Pink | AHPLP16-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Peach Pink | AHPLP16-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Peach Pink | AHPLP16-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Peach Pink | AHPLP16-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Interstellar Violet | AHPLP17-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Interstellar Violet | AHPLP17-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Interstellar Violet | AHPLP17-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Interstellar Violet | AHPLP17-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Tropical Turquoise | AHPLP18-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Tropical Turquoise | AHPLP18-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Tropical Turquoise | AHPLP18-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Tropical Turquoise | AHPLP18-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Spring Leaf | AHPLP19-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Spring Leaf | AHPLP19-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Spring Leaf | AHPLP19-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Spring Leaf | AHPLP19-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Green | AHPLPCG-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Green | AHPLPCG-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Green | AHPLPCG-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Green | AHPLPCG-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Grey | AHPLPGE-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Grey | AHPLPGE-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Grey | AHPLPGE-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Grey | AHPLPGE-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Pink | AHPLPSP-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Pink | AHPLPSP-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Pink | AHPLPSP-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Pink | AHPLPSP-107 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Beige | AHPLPLB-108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 20.51 USD | Beige | AHPLPLB-108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 22.31 USD | Beige | AHPLPLB-108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ | 18.99 USD | Beige | AHPLPLB-108 | https://store.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Black | AHPLBK-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Black | AHPLBK-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Black | AHPLBK-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Black | AHPLBK-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Texture Grey | AHPLGY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Texture Grey | AHPLGY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Texture Grey | AHPLGY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Texture Grey | AHPLGY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | White | AHPLBW-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | White | AHPLBW-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | White | AHPLBW-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | White | AHPLBW-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Red | AHPLRR-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Red | AHPLRR-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Red | AHPLRR-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Red | AHPLRR-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Pink | AHPLSP-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Pink | AHPLSP-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Pink | AHPLSP-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Pink | AHPLSP-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Orange | AHPLVO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Orange | AHPLVO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Orange | AHPLVO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Orange | AHPLVO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Yellow | AHPLVY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Yellow | AHPLVY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Yellow | AHPLVY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Yellow | AHPLVY-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Green | AHPLCG-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Green | AHPLCG-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Green | AHPLCG-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Green | AHPLCG-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Blue | AHPLDB-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Blue | AHPLDB-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Blue | AHPLDB-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Blue | AHPLDB-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Purple | AHPLPO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 17.27 USD | Purple | AHPLPO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 18.59 USD | Purple | AHPLPO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Basic Refill | 15.99 USD | Purple | AHPLPO-A106 | https://store.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Texture Grey | AHPEGY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Texture Grey | AHPEGY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Texture Grey | AHPEGY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Texture Grey | AHPEGY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Black | AHPEBK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Black | AHPEBK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Black | AHPEBK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Black | AHPEBK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | White | AHPEBW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | White | AHPEBW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | White | AHPEBW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | White | AHPEBW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Grey | AHPEGE-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Grey | AHPEGE-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Grey | AHPEGE-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Grey | AHPEGE-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Purple | AHPEPO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Purple | AHPEPO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Purple | AHPEPO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Purple | AHPEPO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Orange | AHPEVO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Orange | AHPEVO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Orange | AHPEVO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Orange | AHPEVO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Blue | AHPEDB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Blue | AHPEDB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Blue | AHPEDB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Blue | AHPEDB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Yellow | AHPEVY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Yellow | AHPEVY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Yellow | AHPEVY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Yellow | AHPEVY-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Green | AHPECG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Green | AHPECG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Green | AHPECG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Green | AHPECG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Red | AHPERR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Red | AHPERR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Red | AHPERR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Red | AHPERR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Pink | AHPESP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Pink | AHPESP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Pink | AHPESP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Pink | AHPESP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Dark Grey | AHPEDG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Dark Grey | AHPEDG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Dark Grey | AHPEDG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Dark Grey | AHPEDG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Peanut Brown | AHPEPB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Peanut Brown | AHPEPB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Peanut Brown | AHPEPB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Peanut Brown | AHPEPB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Brown | AHPEBR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Brown | AHPEBR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Brown | AHPEBR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Brown | AHPEBR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Lake Blue | AHPEAB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Lake Blue | AHPEAB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Lake Blue | AHPEAB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Lake Blue | AHPEAB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Cream | AHPECR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Cream | AHPECR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Cream | AHPECR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Cream | AHPECR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Beige | AHPELB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Beige | AHPELB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Beige | AHPELB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Beige | AHPELB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Forest Green | AHPEFG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Forest Green | AHPEFG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Forest Green | AHPEFG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Forest Green | AHPEFG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Lime Green | AHPELG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Lime Green | AHPELG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Lime Green | AHPELG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Lime Green | AHPELG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Texture Silver | AHPESL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Texture Silver | AHPESL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Texture Silver | AHPESL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Texture Silver | AHPESL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Clear | AHPECL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Clear | AHPECL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Clear | AHPECL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Clear | AHPECL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 16.99 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.35 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 19.83 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Filament | 18.99 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Tropical Turquoise | HPL18-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 19.43 USD | Tropical Turquoise | HPL18-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 21.07 USD | Tropical Turquoise | HPL18-101 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Tropical Turquoise | HPL18-101 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Spring Leaf | HPL19-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 19.43 USD | Spring Leaf | HPL19-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 21.07 USD | Spring Leaf | HPL19-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Spring Leaf | HPL19-101 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Peach Pink | HPL16-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 19.43 USD | Peach Pink | HPL16-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 21.07 USD | Peach Pink | HPL16-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Peach Pink | HPL16-101 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Interstellar Violet | HPL17-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 19.43 USD | Interstellar Violet | HPL17-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 21.07 USD | Interstellar Violet | HPL17-105 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Special | 17.99 USD | Interstellar Violet | HPL17-101 | https://store.anycubic.com/products/pla-basic-special-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Gray | HASGY-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | Gray | HASGY-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | Gray | HASGY-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Gray | HASGY-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | White | HASWH-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | White | HASWH-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | White | HASWH-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | White | HASWH-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Black | HASBK-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | Black | HASBK-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | Black | HASBK-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Black | HASBK-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Red | HASRE-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | Red | HASRE-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | Red | HASRE-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Red | HASRE-101 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Blue | HASBL-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | Blue | HASBL-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | Blue | HASBL-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Blue | HASBL-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Green | HASGR-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 33.47 USD | Green | HASGR-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 37.19 USD | Green | HASGR-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ASA Filament | 30.99 USD | Green | HASGR-102 | https://store.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Grey | HYGGY-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Grey | HYGGY-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Grey | HYGGY-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Grey | HYGGY-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Black | HYGBK-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Black | HYGBK-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Black | HYGBK-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Black | HYGBK-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | White | HYGWT-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | White | HYGWT-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | White | HYGWT-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | White | HYGWT-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Yellow | HYGYL-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Yellow | HYGYL-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Yellow | HYGYL-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Yellow | HYGYL-101 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Blue | HYGBL-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Blue | HYGBL-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Blue | HYGBL-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Blue | HYGBL-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Green-Brown | HYGGB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Green-Brown | HYGGB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Green-Brown | HYGGB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Green-Brown | HYGGB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Green | HYGGR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Green | HYGGR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Green | HYGGR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Green | HYGGR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Ice Blue | HYGIB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Ice Blue | HYGIB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Ice Blue | HYGIB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Ice Blue | HYGIB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Orange | HYGOR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Orange | HYGOR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Orange | HYGOR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Orange | HYGOR-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Purple | HYGPU-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Purple | HYGPU-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Purple | HYGPU-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Purple | HYGPU-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Red-Blue | HYGRB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Red-Blue | HYGRB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Red-Blue | HYGRB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Red-Blue | HYGRB-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Red | HYGRE-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Red | HYGRE-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Red | HYGRE-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Red | HYGRE-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Sakura Pink | HYGSP-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 24.83 USD | Sakura Pink | HYGSP-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 27.27 USD | Sakura Pink | HYGSP-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Matte | 22.99 USD | Sakura Pink | HYGSP-102 | https://store.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Pink | AHPETK-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Olive | AHPETL-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Grey | AHPETG-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Brown | AHPETW-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Orange | AHPETO-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Purple | AHPETP-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Blue | AHPETB-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 18.35 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 19.83 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PETG Translucent | 16.99 USD | Translucent Green | AHPETR-101 | https://store.anycubic.com/products/petg-filament-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Rainbow | AHSCRB1-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Rainbow | AHSCRB1-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Rainbow | AHSCRB1-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Rainbow | AHSCRB1-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | White | AHSCWH-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | White | AHSCWH-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | White | AHSCWH-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | White | AHSCWH-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Christmas Green | AHSCCG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Christmas Green | AHSCCG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Christmas Green | AHSCCG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Christmas Green | AHSCCG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Silver | AHSCSL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Silver | AHSCSL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Silver | AHSCSL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Silver | AHSCSL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Light Gold | AHSCGD-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Light Gold | AHSCGD-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Light Gold | AHSCGD-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Light Gold | AHSCGD-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Blue | AHSCBL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Blue | AHSCBL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Blue | AHSCBL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Blue | AHSCBL-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Copper | AHSCCO-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Copper | AHSCCO-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Copper | AHSCCO-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Copper | AHSCCO-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Christmas Red | AHSCCR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Christmas Red | AHSCCR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Christmas Red | AHSCCR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Christmas Red | AHSCCR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Green | AHSCGR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Green | AHSCGR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Green | AHSCGR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Green | AHSCGR-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Pink | AHSCPK-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Pink | AHSCPK-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Pink | AHSCPK-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Pink | AHSCPK-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Gray | HSCGY-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Gray | HSCGY-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Gray | HSCGY-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Gray | HSCGY-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Purple | AHSCPU-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Purple | AHSCPU-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Purple | AHSCPU-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Purple | AHSCPU-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Shiny Gold | AHSCSG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Shiny Gold | AHSCSG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Shiny Gold | AHSCSG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Shiny Gold | AHSCSG-102 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Metal Blue | HSCML-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 24.83 USD | Metal Blue | HSCML-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 27.27 USD | Metal Blue | HSCML-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk | 22.99 USD | Metal Blue | HSCML-101 | https://store.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Grey | HTPGY-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Grey | HTPGY-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Grey | HTPGY-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Grey | HTPGY-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Black | HTPBK-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Black | HTPBK-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Black | HTPBK-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Black | HTPBK-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Milky White | HTPMW-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Milky White | HTPMW-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Milky White | HTPMW-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Milky White | HTPMW-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Blue | HTPCB-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Blue | HTPCB-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Blue | HTPCB-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Blue | HTPCB-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Green | HTPCG-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Green | HTPCG-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Green | HTPCG-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Green | HTPCG-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Clear | HTPCL-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Clear | HTPCL-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Clear | HTPCL-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Clear | HTPCL-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Orange | HTPCO-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Orange | HTPCO-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Orange | HTPCO-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Orange | HTPCO-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Purple | HTPCP-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Purple | HTPCP-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Purple | HTPCP-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Purple | HTPCP-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Red | HTPCR-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 30.23 USD | Red | HTPCR-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 33.47 USD | Red | HTPCR-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| TPU Filament | 27.99 USD | Red | HTPCR-101 | https://store.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Purple | AHPLPPO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Purple | AHPLPPO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Purple | AHPLPPO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Purple | AHPLPPO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Black | AHPLPBK-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Black | AHPLPBK-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Black | AHPLPBK-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Black | AHPLPBK-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | White | AHPLPBW-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | White | AHPLPBW-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | White | AHPLPBW-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | White | AHPLPBW-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Texture Grey | AHPLPGY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Texture Grey | AHPLPGY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Texture Grey | AHPLPGY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Texture Grey | AHPLPGY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Red | AHPLPRR-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Orange | AHPLPVO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Orange | AHPLPVO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Orange | AHPLPVO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Orange | AHPLPVO-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Pink | AHPLPSP-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Pink | AHPLPSP-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Pink | AHPLPSP-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Pink | AHPLPSP-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Blue | AHPLPDB-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Blue | AHPLPDB-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Blue | AHPLPDB-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Blue | AHPLPDB-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Yellow | AHPLPVY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Yellow | AHPLPVY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Yellow | AHPLPVY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Yellow | AHPLPVY-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Green | AHPLPCG-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 18.35 USD | Green | AHPLPCG-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 19.83 USD | Green | AHPLPCG-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA+ Refill | 16.99 USD | Green | AHPLPCG-A108 | https://store.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Red Blue | AHSC13-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Red Blue | AHSC13-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Red Blue | AHSC13-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Red Blue | AHSC13-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Blue | AHSC08-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Black Blue | AHSC08-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Black Blue | AHSC08-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Blue | AHSC08-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Green | AHSC09-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Black Green | AHSC09-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Black Green | AHSC09-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Green | AHSC09-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Red Gold | AHSC12-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Red Gold | AHSC12-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Red Gold | AHSC12-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Red Gold | AHSC12-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Gold | AHSC07-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Black Gold | AHSC07-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Black Gold | AHSC07-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Gold | AHSC07-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Blue Green | AHSC16-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Blue Green | AHSC16-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Blue Green | AHSC16-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Blue Green | AHSC16-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Red | AHSC17-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Black Red | AHSC17-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Black Red | AHSC17-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Red | AHSC17-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Pink Gold | AHSC11-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Pink Gold | AHSC11-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Pink Gold | AHSC11-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Pink Gold | AHSC11-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Purple | AHSC10-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 26.99 USD | Black Purple | AHSC10-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 29.75 USD | Black Purple | AHSC10-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 24.99 USD | Black Purple | AHSC10-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Red Yellow Green | AHSC15-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 28.07 USD | Red Yellow Green | AHSC15-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 30.99 USD | Red Yellow Green | AHSC15-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Red Yellow Green | AHSC15-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Blue Green Purple | AHSC14-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 28.07 USD | Blue Green Purple | AHSC14-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 30.99 USD | Blue Green Purple | AHSC14-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Blue Green Purple | AHSC14-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Red Blue Yellow | AHSC18-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 28.07 USD | Red Blue Yellow | AHSC18-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 30.99 USD | Red Blue Yellow | AHSC18-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Silk Dual/Tri-Color | 25.99 USD | Red Blue Yellow | AHSC18-102 | https://store.anycubic.com/products/silk-pla-dual-tri-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | Grey | HABGY-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 24.83 USD | Grey | HABGY-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 27.27 USD | Grey | HABGY-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | Grey | HABGY-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | Black | HABBK-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 24.83 USD | Black | HABBK-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 27.27 USD | Black | HABBK-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | Black | HABBK-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | White | HABWH-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 24.83 USD | White | HABWH-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 27.27 USD | White | HABWH-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| ABS Filament | 22.99 USD | White | HABWH-102 | https://store.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Blue | AHXKGL-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 26.99 USD | Galaxy Blue | AHXKGL-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 29.75 USD | Galaxy Blue | AHXKGL-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Blue | AHXKGL-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Brown | AHXKGB-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 26.99 USD | Galaxy Brown | AHXKGB-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 29.75 USD | Galaxy Brown | AHXKGB-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Brown | AHXKGB-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Green | AHXKGG-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 26.99 USD | Galaxy Green | AHXKGG-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 29.75 USD | Galaxy Green | AHXKGG-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Green | AHXKGG-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Purple | AHXKGP-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 26.99 USD | Galaxy Purple | AHXKGP-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 29.75 USD | Galaxy Purple | AHXKGP-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Galaxy | 24.99 USD | Galaxy Purple | AHXKGP-101 | https://store.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 23.99 USD | Marble White | AHLSMW-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 25.91 USD | Marble White | AHLSMW-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 28.51 USD | Marble White | AHLSMW-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 23.99 USD | Marble White | AHLSMW-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 23.99 USD | Brick Red | AHLSBR-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 25.91 USD | Brick Red | AHLSBR-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 28.51 USD | Brick Red | AHLSBR-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Marble | 23.99 USD | Brick Red | AHLSBR-101 | https://store.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Black | HJSMB-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 25.91 USD | Metal Black | HJSMB-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 28.51 USD | Metal Black | HJSMB-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Black | HJSMB-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Champagne | HJSMC-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 25.91 USD | Metal Champagne | HJSMC-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 28.51 USD | Metal Champagne | HJSMC-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Champagne | HJSMC-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Copper | HJSMO-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 25.91 USD | Metal Copper | HJSMO-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 28.51 USD | Metal Copper | HJSMO-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Copper | HJSMO-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Blue | HJSML-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 25.91 USD | Metal Blue | HJSML-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 28.51 USD | Metal Blue | HJSML-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Metal | 23.99 USD | Metal Blue | HJSML-101 | https://store.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Blue | HFGBL-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 33.47 USD | Glow Blue | HFGBL-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 37.19 USD | Glow Blue | HFGBL-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Blue | HFGBL-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Green | HFGGR-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 33.47 USD | Glow Green | HFGGR-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 37.19 USD | Glow Green | HFGGR-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Green | HFGGR-101 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Yellow | HFGYE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 33.47 USD | Glow Yellow | HFGYE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 37.19 USD | Glow Yellow | HFGYE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Glow Yellow | HFGYE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Blue | HFGBE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 33.47 USD | Blue | HFGBE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 37.19 USD | Blue | HFGBE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Blue | HFGBE-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Green | HFGGN-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 33.47 USD | Green | HFGGN-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 37.19 USD | Green | HFGGN-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |
| PLA Glow | 30.99 USD | Green | HFGGN-103 | https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl |

### Color, Color-Code, Filaments (US/EN-Names)
| Color | ID | Products |
| --- | --- | --- |
| Black Gold | 07 | PLA Silk Dual/Tri-Color |
| Black Blue | 08 | PLA Silk Dual/Tri-Color |
| Black Green | 09 | PLA Silk Dual/Tri-Color |
| Black Purple | 10 | PLA Silk Dual/Tri-Color |
| Pink Gold | 11 | PLA Silk Dual/Tri-Color |
| Red Gold | 12 | PLA Silk Dual/Tri-Color |
| Red Blue | 13 | PLA Silk Dual/Tri-Color |
| Blue Green Purple | 14 | PLA Silk Dual/Tri-Color |
| Red Yellow Green | 15 | PLA Silk Dual/Tri-Color |
| Blue Green, Peach Pink | 16 | PLA Silk Dual/Tri-Color, PLA Special, PLA+ |
| Black Red, Interstellar Violet | 17 | PLA Silk Dual/Tri-Color, PLA Special, PLA+ |
| Red Blue Yellow, Tropical Turquoise | 18 | PLA Silk Dual/Tri-Color, PLA Special, PLA+ |
| Spring Leaf | 19 | PLA Special, PLA+ |
| Lake Blue | AB | PETG Filament |
| Rainbow | B1 | PLA Silk |
| Blue | BE | PLA Glow |
| Black | BK | ABS Filament, ASA Filament, PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA Matte, PLA+, PLA+ Refill, TPU Filament |
| Blue, Glow Blue | BL | ASA Filament, PLA Glow, PLA High Speed, PLA Matte, PLA Silk |
| Brick Red, Bright Red, Brown, Red | BR | PETG Filament, PLA Basic, PLA High Speed, PLA Marble, PLA+ |
| Bright White, White | BW | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA+, PLA+ Refill |
| Bronze | BZ | PLA Basic |
| Blue | CB | TPU Filament |
| Christmas Green, Classic Green, Green | CG | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA Silk, PLA+, PLA+ Refill, TPU Filament |
| Clear | CL | PETG Filament, PLA Basic, TPU Filament |
| Copper, Orange | CO | PLA Silk, TPU Filament |
| Purple | CP | TPU Filament |
| Christmas Red, Cream, Red | CR | PETG Filament, PLA Silk, TPU Filament |
| Cyan | CY | PLA Basic |
| Blue, Blue (Navy blue), Dazzling Blue | DB | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA+, PLA+ Refill |
| Dark Grey | DG | PETG Filament |
| Forest Green | FG | PETG Filament |
| Galaxy Brown, Green-Brown | GB | PLA Galaxy, PLA Matte |
| Light Gold | GD | PLA Silk |
| Gray, Grey | GE | PETG Filament, PLA Basic, PLA+ |
| FLash Green, Green Flash | GF | PLA Basic, PLA+ |
| Galaxy Green | GG | PLA Galaxy |
| Galaxy Blue | GL | PLA Galaxy |
| Green | GN | PLA Glow |
| Galaxy Purple | GP | PLA Galaxy |
| Glow Green, Green | GR | ASA Filament, PLA Glow, PLA High Speed, PLA Matte, PLA Silk |
| Gray, Grey, Texture Gray, Texture Grey | GY | ABS Filament, ASA Filament, PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA Matte, PLA Silk, PLA+, PLA+ Refill, TPU Filament |
| Ice Blue | IB | PLA Matte |
| Dark Brown | KB | PLA Basic |
| Beige, Light Blue | LB | PETG Filament, PLA Basic, PLA+ |
| Lime Green | LG | PETG Filament |
| Metal Black | MB | PLA Metal |
| Metal Champagne | MC | PLA Metal |
| Magenta | MG | PLA Basic |
| Metal Blue | ML | PLA Metal, PLA Silk |
| Metal Copper | MO | PLA Metal |
| Marble White, Milky White | MW | PLA Marble, TPU Filament |
| Orange, Vibrant Orange | OR | PLA High Speed, PLA Matte |
| Peanut Brown | PB | PETG Filament |
| Pink | PK | PLA Silk |
| Purple, Purple Opulence | PO | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA+, PLA+ Refill |
| Purple | PU | PLA Matte, PLA Silk |
| Red-Blue | RB | PLA Matte |
| Red | RE | ASA Filament, PLA High Speed, PLA Matte |
| Red | RR | PETG Filament, PLA Basic, PLA Basic Refill, PLA+, PLA+ Refill |
| Shiny Gold | SG | PLA Silk |
| Silver, Texture Silver | SL | PETG Filament, PLA Basic, PLA Silk, PLA+ |
| Pink, Sakura Pink, Strawberry Pink | SP | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA Matte, PLA+, PLA+ Refill |
| Translucent Blue | TB | PETG Filament, PETG Translucent |
| Translucent Grey | TG | PETG Filament, PETG Translucent |
| Translucent Pink | TK | PETG Filament, PETG Translucent |
| Translucent Olive | TL | PETG Filament, PETG Translucent |
| Translucent Orange | TO | PETG Filament, PETG Translucent |
| Translucent Purple | TP | PETG Filament, PETG Translucent |
| Translucent Green | TR | PETG Filament, PETG Translucent |
| Translucent Brown | TW | PETG Filament, PETG Translucent |
| Orange, Vibrant Orange | VO | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA+, PLA+ Refill |
| Vibrant Yellow, Yellow | VY | PETG Filament, PLA Basic, PLA Basic Refill, PLA High Speed, PLA+, PLA+ Refill |
| Bright White, White | WH | ABS Filament, ASA Filament, PLA High Speed, PLA Silk |
| White | WT | PLA Matte |
| Glow Yellow | YE | PLA Glow |
| Yellow | YL | PLA Matte |

## Pretty-Table (terminal fitted) :-)
<img width="1171" height="587" alt="image" src="https://github.com/user-attachments/assets/5290d8a4-6b25-4f5c-9099-bfaa1093520e" />

# Deep dive into SKU interpretation
| Segment | Meaning | Example | Comment |
|----------|----------|----------|----------|
| **A** | Series / generation prefix (optional) | `A` in `AHPLBK-105` | Usually stands for *Anycubic* or a series ID |
| **H** | Core filament prefix | `H` | Present in all filament SKUs = `H` Header/Hotend ?|
| **<Subcode>** | Material group and subtype | `PLP` | Defines material (PLA, PETG, TPU, etc.) |
| **<ColorCode>** | 2–3 letter color code | `BK`, `GY`, `PO` | Matches the official color abbreviation |
| **-<Number>** | Version or revision code | `-105` | Usually 101–107; internal versioning or batch |

> `H`=Hotend maybe these SKUs are for FDM-Filaments. Will check if resin have simlar codings
---

## 2️⃣ Breakdown by Material Type

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

## 3️⃣ Special Observations

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

## 4️⃣ Master Prefix Map

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

## 5️⃣ Meaning of Letter Blocks

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

## Complete list of SKUs, Colors, Filaments
| SKU | Filament | Color |
| --- | --- | --- |
| AHHSBK-102 | PLA High Speed | Black |
| AHHSBR-102 | PLA High Speed | Red |
| AHHSBW-101 | PLA High Speed | Bright White |
| AHHSCG-101 | PLA High Speed | Green |
| AHHSDB-101 | PLA High Speed | Blue |
| AHHSGY-102 | PLA High Speed | Texture Grey |
| AHHSGY-103 | PLA High Speed | Texture Grey |
| AHHSPO-102 | PLA High Speed | Purple |
| AHHSSP-102 | PLA High Speed | Strawberry Pink |
| AHHSVO-102 | PLA High Speed | Vibrant Orange |
| AHHSVY-103 | PLA High Speed | Yellow |
| AHLSBR-101 | PLA Marble | Brick Red |
| AHLSMW-101 | PLA Marble | Marble White |
| AHPEAB-101 | PETG Filament | Lake Blue |
| AHPEBK-101 | PETG Filament | Black |
| AHPEBR-101 | PETG Filament | Brown |
| AHPEBW-101 | PETG Filament | White |
| AHPECG-101 | PETG Filament | Green |
| AHPECL-101 | PETG Filament | Clear |
| AHPECR-101 | PETG Filament | Cream |
| AHPEDB-101 | PETG Filament | Blue |
| AHPEDG-101 | PETG Filament | Dark Grey |
| AHPEFG-101 | PETG Filament | Forest Green |
| AHPEGE-101 | PETG Filament | Grey |
| AHPEGY-101 | PETG Filament | Texture Grey |
| AHPELB-101 | PETG Filament | Beige |
| AHPELG-101 | PETG Filament | Lime Green |
| AHPEPB-101 | PETG Filament | Peanut Brown |
| AHPEPO-101 | PETG Filament | Purple |
| AHPERR-101 | PETG Filament | Red |
| AHPESL-101 | PETG Filament | Texture Silver |
| AHPESP-101 | PETG Filament | Pink |
| AHPETB-101 | PETG Filament | Translucent Blue |
| AHPETG-101 | PETG Filament | Translucent Grey |
| AHPETK-101 | PETG Filament | Translucent Pink |
| AHPETL-101 | PETG Filament | Translucent Olive |
| AHPETO-101 | PETG Filament | Translucent Orange |
| AHPETP-101 | PETG Filament | Translucent Purple |
| AHPETR-101 | PETG Filament | Translucent Green |
| AHPETW-101 | PETG Filament | Translucent Brown |
| AHPEVO-101 | PETG Filament | Orange |
| AHPEVY-101 | PETG Filament | Yellow |
| AHPLBK-105 | PLA Basic | Black |
| AHPLBK-A106 | PLA Basic Refill | Black |
| AHPLBR-105 | PLA Basic | Brown |
| AHPLBW-105 | PLA Basic | White |
| AHPLBW-A106 | PLA Basic Refill | White |
| AHPLBZ-105 | PLA Basic | Bronze |
| AHPLCG-105 | PLA Basic | Classic Green |
| AHPLCG-A106 | PLA Basic Refill | Green |
| AHPLCL-105 | PLA Basic | Clear |
| AHPLCY-105 | PLA Basic | Cyan |
| AHPLDB-105 | PLA Basic | Blue (Navy blue) |
| AHPLDB-A106 | PLA Basic Refill | Blue |
| AHPLGE-106 | PLA Basic | Gray |
| AHPLGF-105 | PLA Basic | FLash Green |
| AHPLGY-105 | PLA Basic | Texture Gray |
| AHPLGY-A106 | PLA Basic Refill | Texture Grey |
| AHPLKB-105 | PLA Basic | Dark Brown |
| AHPLLB-105 | PLA Basic | Beige |
| AHPLMG-105 | PLA Basic | Magenta |
| AHPLP16-107 | PLA+ | Peach Pink |
| AHPLP17-107 | PLA+ | Interstellar Violet |
| AHPLP18-107 | PLA+ | Tropical Turquoise |
| AHPLP19-107 | PLA+ | Spring Leaf |
| AHPLPBK-102 | PLA+ | Black |
| AHPLPBK-A108 | PLA+ Refill | Black |
| AHPLPBR-106 | PLA+ | Bright Red |
| AHPLPBR-107 | PLA+ | Brown |
| AHPLPBW-102 | PLA+ | Bright White |
| AHPLPBW-A108 | PLA+ Refill | White |
| AHPLPCG-107 | PLA+ | Green |
| AHPLPCG-A108 | PLA+ Refill | Green |
| AHPLPDB-102 | PLA+ | Dazzling Blue |
| AHPLPDB-A108 | PLA+ Refill | Blue |
| AHPLPGE-107 | PLA+ | Grey |
| AHPLPGF-102 | PLA+ | Green Flash |
| AHPLPGY-102 | PLA+ | Texture Grey |
| AHPLPGY-A108 | PLA+ Refill | Texture Grey |
| AHPLPLB-101 | PLA+ | Light Blue |
| AHPLPLB-108 | PLA+ | Beige |
| AHPLPO-105 | PLA Basic | Purple |
| AHPLPO-A106 | PLA Basic Refill | Purple |
| AHPLPPO-102 | PLA+ | Purple Opulence |
| AHPLPPO-A108 | PLA+ Refill | Purple |
| AHPLPRR-A108 | PLA+ | Red |
| AHPLPSL-102 | PLA+ | Silver |
| AHPLPSP-107 | PLA+ | Pink |
| AHPLPSP-A108 | PLA+ Refill | Pink |
| AHPLPVO-102 | PLA+ | Vibrant Orange |
| AHPLPVO-A108 | PLA+ Refill | Orange |
| AHPLPVY-101 | PLA+ | Vibrant Yellow |
| AHPLPVY-A108 | PLA+ Refill | Yellow |
| AHPLRR-105 | PLA Basic | Red |
| AHPLRR-A106 | PLA Basic Refill | Red |
| AHPLSL-105 | PLA Basic | Texture Silver |
| AHPLSP-105 | PLA Basic | Pink |
| AHPLSP-A106 | PLA Basic Refill | Pink |
| AHPLVO-105 | PLA Basic | Orange |
| AHPLVO-A106 | PLA Basic Refill | Orange |
| AHPLVY-105 | PLA Basic | Yellow |
| AHPLVY-A106 | PLA Basic Refill | Yellow |
| AHSC07-102 | PLA Silk Dual/Tri-Color | Black Gold |
| AHSC08-102 | PLA Silk Dual/Tri-Color | Black Blue |
| AHSC09-102 | PLA Silk Dual/Tri-Color | Black Green |
| AHSC10-102 | PLA Silk Dual/Tri-Color | Black Purple |
| AHSC11-102 | PLA Silk Dual/Tri-Color | Pink Gold |
| AHSC12-102 | PLA Silk Dual/Tri-Color | Red Gold |
| AHSC13-102 | PLA Silk Dual/Tri-Color | Red Blue |
| AHSC14-102 | PLA Silk Dual/Tri-Color | Blue Green Purple |
| AHSC15-102 | PLA Silk Dual/Tri-Color | Red Yellow Green |
| AHSC16-102 | PLA Silk Dual/Tri-Color | Blue Green |
| AHSC17-102 | PLA Silk Dual/Tri-Color | Black Red |
| AHSC18-102 | PLA Silk Dual/Tri-Color | Red Blue Yellow |
| AHSCBL-102 | PLA Silk | Blue |
| AHSCCG-102 | PLA Silk | Christmas Green |
| AHSCCO-102 | PLA Silk | Copper |
| AHSCCR-102 | PLA Silk | Christmas Red |
| AHSCGD-102 | PLA Silk | Light Gold |
| AHSCGR-102 | PLA Silk | Green |
| AHSCPK-102 | PLA Silk | Pink |
| AHSCPU-102 | PLA Silk | Purple |
| AHSCRB1-102 | PLA Silk | Rainbow |
| AHSCSG-102 | PLA Silk | Shiny Gold |
| AHSCSL-102 | PLA Silk | Silver |
| AHSCWH-102 | PLA Silk | White |
| AHXKGB-101 | PLA Galaxy | Galaxy Brown |
| AHXKGG-101 | PLA Galaxy | Galaxy Green |
| AHXKGL-101 | PLA Galaxy | Galaxy Blue |
| AHXKGP-101 | PLA Galaxy | Galaxy Purple |
| HABBK-102 | ABS Filament | Black |
| HABGY-102 | ABS Filament | Grey |
| HABWH-102 | ABS Filament | White |
| HASBK-101 | ASA Filament | Black |
| HASBL-102 | ASA Filament | Blue |
| HASGR-102 | ASA Filament | Green |
| HASGY-101 | ASA Filament | Gray |
| HASRE-101 | ASA Filament | Red |
| HASWH-101 | ASA Filament | White |
| HFGBE-103 | PLA Glow | Blue |
| HFGBL-101 | PLA Glow | Glow Blue |
| HFGGN-103 | PLA Glow | Green |
| HFGGR-101 | PLA Glow | Glow Green |
| HFGYE-103 | PLA Glow | Glow Yellow |
| HHSBK-101 | PLA High Speed | Black |
| HHSBL-101 | PLA High Speed | Blue |
| HHSGR-102 | PLA High Speed | Green |
| HHSOR-102 | PLA High Speed | Vibrant Orange |
| HHSRE-101 | PLA High Speed | Red |
| HHSWH-101 | PLA High Speed | Bright White |
| HJSMB-101 | PLA Metal | Metal Black |
| HJSMC-101 | PLA Metal | Metal Champagne |
| HJSML-101 | PLA Metal | Metal Blue |
| HJSMO-101 | PLA Metal | Metal Copper |
| HPL16-101 | PLA Special | Peach Pink |
| HPL16-105 | PLA Special | Peach Pink |
| HPL17-101 | PLA Special | Interstellar Violet |
| HPL17-105 | PLA Special | Interstellar Violet |
| HPL18-101 | PLA Special | Tropical Turquoise |
| HPL18-105 | PLA Special | Tropical Turquoise |
| HPL19-101 | PLA Special | Spring Leaf |
| HPL19-105 | PLA Special | Spring Leaf |
| HSCGY-101 | PLA Silk | Gray |
| HSCML-101 | PLA Silk | Metal Blue |
| HTPBK-101 | TPU Filament | Black |
| HTPCB-101 | TPU Filament | Blue |
| HTPCG-101 | TPU Filament | Green |
| HTPCL-101 | TPU Filament | Clear |
| HTPCO-101 | TPU Filament | Orange |
| HTPCP-101 | TPU Filament | Purple |
| HTPCR-101 | TPU Filament | Red |
| HTPGY-101 | TPU Filament | Grey |
| HTPMW-101 | TPU Filament | Milky White |
| HYGBK-101 | PLA Matte | Black |
| HYGBL-102 | PLA Matte | Blue |
| HYGGB-102 | PLA Matte | Green-Brown |
| HYGGR-102 | PLA Matte | Green |
| HYGGY-102 | PLA Matte | Grey |
| HYGIB-102 | PLA Matte | Ice Blue |
| HYGOR-102 | PLA Matte | Orange |
| HYGPU-102 | PLA Matte | Purple |
| HYGRB-102 | PLA Matte | Red-Blue |
| HYGRE-102 | PLA Matte | Red |
| HYGSP-102 | PLA Matte | Sakura Pink |
| HYGWT-101 | PLA Matte | White |
| HYGYL-101 | PLA Matte | Yellow |
# SKU-Conclusion
- A? → optional “Anycubic” prefix
- H → main header
- subcode → material type identifier
- color → color code (2–3 letters or with numeric suffix)
- A?num → optional serial or refill number

The Anycubic SKU structure is consistent and logically organized:
- AH = brand + filament prefix
- The subcode precisely identifies the material family and subtype
- Variants like Glow, Marble, Matte, and Galaxy have unique, fixed subcodes
- Refill versions always include an extra “A” before the numeric code

My subjective impression is that the color codes are not exactly unique but depend on the sub-type.



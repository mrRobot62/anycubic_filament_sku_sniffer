# How to use the sniffer :-)

## Parameters
`--url` : whicht AC side shoud be sniffed. Possibel to use this parameter several times
`--region`: however between US/EN & DE websides there are different source codes which are searched for SKUs
`--with-source`: if set, the URL is printed in the table as well
`--out`: create an output file 
`--md`: instead of PrettyTable use Markdown table
`--unique-colors`: create a second table with unique color-codes (part of SKU) for all Filaments. Hu. AC use same color-code but name them differently.

# Simple US-Example with three US-Websides
- output into a file
- use markdown as output table
- print url inside table
- create a unique-color table additionally

anycubic-nfc-filament % python sniff_anycubic_sites4.py \
--url "https://store.anycubic.com/products/pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--url "https://store.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl" \
--with-source --out result_en_md2.txt --unique-colors --region us --md

# All US-Filaments
python ac_filament_sniffer.py \
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

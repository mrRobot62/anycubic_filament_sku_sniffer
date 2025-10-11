# How to use the sniffer :-)

## Parameters
`--url` : whicht AC side shoud be sniffed. Possibel to use this parameter several times
`--region`: however between US/EN & DE websides there are different source codes which are searched for SKUs. German is default `--region de`, `--region us`, `--region en`
`--with-source`: if set, the URL is printed in the table as well
`--out`: create an output file 
`--md`: instead of PrettyTable use Markdown table
`--unique-colors`: create a second table with unique color-codes (part of SKU) for all Filaments. Hu. AC use same color-code but name them differently.

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

# Example Output
## Pretty-Table
Product                 | Price     | Color                        | SKU          | Source                                                                                        
------------------------+-----------+------------------------------+--------------+-----------------------------------------------------------------------------------------------
PLA Basic               | 17.99 EUR | Weiß / 1KG                   | AHPLBW-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Schwarz / 1KG                | AHPLBK-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Strukturgrau / 1KG           | AHPLGY-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Klar / 1KG                   | AHPLCL-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Rot / 1KG                    | AHPLRR-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Struktursilber / 1KG         | AHPLSL-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Grün / 1KG                   | AHPLCG-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Lila / 1KG                   | AHPLPO-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Beige / 1KG                  | AHPLLB-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Bronze / 1KG                 | AHPLBZ-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Magenta / 1KG                | AHPLMG-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Gelb / 1KG                   | AHPLVY-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Rosa / 1KG                   | AHPLSP-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Orange / 1KG                 | AHPLVO-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Braun / 1KG                  | AHPLBR-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Cyan / 1KG                   | AHPLCY-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Blau (Marineblau) / 1KG      | AHPLDB-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Grüner Blitz / 1KG           | AHPLGF-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Dunkelbraun / 1KG            | AHPLKB-105   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA Basic               | 17.99 EUR | Grau / 1KG                   | AHPLGE-106   | https://de.anycubic.com/products/pla-filament?variant=32866809217101                          
PLA High Speed          | 18.99 EUR | Perlschwarz / 1KG            | AHHSBK-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Strukturgrau / 1KG           | AHHSGY-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Strahlendes Weiß / 1KG       | AHHSBW-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Leuchtendes Rot / 1KG        | AHHSBR-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Strahlendes Blau / 1KG       | AHHSDB-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Klassisches Grün / 1KG       | AHHSCG-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Lebendiges Orange / 1KG      | AHHSVO-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Erdbeerrosa / 1KG            | AHHSSP-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Leuchtendes Gelb / 1KG       | AHHSVY-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA High Speed          | 18.99 EUR | Prachtlila / 1KG             | AHHSPO-102   | https://de.anycubic.com/products/high-speed-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA+                    | 18.99 EUR | Strukturgrau / 1KG           | AHPLPGY-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Schwarz / 1KG                | AHPLPBK-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Weiß / 1KG                   | AHPLPBW-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Blau / 1KG                   | AHPLPDB-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Grüner Blitz / 1KG           | AHPLPGF-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Orange / 1KG                 | AHPLPVO-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Lila / 1KG                   | AHPLPPO-103  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Leuchtendes Rot / 1KG        | AHPLPBR-106  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Silber / 1KG                 | AHPLPSL-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Gelb / 1KG                   | AHPLPVY-102  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Hellblau / 1KG               | AHPLPLB-106  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Pfirsichrosa / 1KG           | AHPLP16-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Interstellar Violett / 1KG   | AHPLP17-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Tropisches Türkis / 1KG      | AHPLP18-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Frühlingsblatt / 1KG         | AHPLP19-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Grün / 1KG                   | AHPLPCG-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Grau / 1KG                   | AHPLPGE-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Rot / 1KG                    | AHPLPRR-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Rosa / 1KG                   | AHPLPSP-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Braun / 1KG                  | AHPLPBR-107  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA+                    | 18.99 EUR | Beige / 1KG                  | AHPLPLB-108  | https://de.anycubic.com/products/pla-plus-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Basic Refill        | 15.99 EUR | Schwarz / 1KG                | AHPLBK-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Strukturgrau / 1KG           | AHPLGY-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Weiß / 1KG                   | AHPLBW-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Rot / 1KG                    | AHPLRR-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Rosa / 1KG                   | AHPLSP-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Orange / 1KG                 | AHPLVO-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Gelb / 1KG                   | AHPLVY-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Grün / 1KG                   | AHPLCG-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Blau / 1KG                   | AHPLDB-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Basic Refill        | 15.99 EUR | Lila / 1KG                   | AHPLPO-A106  | https://de.anycubic.com/products/pla-basic-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG                    | 16.99 EUR | Schwarz / 1KG                | AHPEBK-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Weiß / 1KG                   | AHPEBW-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Strukturgrau / 1KG           | AHPEGY-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Orange / 1KG                 | AHPEVO-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Lila / 1KG                   | AHPEPO-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Blau / 1KG                   | AHPEDB-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Klar / 1KG                   | AHPECL-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Grün / 1KG                   | AHPECG-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Gelb / 1KG                   | AHPEVY-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | See-Blau / 1KG               | AHPEAB-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Braun / 1KG                  | AHPEBR-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Creme / 1KG                  | AHPECR-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Dunkelgrau / 1KG             | AHPEDG-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Waldgrün / 1KG               | AHPEFG-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Grau (PETG) / 1KG            | AHPEGE-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Beige (PETG) / 1KG           | AHPELB-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Limettengrün / 1KG           | AHPELG-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Erdnussbraun / 1KG           | AHPEPB-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Struktursilber / 1KG         | AHPESL-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Rosa (PETG) / 1KG            | AHPESP-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PETG                    | 16.99 EUR | Rot / 1KG                    | AHPERR-101   | https://de.anycubic.com/products/petg-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                   
PLA Spezial             | 17.99 EUR | Tropisches Türkis / 1KG      | HPL18-105    | https://de.anycubic.com/products/pla-basic-spezial-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl
PLA Spezial             | 17.99 EUR | Frühlingsblatt / 1KG         | HPL19-105    | https://de.anycubic.com/products/pla-basic-spezial-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl
PLA Spezial             | 17.99 EUR | Pfirsichrosa / 1KG           | HPL16-105    | https://de.anycubic.com/products/pla-basic-spezial-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl
PLA Spezial             | 17.99 EUR | Interstellar Violett / 1KG   | HPL17-105    | https://de.anycubic.com/products/pla-basic-spezial-color-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl
ASA                     | 30.99 EUR | Weiß / 1KG                   | HASWH-101    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ASA                     | 30.99 EUR | Schwarz / 1KG                | HASBK-101    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ASA                     | 30.99 EUR | Grau / 1KG                   | HASGY-101    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ASA                     | 30.99 EUR | Rot / 1KG                    | HASRE-101    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ASA                     | 30.99 EUR | Grün / 1KG                   | HASGR-102    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ASA                     | 30.99 EUR | Blau / 1KG                   | HASBL-102    | https://de.anycubic.com/products/asa-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
PLA Matte               | 22.99 EUR | Schwarz / 1KG                | HYGBK-101    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Weiß / 1KG                   | HYGWT-101    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Grau / 1KG                   | HYGGY-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Rot / 1KG                    | HYGRE-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Sakura-Rosa / 1KG            | HYGSP-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Rot-Blau / 1KG               | HYGRB-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Lila / 1KG                   | HYGPU-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Orange / 1KG                 | HYGOR-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Eisblau / 1KG                | HYGIB-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Grün / 1KG                   | HYGGR-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Grün-Braun / 1KG             | HYGGB-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Blau / 1KG                   | HYGBL-102    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Matte               | 22.99 EUR | Gelb / 1KG                   | HYGYL-101    | https://de.anycubic.com/products/matte-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PETG Translucent        | 16.99 EUR | Klar / 1KG                   | AHPECL-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Blau / 1KG     | AHPETB-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Grau / 1KG     | AHPETG-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Rosa / 1KG     | AHPETK-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Olivgrün / 1KG | AHPETL-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Orange / 1KG   | AHPETO-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Lila / 1KG     | AHPETP-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Grün / 1KG     | AHPETR-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PETG Translucent        | 16.99 EUR | Transparentes Braun / 1KG    | AHPETW-101   | https://de.anycubic.com/products/petg-translucent?_sasdk=faW5mb0BtYmstZ2JyLmRl                
PLA Silk                | 22.99 EUR | Regenbogen / 1KG*1           | AHSCRB1-102  | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Silber / 1KG*1               | AHSCSL-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Gold / 1KG*1                 | AHSCGD-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Weiß / 1KG*1                 | AHSCWH-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Metallblau / 1KG*1           | HSCML-101    | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Grau / 1KG*1                 | HSCGY-101    | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Glänzendes Gold / 1KG*1      | AHSCSG-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Weihnachtsgrün / 1KG*1       | AHSCCG-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Weihnachtsrot / 1KG*1        | AHSCCR-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Kupfer / 1KG*1               | AHSCCO-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Grün / 1KG*1                 | AHSCGR-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Rosa / 1KG*1                 | AHSCPK-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Lila / 1KG*1                 | AHSCPU-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
PLA Silk                | 22.99 EUR | Blau / 1KG*1                 | AHSCBL-102   | https://de.anycubic.com/products/silk-pla-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl               
TPU Filament            | 27.99 EUR | Schwarz / 1KG                | HTPBK-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Milchweiß / 1KG              | HTPMW-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Grau / 1KG                   | HTPGY-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar Blau / 1KG              | HTPCB-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar Grün / 1KG              | HTPCG-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar / 1KG                   | HTPCL-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar Orange / 1KG            | HTPCO-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar Lila / 1KG              | HTPCP-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
TPU Filament            | 27.99 EUR | Klar Rot / 1KG               | HTPCR-101    | https://de.anycubic.com/products/tpu-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
PLA+ Refill             | 16.99 EUR | Schwarz / 1KG                | AHPLPBK-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Weiß / 1KG                   | AHPLPBW-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Strukturgrau / 1KG           | AHPLPGY-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Rot / 1KG                    | AHPLPRR-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Blau / 1KG                   | AHPLPDB-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Gelb / 1KG                   | AHPLPVY-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Grün / 1KG                   | AHPLPCG-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Orange / 1KG                 | AHPLPVO-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Lila / 1KG                   | AHPLPPO-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA+ Refill             | 16.99 EUR | Rosa / 1KG                   | AHPLPSP-A108 | https://de.anycubic.com/products/pla-refill?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Silk Dual/Tri-Color | 24.99 EUR | Schwarz Gold / 1KG           | AHSC07-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Schwarz Blau / 1KG           | AHSC08-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Schwarz Grün / 1KG           | AHSC09-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Schwarz Lila / 1KG           | AHSC10-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Rosa Gold / 1KG              | AHSC11-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Rot Gold / 1KG               | AHSC12-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Rot Blau / 1KG               | AHSC13-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 25.99 EUR | Blau Grün Lila / 1KG         | AHSC14-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 25.99 EUR | Rot Gelb Grün / 1KG          | AHSC15-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Blau Grün / 1KG              | AHSC16-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 24.99 EUR | Schwarz Rot / 1KG            | AHSC17-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
PLA Silk Dual/Tri-Color | 25.99 EUR | Rot Blau Gelb / 1KG          | AHSC18-102   | https://de.anycubic.com/products/silk-pla-dual-tri-color?_sasdk=faW5mb0BtYmstZ2JyLmRl         
ABS Filament            | 22.99 EUR | Schwarz / 1KG                | HABBK-102    | https://de.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ABS Filament            | 22.99 EUR | Weiß / 1KG                   | HABWH-102    | https://de.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
ABS Filament            | 22.99 EUR | Grau / 1KG                   | HABGY-102    | https://de.anycubic.com/products/abs-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl                    
PLA Galaxy              | 24.99 EUR | Galaxy Braun / 1KG           | AHXKGB-101   | https://de.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Galaxy              | 24.99 EUR | Galaxy Grün / 1KG            | AHXKGG-101   | https://de.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Galaxy              | 24.99 EUR | Galaxy Blau / 1KG            | AHXKGL-101   | https://de.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Galaxy              | 24.99 EUR | Galaxy Lila / 1KG            | AHXKGP-101   | https://de.anycubic.com/products/pla-galaxy?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Marble              | 23.99 EUR | Marmorweiß / 1KG             | AHLSMW-101   | https://de.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Marble              | 23.99 EUR | Ziegelrot / 1KG              | AHLSBR-101   | https://de.anycubic.com/products/pla-marble?_sasdk=faW5mb0BtYmstZ2JyLmRl                      
PLA Metal               | 23.99 EUR | Metall Schwarz / 1KG         | HJSMB-101    | https://de.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Metal               | 23.99 EUR | Metall Champagner / 1KG      | HJSMC-101    | https://de.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Metal               | 23.99 EUR | Metall Blau / 1KG            | HJSML-101    | https://de.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Metal               | 23.99 EUR | Metall Kupfer / 1KG          | HJSMO-101    | https://de.anycubic.com/products/pla-metal-filament?_sasdk=faW5mb0BtYmstZ2JyLmRl              
PLA Glow                | 30.99 EUR | Nachleuchtendes Blau / 1KG   | HFGBL-101    | https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl                        
PLA Glow                | 30.99 EUR | Nachleuchtendes Grün / 1KG   | HFGGR-101    | https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl                        
PLA Glow                | 30.99 EUR | Nachleuchtendes Gelb / 1KG   | HFGYE-103    | https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl                        
PLA Glow                | 30.99 EUR | Blau / 1KG                   | HFGBE-103    | https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl                        
PLA Glow                | 30.99 EUR | Grün / 1KG                   | HFGGN-103    | https://de.anycubic.com/products/pla-glow?_sasdk=faW5mb0BtYmstZ2JyLmRl                        




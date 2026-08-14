# Offline Pokémon TCG Databases — Cross-Reference Reference

## When to use

When you have set + card number from a cert lookup (or from the buy sheet) but need the exact card name. Use these databases to fill the name gap without another API call.

## Primary: Pokémon TCG Data (github.com/PokemonTCG/pokemon-tcg-data)

**Most comprehensive, actively maintained.** 448 commits, last update July 2026.

**Structure:**
```
cards/en/          — one JSON file per card (English)
cards/ja/          — Japanese
sets/              — set definitions (code, name, release date, card count)
decks/en/          — deck lists
```

**Card JSON example** (cards/en/):
```json
{
  "id": "swsh4_001",
  "name": "Pikachu",
  "set": "swsh4",
  "number": "001",
  "rarity": "Rare Holo",
  "hp": 70,
  "types": ["Electric"],
  "attacks": [...],
  "weakness": "Fighting",
  "retreatCost": 1
}
```

**Set code lookup:** sets/en.json maps set codes → names. The Variety field from PSA API (e.g., "PAR En-Paradox Rift") maps to a set code you can look up.

**Usage:**
```python
import json
from pathlib import Path

# Load all cards
cards_dir = Path('cards/en')
cards = {}
for f in cards_dir.glob('*.json'):
    card = json.loads(f.read_text())
    cards[card['id']] = card

# Look up by set code + number
def find_card(set_code, card_number):
    for card in cards.values():
        if card.get('set') == set_code and card.get('number') == card_number:
            return card
    return None
```

**Caveats:**
- Card IDs use set abbreviation + number (e.g., `swsh4_001`) — you need to map the PSA Variety to the set code
- Some promos/special sets may not be in the main cards directory
- Japanese-only sets have separate `cards/ja/` directory

## Secondary: TCGdex (github.com/tcgdex/cards-database)

**Also comprehensive.** API at `tcgdex.dev`. MIT licensed.

**Structure:**
```
cards-en.json      — all English cards
sets-en.json       — all English sets
```

**Card JSON example:**
```json
{
  "id": "swsh4/001",
  "name": "Pikachu",
  "setCode": "swsh4",
  "set": "2020 Sword & Shield Base Set",
  "number": "001",
  "rarity": "Rare Holo",
  ...
}
```

**Usage:** Similar to Pokémon TCG Data. TCGdex uses `setCode/number` format for IDs.

**Advantages over Pokémon TCG Data:**
- Cleaner ID format (`setCode/number`)
- Actively maintained API (tcgdex.dev)
- Multiple languages

## Tertiary: TCGCSV (tcgcsv.com)

**CSV downloads with prices.** Good for price data, but card identity data is secondary.

## Cross-reference workflow

When using PSA API FileAppend response:
```python
# From PSA API FileAppend:
# SetName = "PAR En-Paradox Rift"
# CardNumber = "252"
# Subject = "Gholdengo ex"

# Step 1: Map SetName → set code
# PAR = Paranormal (set code varies by year — check sets/ directory)
# Step 2: Look up card by set code + number in offline DB
# Step 3: Extract card name from DB result
```

**The tricky part:** PSA's Variety/SetName format doesn't directly map to TCG set codes. You need a mapping table (e.g., "PAR En-Paradox Rift" → "par25" or similar). The sets/ directory in Pokémon TCG Data has set names you can fuzzy-match against.

## TCGGO API (tcggo.com/api-docs/v1/)

Alternative API for TCG card data. Less documented than the offline DBs.

## Sources

- `https://github.com/PokemonTCG/pokemon-tcg-data` — primary DB, 448 commits, active
- `https://github.com/tcgdex/cards-database` — secondary DB + API at tcgdex.dev
- `https://tcgcsv.com/` — CSV downloads with prices
- `https://tcggo.com/api-docs/v1/` — TCGGO API

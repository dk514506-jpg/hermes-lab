# Card Hedge API — Endpoint Reference

## Base URL

`https://api.cardhedger.com/`

## Authentication

`X-API-Key` header on every `/v1/*` request. Signup: `ai.cardhedger.com/signup` — 7-day free trial, then paid plans.

## Key Endpoints

### `POST /v1/cards/details-by-certs` (BATCH — this is the one we want)

**Request:**
```json
{
  "certs": ["76676185", "50000000", "12345678"],
  "grader": "PSA"
}
```

**Response:**
```json
{
  "results": [
    {
      "cert_info": {
        "grader": "psa",
        "cert": "76676185",
        "grade": "PSA 9",
        "gemrate_id": "9f4cd2db...",
        "description": "2000 Pokemon Japanese Neo Wooper 194"
      }
    },
    {
      "cert_info": {
        "grader": "psa",
        "cert": "50000000",
        "grade": "PSA 10",
        "gemrate_id": "25783324...",
        "description": "1999 Bowman Chrome C.C. Sabathia 344"
      },
      "card": {
        "card_id": "16996705...",
        "description": "C.C. Sabathia 1999 Bowman Chrome Baseball",
        "player": "C.C. Sabathia",
        "set": "1999 Bowman Chrome Baseball",
        "number": "344",
        "variant": "Base",
        "image": "...",
        "category": "Baseball",
        "category_group": "Sports Cards",
        "set_type": "Bowman Chrome Baseball"
      }
    }
  ],
  "total_requested": 2,
  "total_found": 1
}
```

**Notes:**
- Max 100 certs per request
- Cards not found in Card Hedge have null `card` field
- `description` field often has "Year Brand Set CardName Number" format

### `POST /v1/cards/comps-by-cert`

Get paginated raw sales from a slab certificate. Returns eBay/Fanatics/Heritage/Goldin sales data from 2020-07-01 onward. Pagination: offset + limit ≤ 10000.

### `POST /v1/cards/prices-by-cert`

Price history from a cert number.

### `POST /v1/cards/card-match`

AI matching: send a natural-language description, get the best card match with confidence score.

### `POST /v1/cards/image-match`

Identify a card from a photo.

### `POST /v1/cards/all-prices-by-card`

Current prices at every grade for a card.

## Rate Limits

- Tier-based per-minute and per-day request allowance
- OCR endpoints (prices-by-cert-ocr, details-by-cert-ocr): 2000/day hard cap per API key
- HTTP 429 returns `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`

## Errors

| Code | Meaning |
|------|---------|
| 401 | Missing/invalid API key |
| 403 | Subscription tier can't access operation |
| 404 | Cert/card not found |
| 422 | JSON validation failed |
| 429 | Rate limit |

## Sample: batch lookup for our workflow

```bash
curl -X POST https://api.cardhedger.com/v1/cards/details-by-certs \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "certs": ["100143924", "75716523", "117389921"],
    "grader": "PSA"
  }'
```

## Sources

- `https://api.cardhedger.com/docs` — full API docs
- `https://api.cardhedger.com/openapi.json` — full OpenAPI 3.1 spec
- `https://ai.cardhedger.com/signup` — signup, 7-day trial

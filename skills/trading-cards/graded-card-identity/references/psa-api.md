# PSA Public API — Endpoint Reference

## Base URL

`https://api.psacard.com/publicapi/`

## Authentication

Bearer token from PSA account login at `app.collectors.com`. Header: `Authorization: Bearer <token>`.

**BLOCKER:** Requires PSA account — unavailable without existing credentials.

## Endpoints

### `GET /cert/GetByCertNumber/{certNumber}`

Returns `PublicCertificationModel` → `PublicPSACert`:

| Field | Type | Notes |
|-------|------|-------|
| CertNumber | string | |
| SpecID | int32 | For population endpoint |
| SpecNumber | string | |
| LabelType | string | e.g. "Standard" |
| ReverseBarCode | boolean | |
| Year | string | |
| Brand | string | e.g. "POKEMON" |
| Category | string | e.g. "Trading Card" |
| CardNumber | string | |
| Subject | string | e.g. "Gholdengo" |
| Variety | string | e.g. "En-Paradox Rift" |
| IsPSADNA | boolean | |
| IsDualCert | boolean | |
| GradeDescription | string | e.g. "GEM MT 10" |
| CardGrade | string | e.g. "10" |
| PrimarySigners | string[] | |
| OtherSigners | string[] | |
| AutographGrade | string | |
| TotalPopulation | int32 | |
| TotalPopulationWithQualifier | int32 | |
| PopulationHigher | int32 | |
| T206PopulationAllBacks | int32 | |
| T206PopulationHigherAllBacks | int32 | |
| ItemStatus | string | |

**NOTE:** This endpoint does NOT include SetName. Use FileAppend instead.

### `GET /cert/GetByCertNumberForFileAppend/{certNumber}`

Returns `CertFileAppendModel` → `CertFileAppendPSACert` + `CertFileAppendPSAPopulation`:

| Field | Type | Notes |
|-------|------|-------|
| CertNumber | string | |
| Year | string | |
| Category | string | |
| **SetName** | string | ← THIS is what main endpoint lacks |
| CardNumber | string | |
| Subject | string | |
| Variety | string | |
| Grade | string | e.g. "10" |
| QualifierCode | string | |
| GradeDescription | string | e.g. "GEM MT 10" |
| TotalPopulation | string | |
| PopulationHigher | string | |
| TotalPopulationWithQualifier | string | |
| T206PopulationAllBacks | string | |
| T206PopulationHigherAllBacks | string | |
| IsReverseBarcode | string | |
| CertificationType | int32 | 0=PSA, 1=PSA/DNA |

**USE THIS ENDPOINT.** It gives SetName + population in one call.

### `GET /cert/GetImagesByCertNumber/{certNumber}`

Returns slab image URLs. Only for certs from October 2021 onward (when PSA started scanning).

### `GET /pop/GetPSASpecPopulation/{specID}`

Returns `PSASpecPopulationModel` → grade-by-grade breakdown:

| Field | Type | Notes |
|-------|------|-------|
| SpecID | int32 | |
| Description | string | |
| PSAPop | object | Total, Auth, Grade1-Grade10 (each with Q variants) |
| PSADNAPop | object | Same structure |

Use this for detailed population breakdown when FileAppend's summary numbers aren't enough.

## Rate Limits

~100 calls/day free tier. HTTP 429 when exceeded.

## Sample response (GetByCertNumber)

```json
{
  "PSACert": {
    "CertNumber": "100143924",
    "SpecID": 1234567,
    "LabelType": "Standard",
    "Year": "2023",
    "Brand": "POKEMON",
    "Category": "Trading Card",
    "CardNumber": "252",
    "Subject": "Gholdengo ex",
    "Variety": "PAR En-Paradox Rift",
    "GradeDescription": "GEM MT 10",
    "CardGrade": "10",
    "TotalPopulation": 1288,
    "PopulationHigher": 0
  },
  "IsValidRequest": true,
  "ServerMessage": "Request successful"
}
```

## Error codes

| Code | Meaning |
|------|---------|
| 200 | Successful call (data may still be null) |
| 204 | Empty request (missing cert number) |
| 401/500 | Invalid credentials |
| 429 | Rate limit exceeded |
| `{ "IsValidRequest": false, "ServerMessage": "Invalid CertNo" }` | Bad cert format |
| `{ "IsValidRequest": true, "ServerMessage": "No data found" }` | Cert exists but no data |

## Sources

- `https://www.psacard.com/publicapi/documentation`
- `https://api.psacard.com/publicapi/swagger.json` (full OpenAPI 2.0 spec)

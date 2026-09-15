# ONET-Data-Collector

A small, dependency-light Python toolkit that turns [O*NET Web Services](https://services.onetcenter.org/)
occupational data into tidy, analysis-ready tables.

It is the **data-collection (ETL) half** of a two-repository pipeline. Its
companion, [data-science-onet](https://github.com/Benjamin-V-Chan/data-science-onet),
consumes the tables produced here and runs the analytics (EDA, clustering,
keyword attribution).

---

## What it does

The pipeline has three stages, each usable as a library function or a CLI
subcommand:

| Stage | Input | Output | Function / CLI |
|-------|-------|--------|----------------|
| **1. Keyword search** | search terms | CSV of matching occupations | `keyword_search` / `onet-collect search` |
| **2. Detail fetch** | CSV of occupation codes | raw detail JSON (preserved verbatim) | `fetch_job_details` / `onet-collect details` |
| **3. Condense** | raw detail JSON | flat, wide CSV (one row per occupation) | `condense_job_details` / `onet-collect condense` |

Under the hood everything runs through `OnetClient`, a resilient wrapper around
the O*NET REST API with retries, timeouts, pagination, and typed errors.

---

## Install

```bash
git clone https://github.com/Benjamin-V-Chan/ONET-Data-Collector.git
cd ONET-Data-Collector
python -m venv .venv && source .venv/bin/activate
pip install -e .            # installs the `onet-collect` command
```

The only runtime dependency is `pandas`; the HTTP client is built on the Python
standard library. Development/test extras: `pip install -e ".[dev]"`.

## Credentials

O*NET Web Services requires a free account:
<https://services.onetcenter.org/developer/signup>. Provide credentials in any
of these ways (highest precedence first):

1. Explicit arguments to the functions / `--username` / `--password`.
2. Environment variables `ONET_USERNAME` / `ONET_PASSWORD`.
3. A `.env` file (copy `.env.example` to `.env`).
4. Interactive prompt (CLI only, when run in a terminal).

---

## Quick start

### CLI

```bash
# Run the whole pipeline for a few keywords into ./data
onet-collect pipeline "data scientist" "registered nurse" --out-dir data

# Or run stages individually
onet-collect search "data scientist" "nursing" -o data/raw/keywords.csv
onet-collect details data/raw/keywords.csv     -o data/raw/job_details.json
onet-collect condense data/raw/job_details.json -o data/processed/condensed.csv
```

### Library

```python
from onet_data_collector import (
    keyword_search_many, fetch_job_details, condense_job_details, resolve_credentials,
)

user, pw = resolve_credentials()                       # from env / .env

df = keyword_search_many(user, pw, ["data scientist", "nursing"])
df.to_csv("data/raw/keywords.csv", index=False)

fetch_job_details(user, pw, "data/raw/keywords.csv", "data/raw/job_details.json")
condense_job_details("data/raw/job_details.json", "data/processed/condensed.csv")
```

Need a raw endpoint? Use the client directly:

```python
from onet_data_collector import OnetClient

onet = OnetClient(user, pw)                 # retries + timeouts baked in
about = onet.about()
results = onet.paginate("online/search", ("keyword", "design"), item_key="occupation")
```

---

## Output schema

`condense_job_details` produces one row per occupation with these columns:

`occupation_code`, `occupation_title`, `description`, `bright_outlook`, `green`,
`tasks`, `technology_skills`, `tools_used`, `knowledge`, `skills`, `abilities`,
`work_activities`, `detailed_work_activities`, `work_context`, `job_zone`,
`education`, `interests`, `work_styles`, `work_values`, `related_occupations`,
`additional_information`.

Multi-valued fields are joined with `"; "`. The raw JSON layer from stage 2 is
kept verbatim so the condensed schema can be regenerated or extended later
without re-hitting the API.

---

## Design highlights

- **Resilient client** — exponential backoff with `Retry-After` support on
  network errors, HTTP 429, and 5xx; typed exceptions
  (`OnetAuthError`, `OnetValidationError`, `OnetHTTPError`) instead of magic
  error dicts.
- **Pagination** — `OnetClient.paginate` walks O*NET's `start`/`end`/`total`
  paging so searches return *all* matches, not just the first page.
- **Shape-tolerant flattening** — O*NET fields can be absent, a single object,
  or a list; the condenser normalises all three.
- **Config, not code** — credentials come from env/`.env`/args, never hard-coded.
- **Tested** — the full suite runs offline against a fake HTTP layer
  (`pytest`).

---

## Development

```bash
pip install -e ".[dev]"
pytest            # 29 tests, all offline (no network / credentials needed)
```

## Backwards compatibility

The original import paths and function names still work:
`from onet_data_collector.OnetWebService import OnetWebService`,
`keyword_search`, `fetch_job_details`, `condense_job_details`, and
`check_for_error`. `OnetWebService` is now an alias of `OnetClient`.

## Project role in the larger stack

- **ONET-Data-Collector** (this repo) — ingestion, retrieval, normalization.
- **data-science-onet** — analytics, clustering, keyword attribution.

Together they form a modular pipeline from public labor-market data to
analysis-ready occupational tables.

## License

MIT — see [LICENSE](LICENSE).

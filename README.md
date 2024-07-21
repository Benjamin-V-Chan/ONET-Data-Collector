# onet-data-scraperi

This project uses the O*NET API to fetch and process job-related data. The scripts in this repository allow you to search for job information, fetch detailed job reports, and export data to CSV files.

## Installation

1. Clone this repository.
2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Keyword Search

Run the keyword search script to find jobs related to a specific keyword and save the results to `occupations.csv`:

```bash
python scripts/keyword_search.py
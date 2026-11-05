# Data Quality Analysis Using Python, SQL & Google BigQuery

## Project overview
This beginner portfolio project uses a **synthetic customer dataset** to demonstrate basic data-quality checks, data cleaning with Python/Pandas, and analytical SQL queries intended for Google BigQuery.

The dataset is fictional. It contains intentionally introduced issues such as missing emails, invalid ages, negative income values, inconsistent text formatting, and a duplicate record.

## Project objectives
1. Identify missing, duplicate, invalid, and inconsistent data.
2. Clean records using transparent, documented rules.
3. Produce a clean CSV and a data-quality issue log.
4. Load the cleaned data into BigQuery.
5. Run SQL checks and simple business summaries.

## Folder structure
- `data/customer_data_raw.csv` — synthetic source data
- `data/customer_data_clean.csv` — generated after running the Python script
- `data/data_quality_issues.csv` — generated issue log
- `python/clean_data.py` — cleaning and validation script
- `sql/create_table.sql` — BigQuery table definition
- `sql/analysis_queries.sql` — BigQuery analysis queries

## Step 1: Set up Python
Install Python 3.10+ and run:

```bash
python -m pip install -r requirements.txt
```

## Step 2: Run the cleaning script
From the project root:

```bash
python python/clean_data.py
```

Review the printed row counts and inspect the generated clean CSV and issue log.

## Step 3: Create a BigQuery dataset
1. Sign in to Google Cloud Console.
2. Create or select a Google Cloud project.
3. Enable the BigQuery API if required.
4. Open BigQuery Studio.
5. Replace `YOUR_PROJECT_ID` in `sql/create_table.sql` and `sql/analysis_queries.sql`.
6. Create a dataset named `data_quality` (or run the schema statement).
7. Upload `data/customer_data_clean.csv` to the dataset as a table named `customer_data_clean`.
8. Set `signup_date` to DATE and use the CSV header row.

You may need a billing-enabled Google Cloud project depending on your account and usage. Review current Google Cloud pricing and free-tier terms before enabling paid services. Do not upload real personal or financial data.

## Step 4: Run SQL
Run the queries in `sql/analysis_queries.sql` in BigQuery. Save screenshots of:
- Total clean records
- Duplicate ID check
- Missing value check
- Average income by city
- Customer count by account type

## Data-quality rules used
- Remove exact duplicate rows.
- Keep ages between 18 and 100.
- Exclude negative annual income.
- Exclude missing or invalid email addresses.
- Trim whitespace and standardise city/account-type capitalisation.

These are demonstration rules, not universal business rules. In a real project, agree validation rules with data owners before changing or rejecting records.

## Deliverables
- Raw synthetic dataset
- Cleaned dataset
- Data-quality issue log
- Python cleaning script
- BigQuery table definition
- SQL analysis queries
- Screenshots and a short findings report (to be completed after running the project)

## Resume wording — use only after completing the work
**Data Quality Analysis using Python, SQL and Google BigQuery**
- Analysed a synthetic customer dataset to identify missing, duplicate, invalid and inconsistent records.
- Used Python and Pandas to standardise fields, apply validation rules and generate a data-quality issue log.
- Loaded the cleaned dataset into BigQuery and wrote SQL queries to validate records and summarise data by city and account type.

Do not claim this as professional experience. Clearly present it as an academic or personal project.

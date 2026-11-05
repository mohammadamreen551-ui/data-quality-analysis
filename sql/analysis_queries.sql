-- Run after creating customer_data_clean table in BigQuery.
-- 1. Check row count
SELECT COUNT(*) AS total_clean_records
FROM `YOUR_PROJECT_ID.data_quality.customer_data_clean`;

-- 2. Check for duplicate record IDs
SELECT record_id, COUNT(*) AS occurrences
FROM `YOUR_PROJECT_ID.data_quality.customer_data_clean`
GROUP BY record_id
HAVING COUNT(*) > 1;

-- 3. Check for missing required values
SELECT
  COUNTIF(record_id IS NULL) AS missing_record_ids,
  COUNTIF(email IS NULL OR TRIM(email) = '') AS missing_emails,
  COUNTIF(city IS NULL OR TRIM(city) = '') AS missing_cities
FROM `YOUR_PROJECT_ID.data_quality.customer_data_clean`;

-- 4. Average income by city
SELECT city, ROUND(AVG(annual_income), 2) AS average_annual_income
FROM `YOUR_PROJECT_ID.data_quality.customer_data_clean`
GROUP BY city
ORDER BY average_annual_income DESC;

-- 5. Customer count by account type
SELECT account_type, COUNT(*) AS customer_count
FROM `YOUR_PROJECT_ID.data_quality.customer_data_clean`
GROUP BY account_type
ORDER BY customer_count DESC;

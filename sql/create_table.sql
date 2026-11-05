CREATE SCHEMA IF NOT EXISTS `YOUR_PROJECT_ID.data_quality`;

CREATE OR REPLACE TABLE `YOUR_PROJECT_ID.data_quality.customer_data_clean` (
  record_id STRING,
  customer_name STRING,
  email STRING,
  age INT64,
  city STRING,
  account_type STRING,
  annual_income INT64,
  signup_date DATE
);

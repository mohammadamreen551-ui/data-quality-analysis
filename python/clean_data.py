from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "customer_data_raw.csv"
OUTPUT = ROOT / "data" / "customer_data_clean.csv"
ISSUES = ROOT / "data" / "data_quality_issues.csv"

df = pd.read_csv(INPUT)
original_rows = len(df)

# Standardise text fields
for col in ["customer_name", "email", "city", "account_type"]:
    df[col] = df[col].astype("string").str.strip()

df["city"] = df["city"].str.title()
df["account_type"] = df["account_type"].str.title()
df["email"] = df["email"].str.lower()

# Track records with quality issues before applying cleaning rules
issues = pd.DataFrame({
    "record_id": df["record_id"],
    "missing_email": df["email"].isna(),
    "invalid_age": ~df["age"].between(18, 100),
    "invalid_income": df["annual_income"] < 0,
    "invalid_email_format": df["email"].notna() & ~df["email"].str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", na=False)
})
issues["has_issue"] = issues.drop(columns="record_id").any(axis=1)
issues.to_csv(ISSUES, index=False)

# Apply transparent cleaning rules
df = df.drop_duplicates()
df = df[df["age"].between(18, 100)]
df = df[df["annual_income"] >= 0]
df = df[df["email"].notna()]
df = df[df["email"].str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", na=False)]

df.to_csv(OUTPUT, index=False)

print(f"Raw rows: {original_rows}")
print(f"Clean rows: {len(df)}")
print(f"Rows removed: {original_rows - len(df)}")
print(f"Clean dataset saved to: {OUTPUT}")
print(f"Issue log saved to: {ISSUES}")

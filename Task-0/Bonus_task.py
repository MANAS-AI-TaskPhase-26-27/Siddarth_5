"""
Data cleaning pipeline for ManipalRains.csv
Tailored to the actual issues found in this file (see analysis notes below each step).
"""

import pandas as pd

# 1. Load & parse dates -------------------------------------------------
df = pd.read_csv("ManipalRains.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")  # file uses DD-MM-YYYY

# 2. Drop columns that are almost half-empty -----------------------------
# Sunshine (48%), Evaporation (43%), Cloud9am (38%), Cloud3pm (41%) missing.
# That's too sparse to impute reliably without biasing the result, so they're
# dropped rather than filled. Comment this out if you want to keep + impute them instead.
df = df.drop(columns=["Sunshine", "Evaporation", "Cloud9am", "Cloud3pm"])

# 3. Drop rows missing the label columns ---------------------------------
# RainToday / RainTomorrow are categorical outcomes (~2.2% missing each) —
# not safe to guess, so rows missing either are dropped.
df = df.dropna(subset=["RainToday", "RainTomorrow"])

# 4. Impute remaining missing values --------------------------------------
num_cols = df.select_dtypes(include="number").columns
non_cat = list(num_cols) + ["Date", "RainToday", "RainTomorrow"]
cat_cols = [c for c in df.columns if c not in non_cat]

for col in num_cols:                                    # Pressure9am/3pm, WindGustSpeed, etc.
    df[col] = df[col].fillna(df[col].median())           # median: robust to skew (e.g. Rainfall)

for col in cat_cols:                                     # WindGustDir, WindDir9am, WindDir3pm
    df[col] = df[col].fillna(df[col].mode()[0])

# 5. Duplicates -------------------------------------------------------------
# None found in the original file, but kept as a safety net for re-runs.
df = df.drop_duplicates()

# 6. Categorical text -----------------------------------------------------
# WindGustDir/WindDir9am/WindDir3pm/RainToday/RainTomorrow were already clean
# (consistent casing, no stray whitespace) — no .str.strip()/.lower() needed here.

# 7. Outliers ---------------------------------------------------------------
# Skipped deliberately: values like 371mm rainfall or 135 km/h wind gusts are
# genuine extreme-weather readings in this dataset, not data-entry errors.
# Blind IQR clipping would just delete real storms. If you need it for a
# specific column, use the IQR snippet from the general pipeline.

# 8. Save ---------------------------------------------------------------
df.to_csv("ManipalRains_cleaned.csv", index=False)
print("Final shape:", df.shape)
print("Remaining missing values:", df.isnull().sum().sum())

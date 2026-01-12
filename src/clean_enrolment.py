import pandas as pd

# Load merged data
df = pd.read_csv("enrolment_merged.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y", errors='coerce')

# Create total enrolments column
df['total_enrolments'] = (
    df['age_0_5'] +
    df['age_5_17'] +
    df['age_18_greater']
)

# Basic sanity checks
print("Shape after loading:", df.shape)
print("Null dates:", df['date'].isna().sum())
print("Total enrolments stats:")
print(df['total_enrolments'].describe())

# Save cleaned file
df.to_csv("enrolment_clean.csv", index=False)
print("\nSaved cleaned file: enrolment_clean.csv")

# Show sample
print("\nFirst 5 rows:")
print(df.head())

import pandas as pd
import glob

# Find all enrolment CSV files
files = sorted(glob.glob("api_data_aadhar_enrolment/*.csv"))

print(f"Found {len(files)} enrolment files")

# Load and merge
dfs = []
for f in files:
    print(f"Loading {f}")
    dfs.append(pd.read_csv(f))

df = pd.concat(dfs, ignore_index=True)

print("\nMerged shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# Save merged file
df.to_csv("enrolment_merged.csv", index=False)
print("\nSaved merged file: enrolment_merged.csv")

# Quick sanity check
print("\nFirst 5 rows:")
print(df.head())

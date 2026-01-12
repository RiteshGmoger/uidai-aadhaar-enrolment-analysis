import pandas as pd

# Load clean data
df = pd.read_csv("enrolment_clean.csv")

# Group by state
state_summary = (
    df.groupby("state", as_index=False)
      .agg(
          total_enrolments=("total_enrolments", "sum"),
          records=("total_enrolments", "count")
      )
)

# Sort by total enrolments
state_summary = state_summary.sort_values(
    by="total_enrolments",
    ascending=False
)

# Save result
state_summary.to_csv("state_wise_enrolments.csv", index=False)

# Print top 10 for sanity
print("Top 10 States by Total Enrolments:")
print(state_summary.head(10))

print("\nSaved file: state_wise_enrolments.csv")

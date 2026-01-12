import pandas as pd

# Load state-cleaned data
df = pd.read_csv("enrolment_clean_states.csv")

# Aggregate by district + state
district_summary = (
    df.groupby(['state', 'district'], as_index=False)
      .agg(
          total_enrolments=('total_enrolments', 'sum'),
          records=('total_enrolments', 'count')
      )
)

# Compute z-score style anomaly measure
mean = district_summary['total_enrolments'].mean()
std = district_summary['total_enrolments'].std()

district_summary['anomaly_score'] = (
    (district_summary['total_enrolments'] - mean) / std
)

# Sort by anomaly (high first)
district_summary = district_summary.sort_values(
    by='anomaly_score',
    ascending=False
)

# Save result
district_summary.to_csv("district_anomalies.csv", index=False)

# Print top anomalies
print("TOP 10 DISTRICT ANOMALIES (HIGH ENROLMENTS):")
print(district_summary.head(10))

print("\nSaved file: district_anomalies.csv")

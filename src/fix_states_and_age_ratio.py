import pandas as pd

# Load clean enrolment data
df = pd.read_csv("enrolment_clean.csv")

# Normalize state names
df['state'] = (
    df['state']
    .astype(str)
    .str.strip()
    .str.lower()
)

# Remove invalid states (numeric / junk)
df = df[~df['state'].str.fullmatch(r'\d+')]
df = df[df['state'].str.len() > 3]

# Canonical state mapping
state_map = {
    'orissa': 'odisha',
    'odisa': 'odisha',

    'west bengal': 'west bengal',
    'westbengal': 'west bengal',
    'west bangal': 'west bengal',
    'west  bengal': 'west bengal',

    'andrapradesh': 'andhra pradesh'
}

df['state'] = df['state'].replace(state_map)

# Create age buckets
df['child_enrolments'] = df['age_0_5'] + df['age_5_17']
df['adult_enrolments'] = df['age_18_greater']

# Aggregate by state
state_age = (
    df.groupby('state', as_index=False)
      .agg(
          total_child=('child_enrolments', 'sum'),
          total_adult=('adult_enrolments', 'sum')
      )
)

# Remove divide-by-zero cases
state_age = state_age[state_age['total_child'] > 0]

# Compute ratio
state_age['adult_child_ratio'] = (
    state_age['total_adult'] / state_age['total_child']
)

# Sort
state_age = state_age.sort_values(
    by='adult_child_ratio',
    ascending=False
)

# Save outputs
state_age.to_csv("state_age_ratio_clean.csv", index=False)
df.to_csv("enrolment_clean_states.csv", index=False)

# Print sanity output
print("TOTAL STATES:", state_age.shape[0])
print("\nTOP 5 ADULT-HEAVY STATES:")
print(state_age.head(5))

print("\nTOP 5 CHILD-HEAVY STATES:")
print(state_age.tail(5))

import pandas as pd

# Load, add sub-labels, set sub as index
tsv = pd.read_csv("participants.tsv", sep="\t")
tsv.dropna(how="all", inplace=True)
tsv['participant_id'] = "sub-" + tsv['participant_id'].apply(
    int).apply(str).str.zfill(3)
tsv.set_index('participant_id', inplace=True)

# Meq to Chronotype
tsv.loc[tsv["chronotype"].between(16,41), "chronotype"] = 2 # Evening
tsv.loc[tsv["chronotype"].between(42,58), "chronotype"] = 3 # Intermediate
tsv.loc[tsv["chronotype"].between(59,86), "chronotype"] = 1 # Morning

# Factorise handedness
tsv.loc[tsv["handedness"] > 0, "handedness"] = 1 # Right
tsv.loc[tsv["handedness"] < 0, "handedness"] = 2 # Left
tsv.loc[tsv["handedness"] == 0, "handedness"] = 3 # Ambidextrous
tsv["handedness"] = tsv["handedness"].astype(str)

tsv.loc[tsv["handedness"].apply(str) == "1.0", "handedness"] = "R" # Right
tsv.loc[tsv["handedness"] == "2.0", "handedness"] = "L" # Right
tsv.loc[tsv["handedness"] == "3.0", "handedness"] = "A" # Right

# Save
tsv.to_csv("participants.tsv", sep="\t")

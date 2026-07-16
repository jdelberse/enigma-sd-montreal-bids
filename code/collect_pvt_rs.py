## Author : JD Elberse
## This script collects PVT mean reaction speed times and 
## updates the participants.tsv

import os
import pandas as pd

# Parameters
root = os.getcwd()
participants = pd.read_csv(f"{root}/participants.tsv", sep = "\t")
subs = participants.participant_id
rs_data = pd.read_excel(f"{root}/sourcedata/participants_MontrealConcordia_update2026_RS.xlsx", header = 1)

# Loop over subjects
for sub in subs:
    dicom_sub = "SDEP" + sub.split("-")[1]
    print(f"{sub} / {dicom_sub}")
    
    mask = rs_data.Subject == dicom_sub
    baseline = rs_data[mask].PVT_reaction_speed_baseline.item()
    followup = rs_data[mask].PVT_reaction_speed_sleep_deprivation.item()
    print(f"Baseline mean RS: {baseline}")
    print(f"Follow-up mean RS: {followup}")

    mask = participants.participant_id == sub
    participants[mask].pvt_meanrs_baseline = baseline
    participants[mask].pvt_meanrs_sd = followup

participants.to_csv(f"{root}/participants.tsv", sep = "\t")
print("Saved to participants.tsv")


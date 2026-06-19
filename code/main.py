import json
import pandas as pd

from csv_processor import load_sample_claims
from image_analyzer import analyze_image
from history_checker import get_risk_flags
from claim_parser import extract_claim
from decision_engine import build_decision

claims_df = load_sample_claims()

row = claims_df.iloc[1]

images = row["image_paths"].split(";")

print(images)
result = analyze_image(
    "dataset/" + images[1],
    row["user_claim"],
    row["claim_object"]
)

data = json.loads(
    result.replace("```json", "")
          .replace("```", "")
          .strip()
)

history_df = pd.read_csv("dataset/user_history.csv")

history_row = history_df[
    history_df["user_id"] == row["user_id"]
].iloc[0]

risk_flags = get_risk_flags(history_row)
claimed_issue = extract_claim(row["user_claim"])
decision = build_decision(
    data,
    risk_flags,
    claimed_issue
)
print(decision)
import json
import time
import pandas as pd

from csv_processor import load_claims
from image_analyzer import analyze_image
from history_checker import get_risk_flags
from claim_parser import extract_claim
from decision_engine import build_decision

# Final submission dataset
claims_df = load_claims()

history_df = pd.read_csv("dataset/user_history.csv")

all_results = []

for index, row in claims_df.iterrows():
    print(f"\nProcessing Claim {index + 1}")

    images = row["image_paths"].split(";")

    result = analyze_image(
        "dataset/" + images[0],
        row["user_claim"],
        row["claim_object"]
    )

    data = json.loads(
        result.replace("```json", "")
              .replace("```", "")
              .strip()
    )

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

    final_row = {
    "user_id": row["user_id"],
    "image_paths": row["image_paths"],
    "user_claim": row["user_claim"],
    "claim_object": row["claim_object"],

    "evidence_standard_met": decision["evidence_standard_met"],
    "evidence_standard_met_reason": decision["evidence_standard_met_reason"],
    "risk_flags": decision["risk_flags"],
    "issue_type": decision["issue_type"],
    "object_part": decision["object_part"],
    "claim_status": decision["claim_status"],
    "claim_status_justification": decision["claim_status_justification"],

    "supporting_image_ids": "none",
    "valid_image": True,

    "severity": decision["severity"]
}

    all_results.append(final_row)

    print(final_row)

    # Gemini free tier protection
    time.sleep(15)

print("\nTotal Results:", len(all_results))

output_df = pd.DataFrame(
    all_results,
    columns=[
        "user_id",
        "image_paths",
        "user_claim",
        "claim_object",
        "evidence_standard_met",
        "evidence_standard_met_reason",
        "risk_flags",
        "issue_type",
        "object_part",
        "claim_status",
        "claim_status_justification",
        "supporting_image_ids",
        "valid_image",
        "severity"
    ]
)

output_df.to_csv(
    "output.csv",
    index=False
)

print("output.csv generated")
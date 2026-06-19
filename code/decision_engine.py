def build_decision(
    row,
    image_result,
    risk_flags,
    claimed_issue
):
    return {
        "user_id": row["user_id"],
        "image_paths": row["image_paths"],
        "user_claim": row["user_claim"],
        "claim_object": row["claim_object"],

        "evidence_standard_met": True,
        "evidence_standard_met_reason": "Visible evidence available",

        "risk_flags": risk_flags,

        "issue_type": image_result["issue_type"],
        "object_part": image_result["object_part"],

        "claim_status": image_result["claim_status"],

        "claim_status_justification": image_result["reason"],

        "supporting_image_ids": "none",

        "valid_image": True,

        "severity": image_result["severity"]
    }
def build_decision(image_result, risk_flags, claimed_issue):
    return {
        "evidence_standard_met": True,
        "evidence_standard_met_reason": "Visible evidence available",
        "risk_flags": risk_flags,
        "issue_type": image_result["issue_type"],
        "object_part": image_result["object_part"],
        "claim_status": image_result["claim_status"],
        "claim_status_justification": image_result["reason"],
        "severity": image_result["severity"]
    }
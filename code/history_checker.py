def get_risk_flags(user_history_row):
    flags = str(user_history_row["history_flags"]).strip()

    if flags.lower() == "none":
        return "none"

    return flags
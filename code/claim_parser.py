def extract_claim(user_claim):
    claim = user_claim.lower()

    if "dent" in claim:
        return "dent"

    if "scratch" in claim:
        return "scratch"

    if "crack" in claim:
        return "crack"

    if "broken" in claim:
        return "broken_part"

    if "missing" in claim:
        return "missing_part"

    if "water" in claim:
        return "water_damage"

    return "unknown"
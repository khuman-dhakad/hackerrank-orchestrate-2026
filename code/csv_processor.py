import pandas as pd


def load_sample_claims():
    return pd.read_csv("dataset/sample_claims.csv")


def load_claims():
    return pd.read_csv("dataset/claims.csv")


def load_user_history():
    return pd.read_csv("dataset/user_history.csv")


def load_evidence_requirements():
    return pd.read_csv("dataset/evidence_requirements.csv")
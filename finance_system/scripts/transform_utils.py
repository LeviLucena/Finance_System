import pandas as pd

def parse_dates(df: pd.DataFrame, date_columns: list[str]) -> pd.DataFrame:
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

def normalize_text(df: pd.DataFrame, text_columns: list[str]) -> pd.DataFrame:
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df

def clean_numeric(df: pd.DataFrame, numeric_columns: list[str]) -> pd.DataFrame:
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def clean_dataframe(df: pd.DataFrame, date_cols=None, text_cols=None, numeric_cols=None) -> pd.DataFrame:
    if date_cols:
        df = parse_dates(df, date_cols)
    if text_cols:
        df = normalize_text(df, text_cols)
    if numeric_cols:
        df = clean_numeric(df, numeric_cols)
    df = drop_duplicates(df)
    return df

# app/data_analysis/data_cleaning.py

import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data, columns=['team_a', 'team_b', 'score_a', 'score_b', 'date'])
    df['date'] = pd.to_datetime(df['date'])
    df['score_a'] = pd.to_numeric(df['score_a'])
    df['score_b'] = pd.to_numeric(df['score_b'])
    df.dropna(inplace=True)
    return df

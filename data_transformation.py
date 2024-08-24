# data_transformation.py

import pandas as pd

def clean_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df.dropna(inplace=True)
    return df

def analyze_data(df):
    avg_scores = df[['score_a', 'score_b']].mean()
    win_loss_ratio = df.apply(lambda row: 'team_a' if row['score_a'] > row['score_b'] else 'team_b', axis=1).value_counts(normalize=True)
    return avg_scores, win_loss_ratio

df = get_data()
df_clean = clean_data(df)
avg_scores, win_loss_ratio = analyze_data(df_clean)
print("Average Scores:", avg_scores)
print("Win/Loss Ratio:", win_loss_ratio)

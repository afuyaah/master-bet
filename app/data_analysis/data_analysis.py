# app/data_analysis/data_analysis.py

import pandas as pd

def analyze_data(df):
    # Example: Calculate average scores
    avg_scores = df[['score_a', 'score_b']].mean()
    
    # Example: Win-loss ratio
    df['result'] = df.apply(lambda row: 'team_a' if row['score_a'] > row['score_b'] else 'team_b', axis=1)
    win_loss_ratio = df['result'].value_counts(normalize=True)
    
    return avg_scores, win_loss_ratio

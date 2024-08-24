# app/data_analysis/ml_model.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(df):
    # Feature engineering
    df['team_strength'] = df.groupby('team_a')['score_a'].transform('mean')
    X = df[['score_a', 'score_b', 'team_strength']]
    y = df['result'].apply(lambda x: 1 if x == 'team_a' else 0)  # Convert result to binary

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

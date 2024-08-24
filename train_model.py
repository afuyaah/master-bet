# train_model.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib  # For saving and loading models

def train_model(df):
    df['result'] = df.apply(lambda row: 1 if row['score_a'] > row['score_b'] else 0, axis=1)
    X = df[['score_a', 'score_b']]
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Save the model to a file
    joblib.dump(model, 'model.pkl')
    
    return model, accuracy

# Load the model for predictions
def load_model():
    return joblib.load('model.pkl')

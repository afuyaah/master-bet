# train_model.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def train_model(df):
    df['result'] = df.apply(lambda row: 1 if row['score_a'] > row['score_b'] else 0, axis=1)
    X = df[['score_a', 'score_b']]
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

df = get_data()
df_clean = clean_data(df)
model, accuracy = train_model(df_clean)
print("Model Accuracy:", accuracy)

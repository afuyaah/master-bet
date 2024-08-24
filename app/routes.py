# app/routes.py

from flask import Blueprint, request, jsonify
from data_transformation import get_data, clean_data, analyze_data
from train_model import load_model

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze', methods=['GET'])
def analyze():
    df = get_data()
    df_clean = clean_data(df)
    avg_scores, win_loss_ratio = analyze_data(df_clean)
    return jsonify({"average_scores": avg_scores.to_dict(), "win_loss_ratio": win_loss_ratio.to_dict()})

# app/routes.py


analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/predict', methods=['POST'])
def predict():
    """
    Predicts the outcome of a football match based on input scores using the trained model.

    Returns:
        json: A JSON object containing the predicted result.
    """
    # Load the trained model
    model = load_model()
    
    # Get data from the request
    input_data = request.json
    score_a = input_data.get('score_a')
    score_b = input_data.get('score_b')
    
    # Prepare features for prediction
    features = [[score_a, score_b]]
    
    # Make prediction using the model
    prediction = model.predict(features)
    
    # Convert prediction to a readable format
    result = 'team_a' if prediction[0] == 1 else 'team_b'
    
    return jsonify({"prediction": result})

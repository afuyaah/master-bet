# app/data_analysis/data_retrieval.py

from app.extensions import db

def get_scraped_data():
    query = """
        SELECT team_a, team_b, score_a, score_b, date
        FROM sports_data
    """
    data = db.session.execute(query).fetchall()
    return data

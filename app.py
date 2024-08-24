from app import create_app, db
from flask_migrate import Migrate
import os

# Create the Flask app and initialize Flask-Migrate
app = create_app()
migrate = Migrate(app, db)

# Initialize the database (if needed)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)

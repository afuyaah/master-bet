from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime, timedelta, date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    auth_code_hash = db.Column(db.String(128))  # New field for hashed auth code

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_auth_code(self, auth_code):
        self.auth_code_hash = generate_password_hash(auth_code)

    def check_auth_code(self, auth_code):
        return check_password_hash(self.auth_code_hash, auth_code)


class ScrapedURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ScrapedURL {self.url}>'





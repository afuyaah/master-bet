from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.main.forms import LoginForm, AuthenticationForm
from app.main.models import User

auth_bp = Blueprint('auth', __name__)

# Assuming email is a constant
USER_EMAIL = "10443"
USER_PASSWORD = "12x"
EXPECTED_AUTH_CODE = "1044314"

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == USER_PASSWORD:
            # Password is correct, redirect to authentication page
            return redirect(url_for('auth.authenticate'))
        else:
            flash('Invalid password', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    form = AuthenticationForm()
    if form.validate_on_submit():
        # Check if the authentication code is correct
        user = User.query.filter_by(email=USER_EMAIL).first()
        if user and user.check_auth_code(form.auth_code.data):
            # Log the user in and redirect to the desired page
            login_user(user)
            return redirect(url_for('main.matches'))
        else:
            flash('Invalid authentication code', 'danger')
    return render_template('auth/authenticate.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

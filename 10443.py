from app import create_app, db
from app.main.models import User

app = create_app()

with app.app_context():
    # Create a new user with the specified email and password
    new_user = User(email='10443')
    new_user.set_password('12x')  # Set the hashed password
    
    # Set the authentication code for the new user
    new_user.set_auth_code('1044314')  # Set the hashed authentication code
    
    # Add the new user to the session and commit to the database
    db.session.add(new_user)
    db.session.commit()
    
    print('User created and authentication code set successfully!')


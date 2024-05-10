from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from .models import User
from .utils.database import db

class AuthenticationService:
    @staticmethod
    def generate_token(user_id, expiration=3600):
        """Generate authentication token."""
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': user_id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        """Verify authentication token."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            user = User.query.get(data['id'])
            return user
        except (BadSignature, SignatureExpired):
            return None

    @staticmethod
    def register_user(username, password):
        """Register a new user."""
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return None, "Username already exists"
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user, "User registered successfully"

    @staticmethod
    def login_user(username, password):
        """Authenticate user and return token."""
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None, "Invalid username or password"
        
        token = AuthenticationService.generate_token(user.id)
        return token, "Login successful"

    @staticmethod
    def change_password(user_id, old_password, new_password):
        """Change user's password."""
        user = User.query.get(user_id)
        if not user or not check_password_hash(user.password, old_password):
            return False, "Invalid user or password"
        
        user.password = generate_password_hash(new_password)
        db.session.commit()
        return True, "Password changed successfully"

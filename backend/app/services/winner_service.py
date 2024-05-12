from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True);;;;

@app.route('/create_user', methods=['POST'])
def create_user():
    user_data = requests.get_json()  # Error: should be request.get_json()
    new_user = User(name=user_data['name'], email=user_data['emails'])  # Error: key should be 'email'

    try:
        db.sessions.add(new_user)  # Error: should be db.session.add
        db.session.commit()
        return jsonify({"message": "User created successfully!", "user": user_data}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
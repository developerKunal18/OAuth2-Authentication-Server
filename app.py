from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# ---------- Config ----------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

db = SQLAlchemy(app)
jwt = JWTManager(app)

# ---------- Model ----------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

with app.app_context():
    db.create_all()

# ---------- Register ----------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    user = User(
        username=data["username"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered"
    })

# ---------- Login ----------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()

    if not user:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

    token = create_access_token(
        identity=user.username
    )

    return jsonify({
        "access_token": token
    })

# ---------- Protected API ----------
@app.route("/profile")
@jwt_required()
def profile():

    username = get_jwt_identity()

    return jsonify({
        "user": username,
        "message": "Authenticated"
    })

# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "UP"
    })

if __name__ == "__main__":
    app.run(debug=True)

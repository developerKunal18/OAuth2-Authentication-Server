🧠 Why This Is Important

Instead of every application managing passwords directly:
Client
   ↓
Username + Password
   ↓
Application

OAuth2 introduces an authorization server:
Client
   ↓
OAuth2 Server
   ↓
Access Token
   ↓
Protected API

Benefits:
✅ Secure authentication
✅ Token-based authorization
✅ Third-party login support
✅ Reduced password sharing

Used By
Google Sign-In
GitHub OAuth
Microsoft Azure AD
Auth0
Okta

🛠 Tech Stack
Python
Flask
Flask-JWT-Extended
SQLite
SQLAlchemy

📂 Project Structure
oauth2-auth-server/
│
├── app.py
├── requirements.txt
├── users.db
└── README.md

📄 requirements.txt
flask
flask-sqlalchemy
flask-jwt-extended

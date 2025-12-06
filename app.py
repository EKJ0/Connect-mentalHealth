import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.account_routes import account_bp
from routes.chat_routes import chat_bp
from routes.mood_routes import mood_bp
from routes.journal_routes import journal_bp
from routes.settings_routes import settings_bp

load_dotenv()

# Validate required environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set. Please add it to your .env file.")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set. Please add it to your .env file.")

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

# Make mongo and bcrypt available in other files
app.mongo = mongo
app.bcrypt = bcrypt

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(account_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(mood_bp)
app.register_blueprint(journal_bp)
app.register_blueprint(settings_bp)

def initialize_database():
    """Initialize database with default data if collections don't exist."""
    db = mongo.db

    # USERS COLLECTION (creates default admin)
    if "users" not in db.list_collection_names():
        db.users.insert_one({
            "username": "admin",
            "password": bcrypt.generate_password_hash("Admin123!").decode("utf-8"),
            "name": "Administrator",
            "bio": ""
        })
        print("👤 Default admin user created! (username: admin, password: Admin123!)")

    # SETTINGS COLLECTION (default settings)
    if "settings" not in db.list_collection_names():
        db.settings.insert_one({
            "username": "admin",
            "theme": "light",
            "notifications": True
        })
        print("⚙️ Default settings added!")

    # MOODS COLLECTION (sample mood entry)
    if "moods" not in db.list_collection_names():
        db.moods.insert_one({
            "username": "admin",
            "mood": "happy",
            "date": "2025-01-01"
        })
        print("😊 Sample mood entry created!")

    # JOURNAL COLLECTION (sample journal entry)
    if "journal" not in db.list_collection_names():
        db.journal.insert_one({
            "username": "admin",
            "title": "Welcome Journal",
            "content": "This is your first journal entry!",
            "date": "2025-01-01"
        })
        print("📘 Initial journal entry added!")

    # CHAT / MESSAGES COLLECTION (demo message)
    if "messages" not in db.list_collection_names():
        db.messages.insert_one({
            "from": "admin",
            "to": "admin",
            "content": "Hello! This is the first message.",
            "timestamp": "2025-01-01T00:00:00"
        })
        print("💬 Initial message created!")

    print("✨ ALL collections initialized successfully!")

if __name__ == "__main__":
    with app.app_context():
        initialize_database()
    app.run(debug=True)
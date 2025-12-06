from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.account_routes import account_bp
from routes.chat_routes import chat_bp
from routes.mood_routes import mood_bp
from routes.journal_routes import journal_bp
from routes.settings_routes import settings_bp

app = Flask(__name__)
app.secret_key = "thisissecret"

app.config["MONGO_URI"] = "mongodb+srv://emmakrj02_db:yvzZ5x8mSufmQWE2@connect-mind.rzqugrq.mongodb.net/mindconnect?retryWrites=true&w=majority"

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

if __name__ == "__main__":
    app.run(debug=True)

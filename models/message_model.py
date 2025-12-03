# models/message_model.py
from flask import current_app
from datetime import datetime

def create_message(username: str, message_text: str):
    """
    Insert a new chat message.
    """
    mongo = current_app.mongo
    return mongo.db.messages.insert_one({
        "user": username,
        "message": message_text,
        "timestamp": datetime.now()
    })


def get_recent_messages(limit: int = 50):
    """
    Get most recent chat messages, newest first.
    """
    mongo = current_app.mongo
    return mongo.db.messages.find().sort("timestamp", -1).limit(limit)

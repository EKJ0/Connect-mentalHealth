# models/mood_model.py
from flask import current_app
from datetime import datetime

def save_mood(username: str, mood: str):
    """
    Save today's mood for the given user.
    """
    mongo = current_app.mongo
    return mongo.db.moods.insert_one({
        "user": username,
        "mood": mood,
        "timestamp": datetime.now()
    })


def get_moods_for_user(username: str, limit: int | None = None):
    """
    Get mood history for a user, newest first.
    """
    mongo = current_app.mongo
    cursor = mongo.db.moods.find({"user": username}).sort("timestamp", -1)
    if limit:
        cursor = cursor.limit(limit)
    return cursor

# models/settings_model.py
from flask import current_app

def get_settings_for_user(username: str):
    """
    Fetch settings document for a specific user.
    """
    mongo = current_app.mongo
    return mongo.db.settings.find_one({"user": username})


def save_settings_for_user(username: str, dark_mode: bool, notifications: bool):
    """
    Upsert (update or insert) settings for a user.
    """
    mongo = current_app.mongo
    return mongo.db.settings.update_one(
        {"user": username},
        {
            "$set": {
                "dark_mode": dark_mode,
                "notifications": notifications
            }
        },
        upsert=True
    )

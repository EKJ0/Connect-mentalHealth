# models/journal_model.py
from flask import current_app
from bson.objectid import ObjectId
from datetime import datetime

def create_entry(username: str, title: str, content: str):
    """
    Create a new journal entry.
    """
    mongo = current_app.mongo
    return mongo.db.journals.insert_one({
        "user": username,
        "title": title,
        "content": content,
        "date": datetime.now()
    })


def get_entries_for_user(username: str):
    """
    Get all journal entries for a user, newest first.
    """
    mongo = current_app.mongo
    return mongo.db.journals.find({"user": username}).sort("date", -1)


def delete_entry(entry_id: str):
    """
    Delete a journal entry by its ID.
    """
    mongo = current_app.mongo
    return mongo.db.journals.delete_one({"_id": ObjectId(entry_id)})


def update_entry(entry_id: str, title: str, content: str):
    """
    Update title and content of a journal entry.
    """
    mongo = current_app.mongo
    return mongo.db.journals.update_one(
        {"_id": ObjectId(entry_id)},
        {"$set": {"title": title, "content": content}}
    )

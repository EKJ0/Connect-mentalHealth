# models/user_model.py
from bson.objectid import ObjectId

def create_user(mongo, name: str, email: str, password_hash: str):
    return mongo.db.users.insert_one({
        "name": name,
        "email": email,
        "password": password_hash,
        "bio": ""
    }).inserted_id


def find_user_by_email(mongo, email: str):
    return mongo.db.users.find_one({"email": email})


def find_user_by_id(mongo, user_id: str):
    return mongo.db.users.find_one({"_id": ObjectId(user_id)})


def update_user_profile(mongo, user_id: str, name: str, bio: str):
    return mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"name": name, "bio": bio}}
    )


def delete_user(mongo, user_id: str):
    return mongo.db.users.delete_one({"_id": ObjectId(user_id)})

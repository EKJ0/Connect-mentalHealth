from flask import Blueprint, render_template, request, session, redirect, current_app
from datetime import datetime

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat_page():
    if "user_id" not in session:
        return redirect("/")

    mongo = current_app.mongo
    messages = mongo.db.messages.find().sort("timestamp", -1)

    return render_template("chat.html", messages=messages)

@chat_bp.route("/chat/send", methods=["POST"])
def send_message():
    mongo = current_app.mongo

    mongo.db.messages.insert_one({
        "user": session["username"],
        "message": request.form["message"],
        "timestamp": datetime.now()
    })

    return redirect("/chat")

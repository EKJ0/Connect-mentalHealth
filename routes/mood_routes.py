from flask import Blueprint, render_template, request, session, redirect, current_app

mood_bp = Blueprint("mood", __name__)

@mood_bp.route("/mood")
def mood_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("mood.html")

@mood_bp.route("/mood", methods=["POST"])
def save_mood():
    if "user_id" not in session:
        return redirect("/")

    mood = request.form.get("mood")
    mongo = current_app.mongo

    mongo.db.moods.insert_one({
        "user_id": session["user_id"],
        "mood": mood
    })

    return redirect("/dashboard")

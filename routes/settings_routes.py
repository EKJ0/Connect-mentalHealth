from flask import Blueprint, render_template, request, session, redirect, current_app

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
def settings_page():
    mongo = current_app.mongo
    settings = mongo.db.settings.find_one({"user": session["username"]})
    return render_template("settings.html", settings=settings)

@settings_bp.route("/settings/save", methods=["POST"])
def save_settings():
    mongo = current_app.mongo

    mongo.db.settings.update_one(
        {"user": session["username"]},
        {"$set": {
            "dark_mode": "dark" in request.form,
            "notifications": "notify" in request.form
        }},
        upsert=True
    )

    return redirect("/settings")

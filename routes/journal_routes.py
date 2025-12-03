from flask import Blueprint, render_template, request, session, redirect, current_app

journal_bp = Blueprint("journal", __name__)

@journal_bp.route("/journal")
def journal_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("journal.html")

@journal_bp.route("/journal", methods=["POST"])
def save_journal():
    if "user_id" not in session:
        return redirect("/")

    entry = request.form.get("entry")
    mongo = current_app.mongo

    mongo.db.journals.insert_one({
        "user_id": session["user_id"],
        "entry": entry
    })

    return redirect("/dashboard")

# routes/account_routes.py
from flask import Blueprint, render_template, request, redirect, session, current_app
from models.user_model import find_user_by_id, update_user_profile, delete_user

account_bp = Blueprint("account", __name__)

@account_bp.route("/account")
def account_page():
    if "user_id" not in session:
        return redirect("/")

    mongo = current_app.mongo
    user = find_user_by_id(mongo, session["user_id"])

    return render_template("account.html", user=user)

@account_bp.route("/account/update", methods=["POST"])
def account_update():
    mongo = current_app.mongo

    name = request.form.get("name")
    bio = request.form.get("bio")

    update_user_profile(mongo, session["user_id"], name, bio)
    return redirect("/account")

@account_bp.route("/account/delete", methods=["POST"])
def account_delete():
    mongo = current_app.mongo
    delete_user(mongo, session["user_id"])

    session.clear()
    return redirect("/")

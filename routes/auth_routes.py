from flask import Blueprint, render_template, request, redirect, session, current_app

auth_bp = Blueprint("auth", __name__)


# ----------------------
# LOGIN PAGE (GET)
# ----------------------
@auth_bp.route("/")
def login_page():
    return render_template("login.html", error=None)


# ----------------------
# LOGIN POST
# ----------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "")

    mongo = current_app.mongo
    bcrypt = current_app.bcrypt

    # Find user
    user = mongo.db.users.find_one({"username": username})

    # Invalid username OR password
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return render_template("login.html", error="Invalid username or password")

    # Login OK
    session["user_id"] = str(user["_id"])
    session["username"] = user["username"]

    return redirect("/dashboard")


# ----------------------
# SIGNUP PAGE (GET)
# ----------------------
@auth_bp.route("/signup")
def signup_page():
    return render_template("signup.html", error=None)


# ----------------------
# SIGNUP POST
# ----------------------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "")

    # Validate empty fields
    if username == "" or password == "":
        return render_template("signup.html", error="All fields are required")

    mongo = current_app.mongo
    bcrypt = current_app.bcrypt

    # Check if username exists
    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return render_template("signup.html", error="Username already exists")

    # Hash password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # Insert new user
    mongo.db.users.insert_one({
        "username": username,
        "password": hashed_password,
        "name": "",
        "bio": ""
    })

    # Redirect to login page after success
    return redirect("/")

#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def Welcome():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    email = request.form.get('email')
    pwd = request.form.get('password')

    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """
    Handle POST /sessions route.

    Retrieves the email and password from the request form data and
    verifies the user's credentials. If the credentials are invalid,
    aborts the request with a 401 status code.

    If the credentials are valid, creates a new session for the user,
    sets the session ID in a cookie named "session_id", and returns
    a JSON response containing the user's email and a confirmation
    message.
    """
    # Récupération email et password
    email = request.form.get('email')
    pwd = request.form.get('password')

    # Vérification que les informations de login sont correctes
    if not AUTH.valid_login(email, pwd):
        abort(401)

    # Création d'une session pour l'user
    session_id = AUTH.create_session(email)
    # Ajout du cookie
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """
    Logs out the current user.

    Retrieves the session_id from the request cookies, finds the
    corresponding user and destroys the session. If the user exists,
    redirects to the home page. Otherwise, aborts with a 403 status code.
    """
    # Récupération de la session_id
    user_session_id = request.cookies.get("session_id")
    # Récupération de l'user grâce à la session_id
    user = AUTH.get_user_from_session_id(user_session_id)
    # Si l'user n'existe pas
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """
    Retrieve the profile of the logged-in user based on the session_id cookie.

    If the session_id corresponds to a valid user, returns the user's email
    with a 200 HTTP status code.
    Otherwise, returns a 403 error.
    """
    # Récupération de la session_id
    user_session_id = request.cookies.get("session_id")
    # Récupération de l'user grâce à la session_id
    user = AUTH.get_user_from_session_id(user_session_id)
    # Si l'user n'existe pas
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

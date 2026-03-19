#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

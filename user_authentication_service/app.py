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
    """
    Handle POST /users to register a new user.

    Expects "email" and "password" in form data. Returns a JSON response
    with the email and a success message if the user is created.
    If the email is already registered, returns an error message with
    status code 400.
    """
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


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """
    Endpoint to generate a password reset token for a user based on the
    email retrieved form data.

    If the email is registered, returns the user's email and reset_token with
    a 200 HTTP status code.
    Otherwise, returns a 403 error.

    Returns:
        JSON response with the email and reset token on success.
        Aborts with 403 if the email is not registered.
    """
    # Récupération email
    email = request.form.get('email')
    try:
        # Génération d'un reset_token.
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """
    Handle PUT /reset_password requests.

    Retrieve the email, reset token, and new password from the request
    form data. Attempt to update the user's password using the provided
    reset token.

    If the token is invalid, respond with a 403 HTTP status code.
    If the password is successfully updated, respond with a JSON payload
    containing the user's email and a confirmation message.
    """
    # Récupération email, reset_token et new_password
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        # Modification du MdP
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

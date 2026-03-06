#!/usr/bin/env python3
"""
Module of Session_auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_authentification():
    """
    Authenticate a user using email and password.

    Retrieves the email and password from the POST form data.
    If the credentials are valid, creates a session for the user and
    returns the user information in JSON format while setting the
    session ID in a cookie.

    Returns:
        JSON response containing the user data and a session cookie
        if authentication succeeds.

    Errors:
        400: If email or password is missing.
        404: If no user is found with the provided email.
        401: If the password is incorrect.
    """
    # Récupération de l'email & pwd
    user_email = request.form.get("email")
    user_pwd = request.form.get("password")

    # Vérification est-ce que les variables ont des valeurs correctes
    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400

    # Récupération des users grâce à l'email
    user_list = User.search({'email': user_email})
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    # Récupération de l'user
    user = user_list[0]
    # Vérification du pwd associé à l'user
    if not user.is_valid_password(user_pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    # Création de la session_id
    session_id = auth.create_session(user.id)  # Créé la Session_id
    response = jsonify(user.to_json())  # Créé le JSON avec les data de l'user
    session_name = os.getenv("SESSION_NAME")  # Récupération de la session_name
    response.set_cookie(session_name, session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete():
    """
    Logs out the user by deleting their session.

    This route handles DELETE requests to '/api/v1/auth_session/logout'.
    It uses the SessionAuth instance `auth` to destroy the session associated
    with the request's cookie.

    Steps:
        1. Retrieve the session from the request cookie using
        `auth.destroy_session(request)`.
        2. If no valid session is found or the session cannot be deleted,
        abort with a 404 error.
        3. If the session is successfully deleted, return an empty JSON
        dictionary with status code 200.

    Returns:
        JSON response: An empty JSON dictionary {} with HTTP 200 if successful.
        Aborts with HTTP 404 if no session is found or deletion fails.
    """
    from api.v1.app import auth
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)
    return jsonify({}), 200

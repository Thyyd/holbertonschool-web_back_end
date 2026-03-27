#!/usr/bin/env python3
"""
App Module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Config class that configures the Languages
    """
    LANGUAGES = ["en", "fr"]
    # Langue et fuseau horaire utilisés par défaut
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Création de l'application Flask
app = Flask(__name__)

# Utilisation de la classe par l'application
app.config.from_object(Config)

# Création de l'objet Babel relié à l'application Flask
babel = Babel()

# Création de la table users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Function that determines the logged user among the users in the table.

    If the login_as is stated in the URL, and is among the users table, then
    it will return the datas of the user.
    Else, it will return None.
    """
    # Récupération de login_as
    user_id = request.args.get("login_as")
    # Vérification si le string est un ou plusieurs chiffres
    if user_id and user_id.isdigit():
        # Conversion du string en entier
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]

    return None


def get_locale() -> str:
    """
    Function that determines the best match among the supported languages.

    If the locale is stated in the URL, and is among the supported languages,
    then it will return this code.
    Else, it will return the best match among the supported languages.

    Returns:
        str: The best matching language code ('en' or 'fr').
    """
    # Récupération de locale
    locale = request.args.get("locale")
    # S'il existe et qu'il est dans Config.LANGUAGES, on force ce langage
    if locale and locale in Config.LANGUAGES:
        return locale
    # Sinon, la fonction fonctionne normalement
    language = request.accept_languages.best_match(Config.LANGUAGES)
    return language


# Initialisation de l'application avec Flask_Babel
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Before Request that set a g_user
    """
    g.user = get_user()


# Création de la route '/'
@app.route("/")
def index():
    """
    Function that will print the template
    """
    return render_template("5-index.html")


# Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

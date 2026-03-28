#!/usr/bin/env python3
"""
App Module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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
babel = Babel(app)

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
    then it will return this code. (Priority 1)
    If a user is logged in, and that its locale is among the supported
    languages, then it will return this code. (Priority 2)
    Else, it will return the best match among the supported languages.
    (Priority 3)


    Returns:
        str: The best matching language code ('en' or 'fr').
    """
    # Récupération de locale dans l'URL. (Priorité 1)
    locale = request.args.get("locale")
    # S'il existe et qu'il est dans Config.LANGUAGES, on force ce langage
    if locale and locale in Config.LANGUAGES:
        return locale

    # Vérification qu'un user est loggé pour récupérer son locale. (Priorité 2)
    user = get_user()
    # S'il est loggé, et qu'il est dans Config.LANGUAGES, on force ce langage
    if user and user["locale"] in Config.LANGUAGES:
        return user["locale"]

    # Sinon, la fonction fonctionne normalement (Priorité 3)
    language = request.accept_languages.best_match(Config.LANGUAGES)
    return language


def get_timezone() -> str:
    """
    Return the best matching timezone based on request parameters and user
    settings.

    If the timezone is stated in the URL, and is a valid one, then it will
    return this timezone. (Priority 1)
    If a user is logged in, and that its timezone is a valid one, then it
    will return this timezone. (Priority 2)
    Else, it will return the default timezone (Priority 3)

    Returns:
        str: The valid timezone.
    """
    # Récupération de Timezone dans l'URL. (Priorité 1)
    url_timezone = request.args.get("timezone")
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Vérification qu'un user est loggé pour récupérer sa timezone (Priorité 2)
    user = get_user()
    if user and user["timezone"]:
        try:
            user_timezone = user["timezone"]
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Sinon, la fonction fonctionne normalement (Priorité 3)
    return Config.BABEL_DEFAULT_TIMEZONE


# Initialisation de l'application avec Flask_Babel
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.before_request
def before_request():
    """
    Before Request that sets a g.user and a g.timezone
    """
    g.user = get_user()
    g.timezone = get_timezone()


# Création de la route '/'
@app.route("/")
def index():
    """
    Function that will print the template
    """
    return render_template("7-index.html")


# Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

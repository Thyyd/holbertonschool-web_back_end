#!/usr/bin/env python3
"""
App Module
"""

from flask import Flask, render_template, request
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


def get_locale() -> str:
    """
    Function that determines the best match among the supported languages

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


# Création de la route '/'
@app.route("/")
def index():
    """
    Function that will print the template
    """
    return render_template("4-index.html")


# Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

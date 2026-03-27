#!/usr/bin/env python3
"""
App Module
"""

from flask import Flask, render_template
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
babel = Babel(app)


# Création de la route '/'
@app.route("/")
def index():
    """
    Function that will print the template
    """
    return render_template("1-index.html")


# Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

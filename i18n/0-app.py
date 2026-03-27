#!/usr/bin/env python3
"""
App Module
"""

from flask import Flask, render_template

# Création de l'application Flask
app = Flask(__name__)


# Création de la route /
@app.route("/")
def index():
    """
    Function that will print the template
    """
    return render_template("0-index.html")


# Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

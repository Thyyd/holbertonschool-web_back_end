#!/usr/bin/env python3
"""
This module defines the filter_datum function that will obfuscate
the content of a string
"""
import re
from typing import List
import logging
import os
import mysql.connector

# Constante PII Fields : Les 5 champs les plus importants à camoufler
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


# Fonction filter_datum
def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that returns the log message with the specified fields obfuscated.

    Parameters :
        - fields : List of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
        - message: a string representing the log line
        - separator: a string representing by which character is separating all
        fields in the log line (message)

    Returns :
        The log message with fields obfuscated
    """
    # Récupération du pattern
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    # Retour du message masqué
    return re.sub(pattern, r"\1=" + redaction, message)


# Classe RedactingFormatter
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    # Constructeur Init
    def __init__(self, fields: List[str]):
        """
        Method __init__ that initialise the formatter

        Parameters :
            fields: list of strings
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    # Méthode format
    def format(self, record: logging.LogRecord) -> str:
        """
        Method that obfuscate Personal data from the record

        Parameters :
            record: LogRecord to format

        Returns :
            The formated and obfuscated message
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


# Fonction get_logger
def get_logger() -> logging.Logger:
    """
    Function get_logger that will return a logging.Logger object.

    Returns :
        A configured logging.Logger object that will obfuscate PII fields.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Génération du Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


# Fonction get_db
def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a MySQLConnection object connected to the database using
    credentials from environment variables.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Création de la variable connection
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return connection


# Fonction main
def main() -> None:
    """
    Main function that will retrieve all users data from the database
    and display these with the PII fields obfuscated
    """
    # Récupération du Logger
    logger = get_logger()

    # Connexion à la db
    db = get_db()
    cursor = db.cursor()  # Permet d'énvoyer des requêtes SQL à la base

    # Récupération des datas de la table users
    cursor.execute("SELECT * FROM users;")

    # Récupérer les noms des champs
    headers = []
    for column in cursor.description:
        headers.append(column[0])

    # Récupération des valeurs des champs
    for row in cursor:
        message = ""

        for i in range(len(row)):
            message += f"{headers[i]}={row[i]}; "

        logger.info(message.strip())  # Affichage du message avec PII masqués

    # Fermeture de la db et libération de la connexion au réseau
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

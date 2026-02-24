#!/usr/bin/env python3
"""
This module defines the filter_datum function that will obfuscate
the content of a string
"""
import re
from typing import List
import logging

# Constante PII Fields : Les 5 champs les plus importants à camoufler
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that return the log message with the specified fields obfuscated.

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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Method __init__ that initialise the formatter

        Parameters :
            fields: list of strings
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

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

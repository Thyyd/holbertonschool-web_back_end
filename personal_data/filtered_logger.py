#!/usr/bin/env python3
"""
This module defines the filter_datum function that will obfuscate
the content of a string
"""
import re
from typing import List


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

#!/usr/bin/env python3
"""
This module defines the filter_datum function that will obfuscate
the content of a string
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Docstring for filter_datum

    Parameters :
        - fields : List of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
        - message: a string representing the log line
        - separator: a string representing by which character is separating all
        fields in the log line (message)

    Returns :
        The log message with fields obfuscated
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, r"\1=" + redaction, message)

#!/usr/bin/env python3
"""
Module api.v1.auth.basic_auth

This module defines the BasicAuth class that extends the Auth class.
It is used to handle Basic HTTP authentication when the environment
variable AUTH_TYPE is set to "basic_auth".
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    pass

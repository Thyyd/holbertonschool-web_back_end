#!/usr/bin/env python3
"""
Module api.v1.auth.basic_auth

This module defines the BasicAuth class that extends the Auth class.
It is used to handle Basic HTTP authentication when the environment
variable AUTH_TYPE is set to "basic_auth".
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class that implements Basic HTTP authentication.

    This class extends the Auth class and provides methods to
    handle Basic Authentication by extracting and decoding
    credentials from the Authorization header.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header.

        Parameters:
            authorization_header (str): The full Authorization header value.

        Returns:
            str: The Base64 encoded part of the header if valid.
            None: If authorization_header is None, not a string,
            or does not start with "Basic ".
        """
        # Si authorization_header vaut None
        if authorization_header is None:
            return None

        # Si authorization_header n'est pas une string
        if not isinstance(authorization_header, str):
            return None

        # Si authorization_header ne commence pas par "Basic "
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    # Méthode decode_base64_authorization_header
    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Décode une chaîne encodée en Base64 et retourne sa valeur UTF-8.

        Parameters:
            base64_authorization_header (str): La chaîne Base64 à décoder.

        Returns:
            str: La chaîne décodée en UTF-8 si le décodage réussit.
            None si :
                - base64_authorization_header vaut None
                - base64_authorization_header n'est pas une string
                - la chaîne n'est pas un Base64 valide
        """
        # Si base64_authorization_header vaut None
        if base64_authorization_header is None:
            return None

        # Si base64_authorization_header n'est pas une string
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)

            decoded_string = decoded_bytes.decode("utf-8")
            return decoded_string
        except Exception:
            return None

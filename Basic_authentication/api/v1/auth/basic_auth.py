#!/usr/bin/env python3
"""
Module api.v1.auth.basic_auth

This module defines the BasicAuth class that extends the Auth class.
It is used to handle Basic HTTP authentication when the environment
variable AUTH_TYPE is set to "basic_auth".
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User


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

    # Méthode extract_user_credentials
    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
            Extrait l’email et le mot de passe depuis une chaîne Base64
            décodée.

            Parameters:
                decoded_base64_authorization_header (str): chaîne de type
                "email:pwd"

            Returns:
                tuple: (email, pwd) si valide, sinon (None, None)
        """
        # Si decoded_base64_authorization_header vaut None
        if decoded_base64_authorization_header is None:
            return None, None

        # Si decoded_base64_authorization_header n'est pas une String
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Si decoded_base64_authorization_header d'a pas de ':'
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Récupération du String avant et après le ':' dans email et pwd
        email, pwd = decoded_base64_authorization_header.split(':', 1)
        return email, pwd

    # Méthode user_object_from_credentials
    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        Retourne l'instance User correspondant à l'email et au mot de passe
        fournis.

        Parameters:
            - user_email (str): L'email de l'utilisateur à rechercher.
            - user_pwd (str): Le mot de passe à vérifier pour l'utilisateur
            trouvé.

        Returns:
            - User: L'instance de l'utilisateur si un utilisateur avec cet
            email existe et si le mot de passe fourni est correct.
            - None: Si user_email ou user_pwd sont None ou ne sont pas des
            strings, si aucun utilisateur avec cet email n'existe dans la
            base de données, ou si le mot de passe fourni ne correspond pas
            à l'utilisateur.
        """
        # Si user_email vaut None OU n'est pas un String
        if user_email is None or not isinstance(user_email, str):
            return None

        # Si user_pwd vaut None OU n'est pas un String
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # On essaye de créer une instance de User, si la base de donnée existe
        try:
            user_list = User.search({'email': user_email})
        except Exception:
            return None

        # Si l'user n'existe pas dans la base de données
        if not user_list:
            return None

        # Si le pwd fourni n'est pas correct
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    # Méthode curren_user
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a given request using
        Basic Authentication.

        This method extracts the Authorization header, decodes
        the Base64 credentials, retrieves the user email and
        password, and returns the corresponding User instance.

        Parameters:
            request: The Flask request object.

        Returns:
            User: The authenticated user.
            None: If authentication fails at any step.
        """
        # Récupération du Header authorization
        authorization = self.authorization_header(request)
        if authorization is None:
            return None

        # Extraction de la partie Base64
        base64_authorization = (
            self.extract_base64_authorization_header(authorization)
        )
        if base64_authorization is None:
            return None

        # Décodage de la Base64
        decoded_authorization = (
            self.decode_base64_authorization_header(base64_authorization)
        )
        if decoded_authorization is None:
            return None

        # Récupération de l'email et du pwd
        email, pwd = self.extract_user_credentials(decoded_authorization)
        if email is None or pwd is None:
            return None

        # Récupération de l'user
        user = self.user_object_from_credentials(email, pwd)

        return user

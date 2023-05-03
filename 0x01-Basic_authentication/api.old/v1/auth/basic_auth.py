#!/usr/bin/env python3
"""Basic authentication"""

import base64
from typing import Tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication implementation"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """
        Return the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header and isinstance(authorization_header, str):
            if authorization_header.split(' ')[0] != 'Basic':
                return None
            return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """
        Return the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header and \
                isinstance(base64_authorization_header, str):
            try:
                return base64.b64decode(
                    base64_authorization_header).decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """
        Return the user email and password from the
        Base64 decoded value
        """
        if decoded_base64_authorization_header and \
                isinstance(decoded_base64_authorization_header, str):
            if ':' not in decoded_base64_authorization_header:
                return (None, None)
            email, password = decoded_base64_authorization_header.split(':')
            return (email, password)
        return (None, None)

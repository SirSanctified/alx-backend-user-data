#!/usr/bin/env python3
"""Basic authentication"""

from auth import Auth


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

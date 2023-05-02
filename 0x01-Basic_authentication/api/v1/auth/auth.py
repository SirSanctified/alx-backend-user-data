from typing import List, TypeVar
from flask import request


class Auth:
    """Manage API authentication"""
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """Check if authentication is required to access route"""
        return False

    def authorization_header(self, header=None) -> str:
        """Return a flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current logged in user"""
        return None

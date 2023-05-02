#!/usr/bin/env python3
"""Skeleton authentication class"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required to access route"""
        if path is None or excluded_paths is None:
            return True
        for p in excluded_paths:
            if path.rstrip('/') == p.rstrip('/'):
                return False
        return True

    def authorization_header(self, header=None) -> str:
        """Return a flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current logged in user"""
        return None

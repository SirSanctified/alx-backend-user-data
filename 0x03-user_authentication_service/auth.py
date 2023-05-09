#!/usr/bin/env python3
"""
Authentication module
"""

import bcrypt
import base64


def _hash_password(password: str) -> str:
    """Hash the password using the bcrypt module"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

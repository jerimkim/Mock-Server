"""
Ingresso Mock Server Authentication Module
Handles Basic Authentication for API requests
"""

from functools import wraps
from flask import request, jsonify
import base64
from ingresso_config import USERNAME, PASSWORD


def check_auth(username, password):
    """Verify username and password"""
    return username == USERNAME and password == PASSWORD


def authenticate():
    """Send 401 response that enables basic auth"""
    return jsonify({
        "error": "Authentication required",
        "message": "Please provide valid credentials"
    }), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}


def require_basic_auth(f):
    """
    Decorator to require Basic Authentication for endpoints
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization

        if not auth:
            return authenticate()

        if not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)

    return decorated_function

"""
Authentication utilities for Disney HK Mock Server
"""

import hashlib
import json
from datetime import datetime
from functools import wraps
from flask import request, jsonify
from config import SECRET_AUTHENTICATION_KEY, REQUEST_TIME_TOLERANCE, AGENT_ID


def generate_signature(message, secret_key):
    """
    Generate SHA-256 signature
    signature = SHA-256 Hash (message||Secret Authentication Key)
    """
    concatenated = f"{message}||{secret_key}"
    return hashlib.sha256(concatenated.encode('utf-8')).hexdigest()


def verify_signature(message, signature):
    """
    Verify the signature
    """
    expected_signature = generate_signature(message, SECRET_AUTHENTICATION_KEY)
    return signature == expected_signature


def verify_request_time(request_time_str):
    """
    Verify that request time is within 15 minutes of current time
    """
    try:
        request_time = datetime.strptime(request_time_str, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()
        time_diff = abs((current_time - request_time).total_seconds())
        return time_diff <= REQUEST_TIME_TOLERANCE
    except Exception:
        return False


def require_auth(f):
    """
    Decorator to require authentication for API endpoints
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get message and signature from JSON body
        try:
            request_body = request.get_json(force=True)
        except Exception:
            return jsonify({
                "responseCode": "1002",
                "message": "Invalid message format"
            }), 400

        if not request_body:
            return jsonify({
                "responseCode": "1002",
                "message": "Invalid message format"
            }), 400

        message = request_body.get('message')
        signature = request_body.get('Signature')

        if not message or not signature:
            return jsonify({
                "responseCode": "1002",
                "message": "Invalid message format"
            }), 400

        # Verify signature
        if not verify_signature(message, signature):
            return jsonify({
                "responseCode": "1001",
                "message": "Invalid signature"
            }), 401

        # Parse message
        try:
            message_data = json.loads(message)
        except json.JSONDecodeError:
            return jsonify({
                "responseCode": "1002",
                "message": "Invalid message format"
            }), 400

        # Verify agent ID
        if message_data.get('agentId') != AGENT_ID:
            return jsonify({
                "responseCode": "1003",
                "message": "Invalid Agent ID"
            }), 403

        # Verify request time
        request_time = message_data.get('requestTime')
        if not request_time or not verify_request_time(request_time):
            return jsonify({
                "responseCode": "1004",
                "message": "Request expired"
            }), 400

        # Pass message_data to the endpoint
        return f(message_data, *args, **kwargs)

    return decorated_function

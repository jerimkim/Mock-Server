"""
Ingresso Mock Server
Flask-based mock server for Ingresso Ticketing API
"""

from flask import Flask, jsonify, request
from auth import require_basic_auth
from config import HOST, PORT, DEBUG
from mock_data import (
    EVENTS_RESPONSE,
    EVENTS_BY_ID_RESPONSE,
    MONTHS_RESPONSE,
    PERFORMANCES_RESPONSE,
    PERFORMANCE_DETAIL_RESPONSE,
    AVAILABILITY_RESPONSE,
    RESERVE_RESPONSE,
    RESERVATIONS,
    # Error responses
    ERROR_BAD_CHANNEL,
    ERROR_AUTH_FAILURE,
    ERROR_BACKEND_CONNECTION,
    ERROR_FORBIDDEN_NETWORK,
    ERROR_DATABASE_CONNECTION,
    ERROR_MEMBERSHIP_AUTH,
    ERROR_BAD_DATA,
    ERROR_EMAIL_BLANK,
    ERROR_EMAIL_MISSING_AT,
    ERROR_EMAIL_BAD_DOMAIN,
    ERROR_EMAIL_SPACES_AFTER_AT,
    ERROR_EMAIL_NON_ASCII,
    ERROR_CARD_UNRECOGNISED,
    ERROR_CARD_NOT_ACCEPTED,
    ERROR_CARD_INVALID_NUMBER,
    ERROR_CARD_INVALID_EXPIRY,
    ERROR_CARD_INVALID_CV2,
    ERROR_CARD_MISSING_ISSUE,
    ERROR_CARD_INVALID_ISSUE,
    ERROR_CARD_MISSING_START_DATE,
    ERROR_CARD_INVALID_START_DATE,
    EMAIL_ERROR_KEYS
)

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Ingresso Mock Server"
    }), 200


@app.route('/f13/events.v1', methods=['GET'])
@require_basic_auth
def get_events():
    """
    Get events list
    Query parameters:
    - keywords (optional): Search keyword
    """
    keywords = request.args.get('keywords')

    # For now, return the same response regardless of keywords
    # Can be extended to filter by keywords if needed
    return jsonify(EVENTS_RESPONSE), 200


@app.route('/f13/events_by_id.v1', methods=['GET'])
@require_basic_auth
def get_events_by_id():
    """
    Get event details by ID
    Query parameters:
    - event_id_list (required): Event ID
    """
    event_id_list = request.args.get('event_id_list')

    if not event_id_list:
        return jsonify({
            "error": "Missing required parameter",
            "message": "event_id_list is required"
        }), 400

    if not EVENTS_BY_ID_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    return jsonify(EVENTS_BY_ID_RESPONSE), 200


@app.route('/f13/months.v1', methods=['GET'])
@require_basic_auth
def get_months():
    """
    Get available months for an event
    Query parameters:
    - event_id (required): Event ID
    """
    event_id = request.args.get('event_id')

    if not event_id:
        return jsonify({
            "error": "Missing required parameter",
            "message": "event_id is required"
        }), 400

    if not MONTHS_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    return jsonify(MONTHS_RESPONSE), 200


@app.route('/f13/performances.v1', methods=['GET'])
@require_basic_auth
def get_performances():
    """
    Get performances for an event on a specific date
    Query parameters:
    - event_id (required): Event ID
    - date (required): Date in format YYYY-MM-DD
    """
    event_id = request.args.get('event_id')
    date = request.args.get('date')

    if not event_id or not date:
        return jsonify({
            "error": "Missing required parameters",
            "message": "event_id and date are required"
        }), 400

    if not PERFORMANCES_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    return jsonify(PERFORMANCES_RESPONSE), 200


@app.route('/f13/performances_by_id.v1', methods=['GET'])
@require_basic_auth
def get_performance_by_id():
    """
    Get performance details by ID
    Query parameters:
    - perf_id_list (required): Performance ID
    - req_avail_details (optional): Request availability details (true/false)
    """
    perf_id_list = request.args.get('perf_id_list')
    req_avail_details = request.args.get('req_avail_details', 'false')

    if not perf_id_list:
        return jsonify({
            "error": "Missing required parameter",
            "message": "perf_id_list is required"
        }), 400

    if not PERFORMANCE_DETAIL_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    return jsonify(PERFORMANCE_DETAIL_RESPONSE), 200


@app.route('/f13/availability.v1', methods=['GET'])
@require_basic_auth
def get_availability():
    """
    Get availability for a performance
    Query parameters:
    - perf_id (required): Performance ID
    """
    perf_id = request.args.get('perf_id')

    if not perf_id:
        return jsonify({
            "error": "Missing required parameter",
            "message": "perf_id is required"
        }), 400

    if not AVAILABILITY_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    return jsonify(AVAILABILITY_RESPONSE), 200


@app.route('/f13/reserve.v1', methods=['POST'])
@require_basic_auth
def reserve():
    """
    Reserve tickets
    Form parameters:
    - perf_id (required): Performance ID
    - ticket_type_code (required): Ticket type code
    - price_band_code (required): Price band code
    - no_of_seats (required): Number of seats
    """
    perf_id = request.form.get('perf_id')
    ticket_type_code = request.form.get('ticket_type_code')
    price_band_code = request.form.get('price_band_code')
    no_of_seats = request.form.get('no_of_seats')

    if not all([perf_id, ticket_type_code, price_band_code, no_of_seats]):
        return jsonify({
            "error": "Missing required parameters",
            "message": "perf_id, ticket_type_code, price_band_code, and no_of_seats are required"
        }), 400

    if not RESERVE_RESPONSE:
        return jsonify({
            "error": "Not implemented",
            "message": "Response data not yet configured"
        }), 501

    # Store reservation (will be implemented when response data is provided)
    reservation_key = f"{perf_id}_{ticket_type_code}_{price_band_code}"
    RESERVATIONS[reservation_key] = {
        "perf_id": perf_id,
        "ticket_type_code": ticket_type_code,
        "price_band_code": price_band_code,
        "no_of_seats": no_of_seats
    }

    return jsonify(RESERVE_RESPONSE), 200


@app.route('/f13/test_errors.v1', methods=['GET'])
@require_basic_auth
def test_errors():
    """
    Test error responses
    Query parameters:
    - error_code (required): Error code to test (2-8, 2000, 3000-3008)
    - email_error_key (optional): Specific email error key for error_code 2000

    Examples:
    - /f13/test_errors.v1?error_code=2        # Bad channel
    - /f13/test_errors.v1?error_code=8        # Bad data
    - /f13/test_errors.v1?error_code=2000&email_error_key=addr_missing_at
    - /f13/test_errors.v1?error_code=3002     # Invalid card number
    """
    error_code = request.args.get('error_code')

    if not error_code:
        return jsonify({
            "error": "Missing required parameter",
            "message": "error_code is required"
        }), 400

    try:
        error_code = int(error_code)
    except ValueError:
        return jsonify({
            "error": "Invalid parameter",
            "message": "error_code must be a number"
        }), 400

    # Map error codes to responses and HTTP status codes
    error_mapping = {
        2: (ERROR_BAD_CHANNEL, 460),
        3: (ERROR_AUTH_FAILURE, 401),
        4: (ERROR_BACKEND_CONNECTION, 502),
        5: (ERROR_FORBIDDEN_NETWORK, 403),
        6: (ERROR_DATABASE_CONNECTION, 500),
        7: (ERROR_MEMBERSHIP_AUTH, 401),
        8: (ERROR_BAD_DATA, 460),
        3000: (ERROR_CARD_UNRECOGNISED, 460),
        3001: (ERROR_CARD_NOT_ACCEPTED, 460),
        3002: (ERROR_CARD_INVALID_NUMBER, 460),
        3003: (ERROR_CARD_INVALID_EXPIRY, 460),
        3004: (ERROR_CARD_INVALID_CV2, 460),
        3005: (ERROR_CARD_MISSING_ISSUE, 460),
        3006: (ERROR_CARD_INVALID_ISSUE, 460),
        3007: (ERROR_CARD_MISSING_START_DATE, 460),
        3008: (ERROR_CARD_INVALID_START_DATE, 460),
    }

    # Handle email errors (2000)
    if error_code == 2000:
        email_error_key = request.args.get('email_error_key', 'addr_may_not_be_blank')

        if email_error_key not in EMAIL_ERROR_KEYS:
            return jsonify({
                "error": "Invalid email_error_key",
                "message": f"Valid keys: {', '.join(EMAIL_ERROR_KEYS.keys())}"
            }), 400

        error_response = {
            "error_code": 2000,
            "error_desc": "Email address is invalid",
            "error_key": email_error_key,
            "transaction_uuid": f"U-TEST-EMAIL-ERROR-{email_error_key.upper()}"
        }
        return jsonify(error_response), 460

    # Handle other errors
    if error_code in error_mapping:
        error_response, status_code = error_mapping[error_code]
        return jsonify(error_response), status_code

    return jsonify({
        "error": "Unknown error_code",
        "message": f"Supported error codes: 2-8, 2000, 3000-3008"
    }), 400


@app.route('/f13/test_errors.v1/list', methods=['GET'])
def list_error_codes():
    """
    List all available error codes for testing (no auth required for convenience)
    """
    return jsonify({
        "general_errors": {
            "2": "Bad channel",
            "3": "User authentication failure",
            "4": "Failed to create connection to the backend system",
            "5": "Host is on a forbidden network",
            "6": "Failed to connect to database",
            "7": "Membership authentication failed",
            "8": "Bad data supplied"
        },
        "email_errors": {
            "2000": "Email address is invalid (use email_error_key parameter)",
            "email_error_keys": list(EMAIL_ERROR_KEYS.keys())
        },
        "card_errors": {
            "3000": "Unrecognised card type from number",
            "3001": "Card type not accepted",
            "3002": "Not a valid card number",
            "3003": "Invalid expiry date",
            "3004": "Invalid CV2",
            "3005": "Missing issue number",
            "3006": "Invalid issue number",
            "3007": "Missing start date",
            "3008": "Invalid start date"
        },
        "usage": {
            "endpoint": "/f13/test_errors.v1",
            "method": "GET",
            "auth": "Basic Auth required",
            "parameters": {
                "error_code": "Required - Error code to test",
                "email_error_key": "Optional - For error_code=2000 only"
            },
            "examples": [
                "/f13/test_errors.v1?error_code=2",
                "/f13/test_errors.v1?error_code=8",
                "/f13/test_errors.v1?error_code=2000&email_error_key=addr_missing_at",
                "/f13/test_errors.v1?error_code=3002"
            ]
        }
    }), 200


if __name__ == '__main__':
    print(f"Starting Ingresso Mock Server on {HOST}:{PORT}")
    print(f"Basic Auth credentials: demo / demopass")
    print("\nAvailable endpoints:")
    print("  GET  /health")
    print("  GET  /f13/events.v1")
    print("  GET  /f13/events_by_id.v1")
    print("  GET  /f13/months.v1")
    print("  GET  /f13/performances.v1")
    print("  GET  /f13/performances_by_id.v1")
    print("  GET  /f13/availability.v1")
    print("  POST /f13/reserve.v1")
    print("\nError testing endpoints:")
    print("  GET  /f13/test_errors.v1/list    (no auth - list all error codes)")
    print("  GET  /f13/test_errors.v1?error_code=<code>")
    app.run(host=HOST, port=PORT, debug=DEBUG)
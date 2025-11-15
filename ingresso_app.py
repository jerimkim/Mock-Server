"""
Ingresso Mock Server
Flask-based mock server for Ingresso Ticketing API
"""

from flask import Flask, jsonify, request
from ingresso_auth import require_basic_auth
from ingresso_config import HOST, PORT, DEBUG
from ingresso_mock_data import (
    EVENTS_RESPONSE,
    EVENTS_BY_ID_RESPONSE,
    MONTHS_RESPONSE,
    PERFORMANCES_RESPONSE,
    PERFORMANCE_DETAIL_RESPONSE,
    AVAILABILITY_RESPONSE,
    RESERVE_RESPONSE,
    RESERVATIONS
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
    app.run(host=HOST, port=PORT, debug=DEBUG)
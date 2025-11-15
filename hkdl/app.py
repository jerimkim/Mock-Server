"""
Disney HK OTE-OTA Mock Server
Based on D-OTE-OTA_Integration_Guide_v_1.8.pdf
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json
import copy

from auth import require_auth
from mock_data import (
    EVENTS_RESPONSE,
    SHOWS_RESPONSE,
    TICKETS_RESPONSE,
    PICKUP_DETAILS_RESPONSE,
    RESERVE_ORDER_RESPONSE,
    CANCEL_ORDER_RESPONSE,
    ORDER_STATUS_COMPLETED,
    ORDER_STATUS_NOT_FOUND,
    ORDER_STATUS_CANCEL_PENDING,
    ORDER_STATUS_CANCELLED,
    RESERVATIONS,
    CANCELLED_RESERVATIONS
)

app = Flask(__name__)


@app.route('/OTA/GetEvents', methods=['POST'])
@require_auth
def get_events(message_data):
    """
    GetEvents API
    Returns the list of events available for the OTA
    """
    return jsonify(EVENTS_RESPONSE)


@app.route('/OTA/GetShows', methods=['POST'])
@require_auth
def get_shows(message_data):
    """
    GetShows API
    Returns the list of shows of a specific event
    """
    event_id = message_data.get('eventId')
    from_date = message_data.get('fromDate')
    to_date = message_data.get('toDate')
    qty = message_data.get('qty')

    # Validate required parameters
    if not event_id:
        return jsonify({
            "responseCode": "4101",
            "message": "Invalid Event ID"
        }), 400

    if not from_date or not to_date:
        return jsonify({
            "responseCode": "1005",
            "message": "Invalid request information"
        }), 400

    # Check if event is Date Specific
    if event_id != "34":  # Only event 34 is Date Specific in our mock data
        return jsonify({
            "responseCode": "4103",
            "message": "Event is not Date Specific"
        }), 400

    return jsonify(SHOWS_RESPONSE)


@app.route('/OTA/GetTickets', methods=['POST'])
@require_auth
def get_tickets(message_data):
    """
    GetTickets API
    Returns the list of tickets of a specific event or a specific show
    """
    event_id = message_data.get('eventId')
    show_id = message_data.get('showId')

    # Validate required parameters
    if not event_id:
        return jsonify({
            "responseCode": "4101",
            "message": "Invalid Event ID"
        }), 400

    return jsonify(TICKETS_RESPONSE)


@app.route('/OTA/GetPickupDetails', methods=['POST'])
@require_auth
def get_pickup_details(message_data):
    """
    GetPickupDetails API
    Returns the list of pickup methods of a specific event
    """
    event_id = message_data.get('eventId')

    # Validate required parameters
    if not event_id:
        return jsonify({
            "responseCode": "4101",
            "message": "Invalid Event ID"
        }), 400

    return jsonify(PICKUP_DETAILS_RESPONSE)


@app.route('/OTA/ReserveOrder', methods=['POST'])
@require_auth
def reserve_order(message_data):
    """
    ReserveOrder API
    Allows OTA to make order reservation
    """
    request_id = message_data.get('requestId')
    event_id = message_data.get('eventId')
    items = message_data.get('items')
    pickup_id = message_data.get('pickupId')
    lang = message_data.get('lang')

    # Validate required parameters
    if not request_id:
        return jsonify({
            "responseCode": "1005",
            "message": "Invalid request information - missing requestId"
        }), 400

    if not event_id:
        return jsonify({
            "responseCode": "4101",
            "message": "Invalid Event ID"
        }), 400

    if not items or len(items) == 0:
        return jsonify({
            "responseCode": "1005",
            "message": "Invalid request information - missing items"
        }), 400

    if not pickup_id:
        return jsonify({
            "responseCode": "4308",
            "message": "Invalid Pickup ID"
        }), 400

    if not lang:
        return jsonify({
            "responseCode": "4502",
            "message": "Missing or Invalid Language Preference"
        }), 400

    # Check for duplicate request
    if request_id in RESERVATIONS:
        return jsonify({
            "responseCode": "3001",
            "message": "Duplicated Request"
        }), 400

    # Generate response with current timestamp
    response = copy.deepcopy(RESERVE_ORDER_RESPONSE)
    response['detail']['transactionDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store reservation
    RESERVATIONS[request_id] = {
        "reservationNo": response['reservationNo'],
        "voucherNo": response['voucherNo'],
        "data": message_data,
        "response": response
    }

    return jsonify(response)


@app.route('/OTA/CancelOrder', methods=['POST'])
@require_auth
def cancel_order(message_data):
    """
    CancelOrder API
    Allows OTA to make order cancellation request
    """
    reservation_no = message_data.get('reservationNo')

    # Validate required parameters
    if not reservation_no:
        return jsonify({
            "responseCode": "1005",
            "message": "Invalid request information - missing reservationNo"
        }), 400

    # Check if reservation exists
    found = False
    for req_id, res_data in RESERVATIONS.items():
        if res_data['reservationNo'] == reservation_no:
            found = True
            CANCELLED_RESERVATIONS.add(reservation_no)
            break

    if not found:
        return jsonify({
            "responseCode": "1007",
            "message": "Reservation not found"
        }), 404

    return jsonify(CANCEL_ORDER_RESPONSE)


@app.route('/OTA/GetOrderStatus', methods=['POST'])
@require_auth
def get_order_status(message_data):
    """
    GetOrderStatus API
    Allows OTA to make order status enquiry
    """
    request_id = message_data.get('requestId')
    reservation_no = message_data.get('reservationNo')

    # Either requestId or reservationNo must be provided
    if not request_id and not reservation_no:
        return jsonify({
            "responseCode": "1005",
            "message": "Invalid request information - missing requestId or reservationNo"
        }), 400

    # Find reservation
    reservation_data = None

    if request_id and request_id in RESERVATIONS:
        reservation_data = RESERVATIONS[request_id]
    elif reservation_no:
        for req_id, res_data in RESERVATIONS.items():
            if res_data['reservationNo'] == reservation_no:
                reservation_data = res_data
                break

    if not reservation_data:
        return jsonify(ORDER_STATUS_NOT_FOUND)

    # Check if cancelled
    if reservation_data['reservationNo'] in CANCELLED_RESERVATIONS:
        response = copy.deepcopy(ORDER_STATUS_CANCELLED)
        response['reservationNo'] = reservation_data['reservationNo']
        response['voucherNo'] = reservation_data['voucherNo']
        return jsonify(response)

    # Return completed status with full details
    response = copy.deepcopy(ORDER_STATUS_COMPLETED)
    response['reservationNo'] = reservation_data['reservationNo']
    response['voucherNo'] = reservation_data['voucherNo']

    return jsonify(response)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        "status": "healthy",
        "service": "Disney HK OTE-OTA Mock Server",
        "version": "1.8"
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "responseCode": "9999",
        "message": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "responseCode": "9999",
        "message": "Internal server error"
    }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("Disney HK OTE-OTA Mock Server")
    print("Based on: D-OTE-OTA_Integration_Guide_v_1.8.pdf")
    print("=" * 60)
    print("\nAvailable Endpoints:")
    print("  POST /OTA/GetEvents")
    print("  POST /OTA/GetShows")
    print("  POST /OTA/GetTickets")
    print("  POST /OTA/GetPickupDetails")
    print("  POST /OTA/ReserveOrder")
    print("  POST /OTA/CancelOrder")
    print("  POST /OTA/GetOrderStatus")
    print("  GET  /health")
    print("\nConfiguration:")
    print(f"  Agent ID: CITYLINE")
    print(f"  Secret Key: xY378DS731A")
    print("=" * 60)
    print("\nStarting server on http://0.0.0.0:5000")
    print("=" * 60)

    app.run(host='0.0.0.0', port=5000, debug=True)

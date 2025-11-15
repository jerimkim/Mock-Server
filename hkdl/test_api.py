"""
Test script for Disney HK OTE-OTA Mock Server
"""

import requests
import hashlib
import json
from datetime import datetime
import sys


BASE_URL = "http://localhost:5000"
SECRET_KEY = "xY378DS731A"


def generate_signature(message):
    """Generate SHA-256 signature"""
    concatenated = f"{message}||{SECRET_KEY}"
    return hashlib.sha256(concatenated.encode('utf-8')).hexdigest()


def make_request(endpoint, message_data):
    """Make API request with authentication"""
    message = json.dumps(message_data, separators=(',', ':'))
    signature = generate_signature(message)

    response = requests.post(
        f"{BASE_URL}{endpoint}",
        data={
            'message': message,
            'Signature': signature
        }
    )

    return response


def test_get_events():
    """Test GetEvents API"""
    print("\n" + "=" * 60)
    print("Testing GetEvents API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    response = make_request("/OTA/GetEvents", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_get_shows():
    """Test GetShows API"""
    print("\n" + "=" * 60)
    print("Testing GetShows API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "eventId": "34",
        "fromDate": "2023-10-01",
        "toDate": "2023-10-14",
        "qty": 6
    }

    response = make_request("/OTA/GetShows", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_get_tickets():
    """Test GetTickets API"""
    print("\n" + "=" * 60)
    print("Testing GetTickets API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "eventId": "34",
        "showId": 79
    }

    response = make_request("/OTA/GetTickets", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_get_pickup_details():
    """Test GetPickupDetails API"""
    print("\n" + "=" * 60)
    print("Testing GetPickupDetails API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "eventId": "34"
    }

    response = make_request("/OTA/GetPickupDetails", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_reserve_order():
    """Test ReserveOrder API"""
    print("\n" + "=" * 60)
    print("Testing ReserveOrder API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "requestId": f"TEST{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "eventId": "34",
        "showId": 79,
        "guestName": "CHAN TAI MAN",
        "guestEmail": "chantaiman@cityline.com.hk",
        "guestSms": "61111111",
        "lang": "en_US",
        "pickupId": 1,
        "referenceNo": "CL-001002003",
        "pickupDate": "2023-12-31",
        "items": [
            {
                "ticketId": "14",
                "qty": 4
            },
            {
                "ticketId": "15",
                "qty": 2
            }
        ]
    }

    response = make_request("/OTA/ReserveOrder", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    if response.status_code == 200:
        return response.json().get('reservationNo')
    return None


def test_cancel_order(reservation_no=None):
    """Test CancelOrder API"""
    print("\n" + "=" * 60)
    print("Testing CancelOrder API")
    print("=" * 60)

    if not reservation_no:
        reservation_no = "1234567890"

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reservationNo": reservation_no,
        "email": "chantaiman@xyz.com"
    }

    response = make_request("/OTA/CancelOrder", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_get_order_status(request_id=None):
    """Test GetOrderStatus API"""
    print("\n" + "=" * 60)
    print("Testing GetOrderStatus API")
    print("=" * 60)

    message_data = {
        "agentId": "CITYLINE",
        "requestTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    if request_id:
        message_data["requestId"] = request_id
    else:
        message_data["reservationNo"] = "1234567890"

    response = make_request("/OTA/GetOrderStatus", message_data)

    print(f"\nStatus Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def test_all():
    """Run all tests"""
    print("\n" + "=" * 80)
    print(" " * 20 + "Disney HK OTE-OTA Mock Server Test")
    print("=" * 80)

    try:
        # Test Product Enquiry APIs
        test_get_events()
        test_get_shows()
        test_get_tickets()
        test_get_pickup_details()

        # Test Order Reservation
        reservation_no = test_reserve_order()

        # Test Order Status
        test_get_order_status()

        # Test Order Cancellation
        if reservation_no:
            test_cancel_order(reservation_no)
        else:
            test_cancel_order()

        print("\n" + "=" * 80)
        print(" " * 30 + "All tests completed!")
        print("=" * 80 + "\n")

    except requests.exceptions.ConnectionError:
        print("\n[ERROR] Cannot connect to server. Please make sure the server is running.")
        print("Run: python app.py")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python test_api.py [command]")
        print("\nCommands:")
        print("  all                - Run all tests")
        print("  get_events         - Test GetEvents API")
        print("  get_shows          - Test GetShows API")
        print("  get_tickets        - Test GetTickets API")
        print("  get_pickup_details - Test GetPickupDetails API")
        print("  reserve_order      - Test ReserveOrder API")
        print("  cancel_order       - Test CancelOrder API")
        print("  get_order_status   - Test GetOrderStatus API")
        print()
        return

    command = sys.argv[1].lower()

    try:
        if command == "all":
            test_all()
        elif command == "get_events":
            test_get_events()
        elif command == "get_shows":
            test_get_shows()
        elif command == "get_tickets":
            test_get_tickets()
        elif command == "get_pickup_details":
            test_get_pickup_details()
        elif command == "reserve_order":
            test_reserve_order()
        elif command == "cancel_order":
            test_cancel_order()
        elif command == "get_order_status":
            test_get_order_status()
        else:
            print(f"Unknown command: {command}")
            print("Run 'python test_api.py' for usage information")

    except requests.exceptions.ConnectionError:
        print("\n[ERROR] Cannot connect to server. Please make sure the server is running.")
        print("Run: python app.py")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")


if __name__ == "__main__":
    main()

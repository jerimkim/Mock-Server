"""
Ingresso Mock Server Test Script
Tests all Ingresso API endpoints
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

BASE_URL = "http://localhost:5001"
USERNAME = "demo"
PASSWORD = "demopass"


def test_get_events():
    """Test GET /f13/events.v1"""
    print("\n=== Testing GET /f13/events.v1 ===")

    # Test with keywords
    response = requests.get(
        f"{BASE_URL}/f13/events.v1",
        params={"keywords": "sphere"},
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    assert response.status_code == 200, "Expected status code 200"
    assert "results" in response.json(), "Expected 'results' in response"

    print("✓ Test passed")


def test_get_events_by_id():
    """Test GET /f13/events_by_id.v1"""
    print("\n=== Testing GET /f13/events_by_id.v1 ===")

    response = requests.get(
        f"{BASE_URL}/f13/events_by_id.v1",
        params={"event_id_list": "1GNCR"},
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    # Will be 501 until response data is provided
    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_get_months():
    """Test GET /f13/months.v1"""
    print("\n=== Testing GET /f13/months.v1 ===")

    response = requests.get(
        f"{BASE_URL}/f13/months.v1",
        params={"event_id": "1GNCR"},
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_get_performances():
    """Test GET /f13/performances.v1"""
    print("\n=== Testing GET /f13/performances.v1 ===")

    response = requests.get(
        f"{BASE_URL}/f13/performances.v1",
        params={
            "event_id": "1GNCR",
            "date": "2024-12-01"
        },
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_get_performance_by_id():
    """Test GET /f13/performances_by_id.v1"""
    print("\n=== Testing GET /f13/performances_by_id.v1 ===")

    response = requests.get(
        f"{BASE_URL}/f13/performances_by_id.v1",
        params={
            "perf_id_list": "1234",
            "req_avail_details": "true"
        },
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_get_availability():
    """Test GET /f13/availability.v1"""
    print("\n=== Testing GET /f13/availability.v1 ===")

    response = requests.get(
        f"{BASE_URL}/f13/availability.v1",
        params={"perf_id": "1234"},
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_reserve():
    """Test POST /f13/reserve.v1"""
    print("\n=== Testing POST /f13/reserve.v1 ===")

    response = requests.post(
        f"{BASE_URL}/f13/reserve.v1",
        data={
            "perf_id": "1234",
            "ticket_type_code": "ADULT",
            "price_band_code": "A",
            "no_of_seats": "2"
        },
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 501:
        print("⚠ Not yet implemented (waiting for response data)")
    else:
        assert response.status_code == 200, "Expected status code 200"
        print("✓ Test passed")


def test_health():
    """Test GET /health"""
    print("\n=== Testing GET /health ===")

    response = requests.get(f"{BASE_URL}/health")

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    assert response.status_code == 200, "Expected status code 200"
    assert response.json()["status"] == "healthy", "Expected healthy status"

    print("✓ Test passed")


def test_all():
    """Run all tests"""
    print("=" * 60)
    print("Running all Ingresso API tests")
    print("=" * 60)

    test_health()
    test_get_events()
    test_get_events_by_id()
    test_get_months()
    test_get_performances()
    test_get_performance_by_id()
    test_get_availability()
    test_reserve()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        if test_name == 'all':
            test_all()
        elif test_name == 'health':
            test_health()
        elif test_name == 'get_events':
            test_get_events()
        elif test_name == 'get_events_by_id':
            test_get_events_by_id()
        elif test_name == 'get_months':
            test_get_months()
        elif test_name == 'get_performances':
            test_get_performances()
        elif test_name == 'get_performance_by_id':
            test_get_performance_by_id()
        elif test_name == 'get_availability':
            test_get_availability()
        elif test_name == 'reserve':
            test_reserve()
        else:
            print(f"Unknown test: {test_name}")
            print("Available tests: all, health, get_events, get_events_by_id, get_months,")
            print("                 get_performances, get_performance_by_id, get_availability, reserve")
    else:
        test_all()

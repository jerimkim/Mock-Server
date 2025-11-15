# Ingresso Mock Server

Flask-based mock server for Ingresso Ticketing API (Ticketswitch f13 API)

## Setup

1. Install dependencies:
```bash
pip install flask requests
```

2. Start the server:
```bash
python ingresso_app.py
```

The server will start on `http://localhost:5001`

## Authentication

All endpoints (except `/health`) require Basic Authentication:
- **Username**: `demo`
- **Password**: `demopass`

## Available Endpoints

### GET /health
Health check endpoint (no authentication required)

```bash
curl http://localhost:5001/health
```

### GET /f13/events.v1
Get events list

**Query Parameters:**
- `keywords` (optional): Search keyword

```bash
curl -X GET "http://localhost:5001/f13/events.v1?keywords=sphere" \
  -u "demo:demopass"
```

### GET /f13/events_by_id.v1
Get event details by ID

**Query Parameters:**
- `event_id_list` (required): Event ID

```bash
curl -X GET "http://localhost:5001/f13/events_by_id.v1?event_id_list=1GNCR" \
  -u "demo:demopass"
```

### GET /f13/months.v1
Get available months for an event

**Query Parameters:**
- `event_id` (required): Event ID

```bash
curl -X GET "http://localhost:5001/f13/months.v1?event_id=1GNCR" \
  -u "demo:demopass"
```

### GET /f13/performances.v1
Get performances for an event on a specific date

**Query Parameters:**
- `event_id` (required): Event ID
- `date` (required): Date in format YYYY-MM-DD

```bash
curl -X GET "http://localhost:5001/f13/performances.v1?event_id=1GNCR&date=2024-12-01" \
  -u "demo:demopass"
```

### GET /f13/performances_by_id.v1
Get performance details by ID

**Query Parameters:**
- `perf_id_list` (required): Performance ID
- `req_avail_details` (optional): Request availability details (true/false)

```bash
curl -X GET "http://localhost:5001/f13/performances_by_id.v1?perf_id_list=1234&req_avail_details=true" \
  -u "demo:demopass"
```

### GET /f13/availability.v1
Get availability for a performance

**Query Parameters:**
- `perf_id` (required): Performance ID

```bash
curl -X GET "http://localhost:5001/f13/availability.v1?perf_id=1234" \
  -u "demo:demopass"
```

### POST /f13/reserve.v1
Reserve tickets

**Form Parameters:**
- `perf_id` (required): Performance ID
- `ticket_type_code` (required): Ticket type code
- `price_band_code` (required): Price band code
- `no_of_seats` (required): Number of seats

```bash
curl -X POST "http://localhost:5001/f13/reserve.v1" \
  -u "demo:demopass" \
  -d "perf_id=1234" \
  -d "ticket_type_code=ADULT" \
  -d "price_band_code=A" \
  -d "no_of_seats=2"
```

## Testing

Run all tests:
```bash
python ingresso_test_api.py all
```

Run specific test:
```bash
python ingresso_test_api.py get_events
python ingresso_test_api.py reserve
```

Available tests:
- `health` - Health check
- `get_events` - Get events list
- `get_events_by_id` - Get event by ID
- `get_months` - Get available months
- `get_performances` - Get performances
- `get_performance_by_id` - Get performance details
- `get_availability` - Get availability
- `reserve` - Reserve tickets

## Project Structure

```
ingresso_app.py           # Main Flask application and routing
ingresso_auth.py          # Basic Authentication utilities
ingresso_config.py        # Configuration (credentials, server settings)
ingresso_mock_data.py     # Mock response data
ingresso_test_api.py      # API test script
ingresso_README.md        # This file
```

## Status

All endpoints are fully implemented and ready to use!

- ✅ `/f13/events.v1` - Implemented
- ✅ `/f13/events_by_id.v1` - Implemented
- ✅ `/f13/months.v1` - Implemented
- ✅ `/f13/performances.v1` - Implemented
- ✅ `/f13/performances_by_id.v1` - Implemented (40+ ticket types)
- ✅ `/f13/availability.v1` - Implemented (simplified with 4 ticket types)
- ✅ `/f13/reserve.v1` - Implemented
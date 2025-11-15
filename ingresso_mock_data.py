"""
Ingresso Mock Server Response Data
Contains mock responses for all Ingresso API endpoints
"""

# GET /f13/events.v1
# Example: GET /f13/events.v1?keywords=sphere
EVENTS_RESPONSE = {
    "results": {
        "event": [
            {
                "area_code": "US",
                "city_code": "las_vegas-us",
                "city_desc": "Las Vegas",
                "classes": {
                    "activities": "Activities",
                    "attractions": "Attractions"
                },
                "country_code": "us",
                "country_desc": "United States of America",
                "custom_filter": [],
                "event_code": "K8vZ9171UAf",
                "event_desc": "Safetix Test product",
                "event_id": "1GNCR",
                "event_path": "/1GNCR-safetix-test-product/",
                "event_status": "live",
                "event_type": "simple_ticket",
                "event_uri_desc": "Safetix-Test-product",
                "geo_data": {
                    "latitude": 36.1207267,
                    "longitude": -115.1642896
                },
                "has_no_perfs": False,
                "is_add_on": False,
                "is_auto_quantity_add_on": False,
                "is_date_matched_add_on": False,
                "is_seated": True,
                "is_time_matched_add_on": False,
                "main_class_key": "activities",
                "need_departure_date": False,
                "need_duration": False,
                "need_performance": True,
                "postcode": "89169",
                "show_perf_time": True,
                "source_code": "ticketmaster_test",
                "source_desc": "ticketmaster test",
                "venue_code": "KovZ917Atbr",
                "venue_desc": "Sphere",
                "venue_uri_desc": "Sphere"
            }
        ],
        "paging_status": {
            "page_length": 50,
            "page_number": 0,
            "pages_remaining": 0,
            "results_remaining": 0,
            "total_unpaged_results": 1
        }
    }
}

# GET /f13/events_by_id.v1
# Example: GET /f13/events_by_id.v1?event_id_list=1GNCR
EVENTS_BY_ID_RESPONSE = {
    "events_by_id": {
        "1GNCR": {
            "event": {
                "area_code": "US",
                "city_code": "las_vegas-us",
                "city_desc": "Las Vegas",
                "classes": {
                    "activities": "Activities",
                    "attractions": "Attractions"
                },
                "country_code": "us",
                "country_desc": "United States of America",
                "custom_filter": [],
                "event_code": "K8vZ9171UAf",
                "event_desc": "Safetix Test product",
                "event_id": "1GNCR",
                "event_path": "/1GNCR-safetix-test-product/",
                "event_status": "live",
                "event_type": "simple_ticket",
                "event_uri_desc": "Safetix-Test-product",
                "geo_data": {
                    "latitude": 36.1207267,
                    "longitude": -115.1642896
                },
                "has_no_perfs": False,
                "is_add_on": False,
                "is_auto_quantity_add_on": False,
                "is_date_matched_add_on": False,
                "is_seated": True,
                "is_time_matched_add_on": False,
                "main_class_key": "activities",
                "need_departure_date": False,
                "need_duration": False,
                "need_performance": True,
                "postcode": "89169",
                "show_perf_time": True,
                "source_code": "ticketmaster_test",
                "source_desc": "ticketmaster test",
                "venue_code": "KovZ917Atbr",
                "venue_desc": "Sphere",
                "venue_uri_desc": "Sphere"
            },
            "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "venue_is_enforced": True
        }
    }
}
# GET /f13/months.v1
# Example: GET /f13/months.v1?event_id=1GNCR
MONTHS_RESPONSE = {
    "results": {
        "month": [
            {
                "month": "dec",
                "month_dates_bitmask": 1073741824,
                "month_desc": "December",
                "month_short_desc": "Dec",
                "month_weekdays_bitmask": 8,
                "year": 2025
            }
        ]
    }
}

# GET /f13/performances.v1
# Example: GET /f13/performances.v1?event_id=1GNCR&date=20251231
PERFORMANCES_RESPONSE = {
    "results": {
        "has_perf_names": False,
        "paging_status": {
            "page_length": 50,
            "page_number": 0,
            "pages_remaining": 0,
            "results_remaining": 0,
            "total_unpaged_results": 2
        },
        "performance": [
            {
                "cached_max_seats": 10,
                "cached_max_seats_is_real": True,
                "date_desc": "Wed, 31st December 2025",
                "event_id": "1GNCR",
                "has_pool_seats": True,
                "is_ghost": False,
                "is_limited": False,
                "iso8601_date_and_time": "2025-12-31T19:30:00-08:00",
                "perf_has_time": True,
                "perf_id": "1GNCR-4",
                "perf_is_visible": True,
                "time_desc": "7.30 PM"
            },
            {
                "cached_max_seats": 10,
                "cached_max_seats_is_real": True,
                "date_desc": "Wed, 31st December 2025",
                "event_id": "1GNCR",
                "has_pool_seats": True,
                "is_ghost": False,
                "is_limited": False,
                "iso8601_date_and_time": "2025-12-31T19:30:00-08:00",
                "perf_has_time": True,
                "perf_id": "1GNCR-5",
                "perf_is_visible": True,
                "time_desc": "7.30 PM"
            }
        ]
    }
}
# GET /f13/performances_by_id.v1
# Example: GET /f13/performances_by_id.v1?perf_id_list=1GNCR-5&req_avail_details=true
# This response is very large as it contains detailed ticket types and pricing
PERFORMANCE_DETAIL_RESPONSE = {
    "currency_details": {
        "usd": {
            "currency_code": "usd",
            "currency_factor": 100,
            "currency_number": 840,
            "currency_places": 2,
            "currency_post_symbol": "",
            "currency_pre_symbol": "$"
        }
    },
    "performances_by_id": {
        "1GNCR-5": {
            "avail_details": {
                "ticket_type": [
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "48/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "48",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "0",
                        "ticket_type_desc": "General Admission Standing Room"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.101",
                        "ticket_type_desc": "Main Level Seating: section 101"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.102",
                        "ticket_type_desc": "Main Level Seating: section 102"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.103",
                        "ticket_type_desc": "Main Level Seating: section 103"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.104",
                        "ticket_type_desc": "Main Level Seating: section 104"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.105",
                        "ticket_type_desc": "Main Level Seating: section 105"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.106",
                        "ticket_type_desc": "Main Level Seating: section 106"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.107",
                        "ticket_type_desc": "Main Level Seating: section 107"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.108",
                        "ticket_type_desc": "Main Level Seating: section 108"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.109",
                        "ticket_type_desc": "Main Level Seating: section 109"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "49/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "49",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "1.110",
                        "ticket_type_desc": "Main Level Seating: section 110"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "51/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "51",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.201",
                        "ticket_type_desc": "Terrace Level Seating: section 201"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.202",
                        "ticket_type_desc": "Terrace Level Seating: section 202"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.203",
                        "ticket_type_desc": "Terrace Level Seating: section 203"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.204",
                        "ticket_type_desc": "Terrace Level Seating: section 204"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.205",
                        "ticket_type_desc": "Terrace Level Seating: section 205"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.206",
                        "ticket_type_desc": "Terrace Level Seating: section 206"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.207",
                        "ticket_type_desc": "Terrace Level Seating: section 207"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.208",
                        "ticket_type_desc": "Terrace Level Seating: section 208"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.209",
                        "ticket_type_desc": "Terrace Level Seating: section 209"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 289.0,
                                        "suffixed_price_band_code": "50/pool",
                                        "surcharge": 106.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "50",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.210",
                        "ticket_type_desc": "Terrace Level Seating: section 210"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "51/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "51",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "2.211",
                        "ticket_type_desc": "Terrace Level Seating: section 211"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "54/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "54",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.301",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 301"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "54/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "54",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.302",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 302"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.303",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 303"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.304",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 304"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.305",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 305"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.306",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 306"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.307",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 307"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.308",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 308"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 215.0,
                                        "suffixed_price_band_code": "52/pool",
                                        "surcharge": 80.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "52",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.309",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 309"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "54/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "54",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.310",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 310"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "54/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "54",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "3.311",
                        "ticket_type_desc": "Lower Gallery Level Seating: section 311"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.403",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 403"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "55/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "55",
                                "price_band_desc": ""
                            },
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.404",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 404"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "55/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "55",
                                "price_band_desc": ""
                            },
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.405",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 405"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "55/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "55",
                                "price_band_desc": ""
                            },
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.406",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 406"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "55/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "55",
                                "price_band_desc": ""
                            },
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.407",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 407"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 133.0,
                                        "suffixed_price_band_code": "55/pool",
                                        "surcharge": 62.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "55",
                                "price_band_desc": ""
                            },
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.408",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 408"
                    },
                    {
                        "price_band": [
                            {
                                "avail_detail": [
                                    {
                                        "approx_last_seen_iso8601_date_and_time": "2025-11-06T13:20:13Z",
                                        "avail_currency_code": "usd",
                                        "cached_number_available": 8,
                                        "discount_code": "00000B0E0001",
                                        "discount_desc": "INGR1",
                                        "discount_semantic_type": "standard",
                                        "seatprice": 99.0,
                                        "suffixed_price_band_code": "56/pool",
                                        "surcharge": 46.0,
                                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                                    }
                                ],
                                "price_band_code": "56",
                                "price_band_desc": ""
                            }
                        ],
                        "ticket_type_code": "4.409",
                        "ticket_type_desc": "Upper Gallery Level Seating: section 409"
                    }
                ]
            },
            "cached_max_seats": 1000000,
            "cached_max_seats_is_real": False,
            "date_desc": "Wed, 31st December 2025",
            "event_id": "1GNCR",
            "has_pool_seats": True,
            "is_ghost": False,
            "is_limited": False,
            "iso8601_date_and_time": "2025-12-31T19:30:00-08:00",
            "perf_has_time": True,
            "perf_id": "1GNCR-5",
            "perf_is_visible": True,
            "time_desc": "7.30 PM"
        }
    }
}
# GET /f13/availability.v1
# Example: GET /f13/availability.v1?perf_id=1GNCR-5
# This response contains availability and pricing details for the performance
# Note: This is a simplified version with a few ticket types for brevity
AVAILABILITY_RESPONSE = {
    "availability": {
        "ticket_type": [
            {
                "price_band": [
                    {
                        "absolute_saving": 0.0,
                        "allows_leaving_single_seats": "never",
                        "discount_code": "00000B0E0001",
                        "discount_desc": "INGR1",
                        "discount_semantic_type": "standard",
                        "is_offer": False,
                        "max_order_no_of_seats": 8,
                        "min_order_no_of_seats": 1,
                        "non_offer_sale_combined": 395.0,
                        "non_offer_sale_seatprice": 289.0,
                        "non_offer_sale_surcharge": 106.0,
                        "number_available": 4,
                        "percentage_saving": 0,
                        "price_band_code": "49/pool",
                        "sale_combined": 395.0,
                        "sale_seatprice": 289.0,
                        "sale_surcharge": 106.0,
                        "unsuffixed_price_band_code": "49",
                        "valid_quantities": [1, 2, 3, 4]
                    }
                ],
                "ticket_type_code": "1.109",
                "ticket_type_desc": "Main Level Seating: section 109"
            },
            {
                "price_band": [
                    {
                        "absolute_saving": 0.0,
                        "allows_leaving_single_seats": "never",
                        "discount_code": "00000B0E0001",
                        "discount_desc": "INGR1",
                        "discount_semantic_type": "standard",
                        "is_offer": False,
                        "max_order_no_of_seats": 8,
                        "min_order_no_of_seats": 1,
                        "non_offer_sale_combined": 295.0,
                        "non_offer_sale_seatprice": 215.0,
                        "non_offer_sale_surcharge": 80.0,
                        "number_available": 8,
                        "percentage_saving": 0,
                        "price_band_code": "48/pool",
                        "sale_combined": 295.0,
                        "sale_seatprice": 215.0,
                        "sale_surcharge": 80.0,
                        "unsuffixed_price_band_code": "48",
                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                    }
                ],
                "ticket_type_code": "0",
                "ticket_type_desc": "General Admission Standing Room"
            },
            {
                "price_band": [
                    {
                        "absolute_saving": 0.0,
                        "allows_leaving_single_seats": "never",
                        "discount_code": "00000B0E0001",
                        "discount_desc": "INGR1",
                        "discount_semantic_type": "standard",
                        "is_offer": False,
                        "max_order_no_of_seats": 8,
                        "min_order_no_of_seats": 1,
                        "non_offer_sale_combined": 195.0,
                        "non_offer_sale_seatprice": 133.0,
                        "non_offer_sale_surcharge": 62.0,
                        "number_available": 8,
                        "percentage_saving": 0,
                        "price_band_code": "54/pool",
                        "sale_combined": 195.0,
                        "sale_seatprice": 133.0,
                        "sale_surcharge": 62.0,
                        "unsuffixed_price_band_code": "54",
                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                    }
                ],
                "ticket_type_code": "3.302",
                "ticket_type_desc": "Lower Gallery Level Seating: section 302"
            },
            {
                "price_band": [
                    {
                        "absolute_saving": 0.0,
                        "allows_leaving_single_seats": "never",
                        "discount_code": "00000B0E0001",
                        "discount_desc": "INGR1",
                        "discount_semantic_type": "standard",
                        "is_offer": False,
                        "max_order_no_of_seats": 8,
                        "min_order_no_of_seats": 1,
                        "non_offer_sale_combined": 145.0,
                        "non_offer_sale_seatprice": 99.0,
                        "non_offer_sale_surcharge": 46.0,
                        "number_available": 8,
                        "percentage_saving": 0,
                        "price_band_code": "56/pool",
                        "sale_combined": 145.0,
                        "sale_seatprice": 99.0,
                        "sale_surcharge": 46.0,
                        "unsuffixed_price_band_code": "56",
                        "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
                    }
                ],
                "ticket_type_code": "4.403",
                "ticket_type_desc": "Upper Gallery Level Seating: section 403"
            }
        ]
    },
    "backend_is_broken": False,
    "backend_is_down": False,
    "backend_throttle_failed": False,
    "can_select_seats": False,
    "contiguous_seat_selection_only": True,
    "currency_code": "usd",
    "currency_details": {
        "usd": {
            "currency_code": "usd",
            "currency_factor": 100,
            "currency_number": 840,
            "currency_places": 2,
            "currency_post_symbol": "",
            "currency_pre_symbol": "$"
        }
    },
    "max_bundle_size": 1,
    "must_select_whole_seat_block": False,
    "source_code": "ticketmaster_test",
    "valid_quantities": [1, 2, 3, 4, 5, 6, 7, 8]
}
# POST /f13/reserve.v1
# Example: POST /f13/reserve.v1 with form data
RESERVE_RESPONSE = {
    "allowed_countries": {
        "uk": "United Kingdom"
    },
    "can_edit_address": True,
    "currency_details": {
        "usd": {
            "currency_code": "usd",
            "currency_factor": 100,
            "currency_number": 840,
            "currency_places": 2,
            "currency_post_symbol": "",
            "currency_pre_symbol": "$"
        }
    },
    "input_contained_unavailable_order": False,
    "language_list": ["en"],
    "minutes_left_on_reserve": 4.95,
    "needs_agent_reference": False,
    "needs_email_address": False,
    "needs_payment_card": False,
    "prefilled_address": {
        "country_code": "uk"
    },
    "reserve_iso8601_date_and_time": "2025-11-06T15:36:50Z",
    "transaction_status": "reserved",
    "trolley_contents": {
        "bundle": [
            {
                "bundle_order_count": 1,
                "bundle_send_cost_tax_component": 0.0,
                "bundle_source_code": "ticketmaster_test",
                "bundle_source_desc": "ticketmaster test",
                "bundle_total_cost": 790.0,
                "bundle_total_seatprice": 578.0,
                "bundle_total_send_cost": 0.0,
                "bundle_total_surcharge": 212.0,
                "bundle_total_trans_fee_component": 0.0,
                "bundle_trans_fee_tax_sub_component": 0.0,
                "currency_code": "usd",
                "max_bundle_size": 1,
                "order": [
                    {
                        "discounts_were_altered": "yes",
                        "event": {
                            "area_code": "US",
                            "city_code": "las_vegas-us",
                            "city_desc": "Las Vegas",
                            "classes": {
                                "activities": "Activities",
                                "attractions": "Attractions"
                            },
                            "country_code": "us",
                            "country_desc": "United States of America",
                            "custom_filter": [],
                            "event_code": "K8vZ9171UAf",
                            "event_desc": "Safetix Test product",
                            "event_id": "1GNCR",
                            "event_path": "/1GNCR-safetix-test-product/",
                            "event_status": "live",
                            "event_type": "simple_ticket",
                            "event_uri_desc": "Safetix-Test-product",
                            "geo_data": {
                                "latitude": 36.1207267,
                                "longitude": -115.1642896
                            },
                            "has_no_perfs": False,
                            "is_add_on": False,
                            "is_auto_quantity_add_on": False,
                            "is_date_matched_add_on": False,
                            "is_seated": True,
                            "is_time_matched_add_on": False,
                            "main_class_key": "activities",
                            "need_departure_date": False,
                            "need_duration": False,
                            "need_performance": True,
                            "postcode": "89169",
                            "show_perf_time": True,
                            "source_code": "ticketmaster_test",
                            "source_desc": "ticketmaster test",
                            "venue_code": "KovZ917Atbr",
                            "venue_desc": "Sphere",
                            "venue_uri_desc": "Sphere"
                        },
                        "extra_data_items": {
                            "per_order": [],
                            "per_seat": []
                        },
                        "internal_reserve_sub_ref": "",
                        "internal_reserve_sub_ref2": "",
                        "item_number": 1,
                        "max_order_no_of_seats": 8,
                        "min_order_no_of_seats": 1,
                        "performance": {
                            "cached_max_seats": 1000000,
                            "cached_max_seats_is_real": False,
                            "date_desc": "Wed, 31st December 2025",
                            "event_id": "1GNCR",
                            "has_pool_seats": True,
                            "is_ghost": False,
                            "is_limited": False,
                            "iso8601_date_and_time": "2025-12-31T19:30:00-08:00",
                            "perf_has_time": True,
                            "perf_id": "1GNCR-5",
                            "perf_is_visible": True,
                            "time_desc": "7.30 PM"
                        },
                        "price_band_code": "49/pool",
                        "requested_seat_ids": [],
                        "seat_request_status": "not_requested",
                        "send_method": {
                            "can_generate_self_print": True,
                            "has_html_page": True,
                            "send_code": "MOBILE",
                            "send_cost": 0.0,
                            "send_cost_tax_component": 0.0,
                            "send_desc": "To access your tickets for entry, you'll need to download the Ticketmaster App or add your tickets to your mobile wallet.",
                            "send_type": "selfprint",
                            "trans_fee_component": 0.0,
                            "trans_fee_tax_sub_component": 0.0
                        },
                        "ticket_orders": {
                            "ticket_order": [
                                {
                                    "discount_code": "00000B0E0001",
                                    "discount_desc": "INGR1",
                                    "discount_semantic_type": "standard",
                                    "no_of_seats": 2,
                                    "sale_combined": 395.0,
                                    "sale_seatprice": 289.0,
                                    "sale_surcharge": 106.0,
                                    "seats": [
                                        {
                                            "col_id": "4",
                                            "full_id": "12.4",
                                            "is_restricted_view": False,
                                            "row_id": "12",
                                            "seat_unique_ref": "S-0WU6EHZV",
                                            "separator": "."
                                        },
                                        {
                                            "col_id": "3",
                                            "full_id": "12.3",
                                            "is_restricted_view": False,
                                            "row_id": "12",
                                            "seat_unique_ref": "S-XWTK08X4",
                                            "separator": "."
                                        }
                                    ],
                                    "total_sale_combined": 790.0,
                                    "total_sale_seatprice": 578.0,
                                    "total_sale_surcharge": 212.0
                                }
                            ]
                        },
                        "ticket_type_code": "1.110",
                        "ticket_type_desc": "Main Level Seating: section 110",
                        "total_no_of_seats": 2,
                        "total_sale_combined": 790.0,
                        "total_sale_seatprice": 578.0,
                        "total_sale_surcharge": 212.0,
                        "trans_type": "affiliate",
                        "unsuffixed_price_band_code": "49",
                        "was_auto_modified": "no"
                    }
                ]
            }
        ],
        "transaction_uuid": "U-76A897A0-3906-4F4C-AD1E-7C6E9694EFFD-F64986C7-LDNX",
        "trolley_bundle_count": 1,
        "trolley_order_count": 1
    },
    "unreserved_orders": []
}

# In-memory storage for reservations
RESERVATIONS = {}

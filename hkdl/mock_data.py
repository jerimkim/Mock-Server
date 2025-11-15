"""
Mock data for Disney HK Mock Server
All data is based on the official API documentation
"""

# GetEvents response
EVENTS_RESPONSE = {
    "responseCode": "0000",
    "events": [
        {
            "eventId": "34",
            "name": {
                "en": "1-DAY TICKET (DESIGNATED DAY)",
                "tc": "1 日門票 (特選日子)",
                "sc": "1 日门票 (特选日子)"
            },
            "remark": {
                "en": "",
                "tc": "",
                "sc": ""
            },
            "eventType": "S",
            "orderType": "FIT",
            "reqGuestName": "Y",
            "cancellable": "Y",
            "minTicket": 1,
            "maxTicket": 14,
            "seq": 1
        },
        {
            "eventId": "36",
            "name": {
                "en": "2-DAY TICKET",
                "tc": "2 日門票",
                "sc": "2 日门票"
            },
            "remark": {
                "en": "This voucher is valid until March 31, 2014.\n2-Day Tickets are valid for visit on any 2 days within a 7-day period.",
                "tc": "此換票証有效至 2014 年 3 月 31 日。\n2 日門票可於 7 日內任何兩天進入樂園。",
                "sc": "此换票证有效至 2014 年 3 月 31 日。\n2 日门票可于 7 日内任何两天进入乐园。"
            },
            "eventType": "R",
            "orderType": "TG",
            "reqGuestName": "N",
            "cancellable": "N",
            "minTicket": 15,
            "maxTicket": 700,
            "seq": 2
        }
    ]
}

# GetShows response
SHOWS_RESPONSE = {
    "responseCode": "0000",
    "shows": [
        {
            "showId": 79,
            "showDateTime": "2013-10-01 10:00",
            "cutoffDateTime": "2013-09-30 16:00"
        },
        {
            "showId": 80,
            "showDateTime": "2013-10-02 10:00",
            "cutoffDateTime": "2013-10-01 16:00"
        }
    ]
}

# GetTickets response
TICKETS_RESPONSE = {
    "responseCode": "0000",
    "tickets": [
        {
            "ticketId": "13",
            "name": {
                "en": "1-DAY GENERAL ADMISSION / DESIGNATED DAY (AGED 12-64)",
                "tc": "1 日標準門票 / 特選日子 (12-64 歲)",
                "sc": "1 日标准门票 / 特选日子 (12-64 岁)"
            },
            "ticketType": {
                "en": "Adult",
                "tc": "成人",
                "sc": "成人"
            },
            "ticketPrice": 348.0,
            "seq": 1
        },
        {
            "ticketId": "14",
            "name": {
                "en": "1-DAY CHILD / DESIGNATED DAY (AGED 3-11)",
                "tc": "1 日小童門票 / 特選日子 (3-11 歲)",
                "sc": "1 日小童门票 / 特选日子 (3-11 岁)"
            },
            "ticketType": {
                "en": "Child",
                "tc": "小童",
                "sc": "小童"
            },
            "ticketPrice": 250.0,
            "seq": 2
        },
        {
            "ticketId": "15",
            "name": {
                "en": "1-DAY SENIOR / DESIGNATED DAY (AGED 65 OR ABOVE)",
                "tc": "1 日長者門票 / 特選日子 (65 歲或以上)",
                "sc": "1 日长者门票 / 特选日子 (65 岁或以上)"
            },
            "ticketType": {
                "en": "Senior",
                "tc": "長者",
                "sc": "长者"
            },
            "ticketPrice": 90.0,
            "seq": 3
        }
    ]
}

# GetPickupDetails response
PICKUP_DETAILS_RESPONSE = {
    "responseCode": "0000",
    "pickupDetails": [
        {
            "pickupId": 1,
            "name": {
                "en": "GUEST SELF PICKUP (VOUCHER)",
                "tc": "賓客自取 (換領憑證)",
                "sc": "宾客自取 (换领凭证)"
            },
            "minQty": 1,
            "pickupDelay": 0,
            "pickupPeriod": 30,
            "cutoffTime": "0000",
            "seq": 6
        },
        {
            "pickupId": 13,
            "name": {
                "en": "ETICKET (PDF)",
                "tc": "電子票 (PDF 檔)",
                "sc": "电子票 (PDF 檔)"
            },
            "minQty": 1,
            "pickupDelay": 0,
            "pickupPeriod": 30,
            "cutoffTime": "0000",
            "seq": 9
        },
        {
            "pickupId": 12,
            "name": {
                "en": "ETICKET (HYPERLINK)",
                "tc": "電子票 (超連結)",
                "sc": "电子票 (超链接)"
            },
            "minQty": 1,
            "pickupDelay": 0,
            "pickupPeriod": 30,
            "cutoffTime": "0000",
            "seq": 9
        }
    ]
}

# ReserveOrder response
RESERVE_ORDER_RESPONSE = {
    "responseCode": "0000",
    "reservationNo": "1234567890",
    "voucherNo": "00123-CL-001002003",
    "detail": {
        "totalAmount": 1180.0,
        "qrCode": "85255141519173710903",
        "thirdPartyQRCodes": [
            {
                "qrCodeGroupDescrption": "busComp1",
                "qrCode": [
                    "QRCODE1_6",
                    "QRCODE1_7",
                    "QRCODE1_8",
                    "QRCODE1_4",
                    "QRCODE1_3",
                    "QRCODE1_2"
                ]
            },
            {
                "qrCodeGroupDescrption": "busComp2",
                "qrCode": [
                    "QRCODE2_1",
                    "QRCODE2_2",
                    "QRCODE2_3",
                    "QRCODE2_4",
                    "QRCODE2_5",
                    "QRCODE2_6"
                ]
            }
        ],
        "transactionDate": "2013-09-28 22:50:30",
        "guestName": "CHAN TAI MAN",
        "event": {
            "en": "1-DAY TICKET (DESIGNATED DAY)",
            "tc": "1日門票 (特選日子)",
            "sc": "1日门票 (特选日子)"
        },
        "remark": {
            "en": "",
            "tc": "",
            "sc": ""
        },
        "showDateTime": "2013-10-01 10:00",
        "pickupMethod": {
            "en": "GUEST SELF PICKUP (VOUCHER)",
            "tc": "賓客自取 (換領憑證)",
            "sc": "宾客自取 (换领凭证)"
        },
        "pickupDate": "2013-12-31",
        "items": [
            {
                "name": {
                    "en": "1-DAY CHILD / DESIGNATED DAY (AGED 3-11)",
                    "tc": "1日小童門票 / 特選日子 (3-11歲)",
                    "sc": "1日小童门票 / 特选日子 (3-11岁)"
                },
                "ticketCode": "AGW45",
                "quantity": 4,
                "subtotalAmount": 1000.0
            },
            {
                "name": {
                    "en": "1-DAY SENIOR / DESIGNATED DAY (AGED 65 OR ABOVE)",
                    "tc": "1日長者門票 / 特選日子 (65歲或以上)",
                    "sc": "1日长者门票 / 特选日子 (65岁或以上)"
                },
                "ticketCode": "AGW55",
                "quantity": 2,
                "subtotalAmount": 180.0
            }
        ]
    },
    "confirmationLetter": "JVBERi0xLjQNJeLjz9MNCjcgMCBvYmoNPDwvT",
    "eticketUrl": "https://example.com/eticket/00002548"
}

# CancelOrder response
CANCEL_ORDER_RESPONSE = {
    "responseCode": "0000"
}

# GetOrderStatus response (COMPLETED)
ORDER_STATUS_COMPLETED = {
    "responseCode": "0000",
    "status": "COMPLETED",
    "reservationNo": "1234567890",
    "voucherNo": "00123-CL-001002003",
    "detail": {
        "totalAmount": 1180.0,
        "qrCode": "85255141519173710903",
        "thirdPartyQRCodes": [
            {
                "qrCodeGroupDescrption": "busComp1",
                "qrCode": [
                    "QRCODE1_6",
                    "QRCODE1_7",
                    "QRCODE1_8",
                    "QRCODE1_4",
                    "QRCODE1_3",
                    "QRCODE1_2"
                ]
            },
            {
                "qrCodeGroupDescrption": "busComp2",
                "qrCode": [
                    "QRCODE2_1",
                    "QRCODE2_2",
                    "QRCODE2_3",
                    "QRCODE2_4",
                    "QRCODE2_5",
                    "QRCODE2_6"
                ]
            }
        ],
        "transactionDate": "2013-09-28 22:50:30",
        "guestName": "CHAN TAI MAN",
        "event": {
            "en": "1-DAY TICKET (DESIGNATED DAY)",
            "tc": "1日門票 (特選日子)",
            "sc": "1日门票 (特选日子)"
        },
        "remark": {
            "en": "",
            "tc": "",
            "sc": ""
        },
        "showDateTime": "2013-10-01 10:00",
        "pickupMethod": {
            "en": "GUEST SELF PICKUP (VOUCHER)",
            "tc": "賓客自取 (換領憑證)",
            "sc": "宾客自取 (换领凭证)"
        },
        "pickupDate": "2013-12-31",
        "items": [
            {
                "name": {
                    "en": "1-DAY CHILD / DESIGNATED DAY (AGED 3-11)",
                    "tc": "1日小童門票 / 特選日子 (3-11歲)",
                    "sc": "1日小童门票 / 特选日子 (3-11岁)"
                },
                "ticketCode": "AGW45",
                "quantity": 4,
                "subtotalAmount": 1000.0
            },
            {
                "name": {
                    "en": "1-DAY SENIOR / DESIGNATED DAY (AGED 65 OR ABOVE)",
                    "tc": "1日長者門票 / 特選日子 (65歲或以上)",
                    "sc": "1日长者门票 / 特选日子 (65岁或以上)"
                },
                "ticketCode": "AGW55",
                "quantity": 2,
                "subtotalAmount": 180.0
            }
        ]
    },
    "confirmationLetter": "JVBERi0xLjQNJeLjz9MNCjcgMCBvYmoNPDwvT",
    "eticketUrl": "https://example.com/eticket/00002548"
}

# GetOrderStatus response (NOT_FOUND)
ORDER_STATUS_NOT_FOUND = {
    "responseCode": "0000",
    "status": "NOT_FOUND"
}

# GetOrderStatus response (CANCEL_PENDING)
ORDER_STATUS_CANCEL_PENDING = {
    "responseCode": "0000",
    "status": "CANCEL_PENDING",
    "reservationNo": "1234567890",
    "voucherNo": "00123-CL-001002003"
}

# GetOrderStatus response (CANCELLED)
ORDER_STATUS_CANCELLED = {
    "responseCode": "0000",
    "status": "CANCELLED",
    "reservationNo": "1234567890",
    "voucherNo": "00123-CL-001002003"
}

# Store reservations in memory
RESERVATIONS = {}
CANCELLED_RESERVATIONS = set()

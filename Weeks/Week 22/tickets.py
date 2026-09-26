tickets = [
    {
        "id": 1,
        "status": "open",
        "total": 2500,
        "paid_at": None
    },
    {
        "id": 2,
        "status": "paid",
        "total": 1800,
        "paid_at": 1781000000
    },
    {
        "id": 3,
        "status": "cancelled",
        "total": 3200,
        "paid_at": None
    },
    {
        "id": 4,
        "status": "open",
        "total": 0,
        "paid_at": None
    }
]

orders = [
    {
        "id": 1,
        "status": "open",
        "items": [
            {"name": "Burger", "quantity": 2, "price": 1200},
            {"name": "Beer", "quantity": 3, "price": 700},
        ],
        "total": 4500,
        "paid_at": None,
    },
    {
        "id": 2,
        "status": "cancelled",
        "items": [
            {"name": "Pizza", "quantity": 1, "price": 1600}
        ],
        "total": 1600,
        "paid_at": None,
    },
]
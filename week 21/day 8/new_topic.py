#question 1 


menu_item_found = {
    "id": 58,
    "name": "Gin & Tonic",
    "inStock": True,
    "prices": {
        "standard": 800,
        "double": 1400,
    },
}

price_key = "double"
quantity = 2
prices = menu_item_found["prices"]


if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
        detail="Invalid price key")


selected_price = prices[price_key]


new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price_key": price_key,
    "quantity": quantity,
    "price": selected_price
}

print(new_ticket_item)








#question 2

ticket_found = {
    "id": 1,
    "name": "John",
    "status": "open",
    "items": [],
    "total": 0,
}

menu_item_found = {
    "id": 69,
    "name": "Japanese Whisky",
    "inStock": True,
    "prices": {
        "standard": 900,
        "15ml": 1000,
        "double": 1600,
    },
}

price_key = "15ml"
quantity = 3


prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
        detail="Invalid price key")

selected_price = prices[price_key]

new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price_key": price_key,
    "quantity": quantity,
    "price": selected_price

}


#confusion , we are not adding ticket to items , we are adding a new item to a ticket 


ticket_found["items"].append(new_ticket_item)

print(ticket_found)


#so result is



"items": [
    {
        "id": 69,
        "name": "Japanese Whisky",
        "price_key": "15ml",
        "quantity": 3,
        "price": 1000,
    }
]



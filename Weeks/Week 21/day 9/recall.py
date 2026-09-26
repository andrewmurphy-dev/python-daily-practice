#question 1 recall

ticket_found = {
    "id": 1,
    "name": "John",
    "status": "open",
    "items": [],
    "total": 0,
}

menu_item_found = {
    "id": 58,
    "name": "Gin & Tonic",
    "prices": {
        "standard": 800,
        "double": 1400,
    },
}

price_key = "double"
quantity = 2

prices = menu_item_found ["prices"]
if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
        detail="Invalid price key")


selected_price = prices[price_key]


new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price_key": price_key,
    "price": selected_price
}

ticket_found["items"].append(new_ticket_item)

line_total = selected_price * quantity

print(ticket_found)
print(line_total)



#question 2 

ticket_found = {
    "id": 2,
    "name": "Sarah",
    "status": "open",
    "items": [],
    "total": 500,
}

menu_item_found = {
    "id": 69,
    "name": "Japanese Whisky",
    "prices": {
        "standard": 900,
        "15ml": 1000,
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
    "price": selected_price,
    "price_key": price_key,
    "quantity": quantity
}

print(new_ticket_item)

line_total = selected_price * quantity

print(line_total)


ticket_found["items"].append(new_ticket_item)

print(ticket_found)


#question 3

ticket_found = {
    "id": 3,
    "name": "Mike",
    "status": "open",
    "items": [
        {
            "id": 10,
            "name": "Cover Charge",
            "price_key": "standard",
            "quantity": 1,
            "price": 500,
        }
    ],
    "total": 500,
}

menu_item_found = {
    "id": 71,
    "name": "Asahi Beer",
    "prices": {
        "standard": 800,
        "large": 1100,
    },
}

price_key = "large"
quantity = 2

prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
        detail="Invalid price key")

selected_price = prices[price_key]

line_total = selected_price * quantity 

new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price": selected_price,
    "price_key": price_key,
    "quantity": quantity
}

ticket_found["items"].append(new_ticket_item)

print(new_ticket_item)
print(line_total)
print(ticket_found)
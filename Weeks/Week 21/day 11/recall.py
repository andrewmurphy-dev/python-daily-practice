#question 1 


ticket_found = {
    "id": 10,
    "name": "James",
    "status": "open",
    "items": [],
    "total": 500,
}

menu_item_found = {
    "id": 69,
    "name": "Glenfiddich 18 Year",
    "prices": {
        "15ml": 1000,
        "30ml": 2000,
    },
}

price_key = "30ml"
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
    "price_key": price_key,
    "quantity": quantity,
    "price": selected_price

}

ticket_found["items"].append(new_ticket_item)
ticket_found["total"] += line_total

print(ticket_found)


#question 2



ticket_found = {
    "id": 11,
    "name": "Anna",
    "status": "open",
    "items": [
        {
            "id": 1,
            "name": "Cover Charge",
            "price_key": "standard",
            "quantity": 1,
            "price": 500,
        }
    ],
    "total": 500,
}

menu_item_found = {
    "id": 73,
    "name": "Speyburn 18 Year",
    "prices": {
        "15ml": 1300,
        "30ml": 2500,
    },
}

price_key = "15ml"
quantity = 3




prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
            detail="Invalid price key")

selected_price = prices[price_key]
line_total = selected_price * quantity


new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price_key": price_key,
    "quantity": quantity,
    "price": selected_price
}

ticket_found["items"].append(new_ticket_item)
ticket_found["total"] += line_total

print(ticket_found)
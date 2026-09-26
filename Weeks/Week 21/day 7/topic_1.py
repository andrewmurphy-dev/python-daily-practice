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

price_key = "standard"
quantity = 3


prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST, detail="Invalid price key")


selected_price = prices[price_key]


result = {
    "name": menu_item_found["name"]
    "price_key": "standard",
    "selected_price": selected_price
    "quantity": quanitity
}

print(result)




#question 2 




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
quantity = 2


prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST, detail="Invalid price key")

selected_price = prices[price_key]


result = {
    "name": menu_item_found["name"],
    "price_key": price_key,
    "selected_price": selected_price,
    "quantity": quantity
}


print(result)
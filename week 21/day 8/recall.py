#question 1 


menu_item_found = {
    "id": 69,
    "name": "Japanese Whisky",
    "prices": {
        "standard": 900,
        "15ml": 1000,
    },
}

price_key = "15ml"
prices = menu_item_found["prices"]


if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST,
        detail="Invalid price key",)



selected_price = prices[price_key]

result = {
    "name": menu_item_found["name"],
    "selected_price": selected_price,
    "price_key": price_key
}

print(result)


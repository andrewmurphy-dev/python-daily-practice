
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
selected_price = None

if price_key in prices:
    selected_price = prices[price_key]
    print(selected_price)
    print("price key is valid")


else:
    print("invalid price key")





#question 2 


if price_key not in prices:
    print("invalid price key")

else:
    selected_price = prices[price_key]
    print(selected_price)
    print("price key is valid")



#question 3 


prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(http.status.HTTP_400_BAD_REQUEST, detail="Invalid price key")

else:
     selected_price = prices[price_key]
     print(selected_price)
     print("price key is valid")


#You do not need else. Once raise HTTPException(...) runs, the endpoint stops immediately.


if price_key not in prices:
    raise HTTPException(status_code=http.status.HTTP_400_BAD_REQUEST, detail="Invalid price key")

selected_prices = prices[price_key]





#question 4 

#Add the price-validation logic to this endpoint section, then include selected_price in the temporary return:

if not menu_item_found["inStock"]:
    raise HTTPException(
        status_code=http_status.HTTP_409_CONFLICT,
        detail="Menu item is out of stock!",
    )

prices = menu_item_found["prices"]

if not price_key in prices:
    raise HTTPException(status_code=http_status.HTTP_400_CONFLICT, detail="price key not found")

selected_price = prices[price_key]

return {
    "menu_item": menu_item_found,
    "price_key": price_key,
    "quantity": quantity,
    "selected_price": selected_price
}

#question 5

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

price = menu_item_found["prices"]

if not price_key in price:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST, detail="price key not found")

selected_price = price[price_key]


result = 
{
    "name": menu_item_found["name"],
    "price_key": "double",
    "selected_price": 1400,
    "quantity": 2

}

print(result)

#question 6 

menu_item_found = {
    "id": 69,
    "name": "Japanese Whisky",
    "inStock": True,
    "prices": {
        "standard": 900,
        "15ml": 1000,
    },
}

price_key = "double"
quantity = 3


prices = menu_item_found["prices"]

if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST, detail="price key not found")


selected_price = prices[price_key]


result = {
    "name": menu_item_found["name"],
    "price_key": "double",
    "selected_price": 
    "quanity": 3
}


print(result)
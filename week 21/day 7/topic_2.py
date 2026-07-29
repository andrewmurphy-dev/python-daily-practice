#here we are doing line total ! calculations 

#line_total = selected_price * quantity 



#Question 1

#Use the same code, but:

#calculate line_total
#add "line_total" to the result dictionary
#print the result

#Do not change any other logic.



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

line_total = selected_price * quantity


result = {
    "name": menu_item_found["name"],
    "quantity": quantity,
    "selected_price": selected_price,
    "line_total": line_total,
    "price_key": price_key 
}

print(result)







#question 2 





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
quantity = 3
prices = menu_item_found["prices"]


if price_key not in prices:
    raise HTTPException(status_code=http_status.HTTP_400_BAD_REQUEST, detail="Invalid price key")


selected_price = prices[price_key]

line_total = selected_price * quantity


result = {
    "name": menu_item_found["name"],
    "price_key": price_key,
    "selected_price": selected_price,
    "quantity": quantity,
    "line_total": line_total 
}


print(result)






















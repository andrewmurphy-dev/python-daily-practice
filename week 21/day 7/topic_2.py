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
    raise HTTPException(status_code=http_status=HTTP_400_BAD_REQUEST, detail="Invalid price key")

selected_price = prices[price_key]

total_price = selected_price * quantity


result = {
    "name": 
}
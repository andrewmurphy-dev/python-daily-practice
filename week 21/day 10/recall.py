#question 1 

ticket_found = {
    "id": 1,
    "name": "John",
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
    "id": 58,
    "name": "Old Glasgow",
    "inStock": True,
    "prices": {
        "standard": 800,
    },
}

price_key = "standard"
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

print(ticket_found)
print(line_total)


#question 2 
#Using the same code, add one line that changes the ticket total from 500 to 2100 



selected_price_1 = ticket_found[0]["price"]
selected_price_2 = ticket_found[1]["price"]

item_total = selected_price_1 + selected_price_2

new_ticket_item["items"]["total"].append(item_total)


print(new_ticket_item)


#this is wrong 

ticket_found["items"].append(new_ticket_item)

ticket_found["total"] += line_total

print(ticket_found)


#remmeber this 

selected_price = prices[price_key]

price_key = "standard"

line_total = selected_price * quantity 

#so we go through id 1 , see the price key and line total and we see the next id and do the same again



#question 3

ticket_found = {
    "id": 4,
    "name": "Sarah",
    "status": "open",
    "items": [],
    "total": 0,
}

menu_item_found = {
    "id": 75,
    "name": "Macallan 12 Year",
    "prices": {
        "15ml": 1000,
        "30ml": 2000,
    },
}

price_key = "30ml"
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



#question 4 


ticket_found = {
    "id": 5,
    "name": "David",
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
quantity = 2

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

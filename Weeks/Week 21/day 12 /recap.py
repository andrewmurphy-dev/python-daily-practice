#question 1 


ticket_found = {
    "items": [
        {
            "id": 73,
            "name": "Speyburn 18 Year",
            "price_key": "15ml",
            "quantity": 2,
            "price": 1300,
        },
        {
            "id": 49,
            "name": "Jameson",
            "price_key": "standard",
            "quantity": 1,
            "price": 800,
        }
    ]
}

menu_item_found = {
    "id": 73,
    "name": "Speyburn 18 Year",
}

price_key = "15ml"
quantity = 2

existing_item = None


for item in ticket_found["items"]:
    if item["id"] == menu_item_found["id"] and item["price_key"] == price_key:
        existing_item = item
        break 


if existing_item is not None:
    existing_item["quantity"] += quantity 

print(existing_item)


#question 2 



ticket_found = {
    "items": [
        {
            "id": 73,
            "name": "Speyburn 18 Year",
            "price_key": "15ml",
            "quantity": 2,
            "price": 1300,
        }
    ]
}

menu_item_found = {
    "id": 73,
    "name": "Speyburn 18 Year",
}

price_key = "30ml"
quantity = 1

existing_item = None


#searches for a matching id and price_key
#stores it in existing_item if found
#uses break
#safely checks whether existing_item was found
#prints existing_item


for item in ticket_found["items"]:
    if item["id"] == menu_item_found["id"] and item["price_key"] == price_key:
        existing_item = item 
        break

if existing_item is not None:
    existing_item["quantity"] += quantity

print(existing_item)
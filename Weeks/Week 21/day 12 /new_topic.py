#New Topic — If No Match, Append a New Item

#existing item found
#→ update quantity

#no existing item found
#→ create new_ticket_item
#→ append it"


#question 1


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

else:
    new_ticket_item = {
        "id": menu_item_found["id"],
        "name": menu_item_found["name"],
        "price_key": price_key,
        "quantity": quantity,
        "price": selected_price

    }

ticket_found["items"].append(new_ticket_item)

print(ticket_found)



#the logic we just built was this ! 

#IF same item + same price_key exists
#→ increase its quantity

#ELSE
#→ create a new item dictionary
#→ append it


#find an existing matching ticket item 


#right now everytime someone orders something we do 


#ticket_found["items"].append(new_ticket_item)


#But what if the exact same item is already there?

#for example


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


#then customer orders 

#menu_item_found["id"] = 73
#price_key = "15ml"
#quantity = 1


#we do not want 

[
    {"id": 73, "price_key": "15ml", "quantity": 2},
    {"id": 73, "price_key": "15ml", "quantity": 1}
]


#we want 


[
    {"id": 73, "price_key": "15ml", "quantity": 3}
]




#so step 1

#we need to find whether a macthing line already exists 


#so we need a match of "id", "price_key"




#example questions 



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




existing_item = None

for item in ticket_found["items"]:
    if item["id"] == menu_item_found["id"] and item["price_key"] == price_key:
        existing_item = item 
        break

print(existing_item)



#confusion how do we store two sepetate things into the "existing_item"

#think about it , we technically are not because , we have price_key in the item dict 

#check TWO properties
#        ↓
#find ONE matching dictionary
#        ↓
#existing_item = item


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

price_key = "15ml"
quantity = 3

existing_item = None



for item in ticket_found["items"]:
    if item["id"] == menu_item_found["id"] and item["price_key"] == price_key:
        existing_item = item 


existing_item["quantity"]  += quantity 

print(existing_item)




#better way to write this is:


if existing_item is not None:
    existing_item["quantity"]  += quantity 

print(existing_item)



#if price key is different it would be a seperate object!


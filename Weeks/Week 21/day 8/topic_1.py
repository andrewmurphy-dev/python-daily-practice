#stop manually writing 

price_key = "standard"
quantity = 2 


#instead we get those values from the pydantic request ! 


#price_key = request.price_key
#quantity = request.quantity
#menu_item_id = request.menu_item_id



#question 1 

#Assume this request model already exists:

class AddTicketItemRequest(BaseModel):
    menu_item_id: int
    price_key: str
    quantity: int



#the front end sends this 

{
  "menu_item_id": 75,
  "price_key": "30ml",
  "quantity": 2
}



#Write three lines that create:


menu_item_id = request.menu_item_id
price_key = request.price_key
quantity = request.quantity 






#question 2 



request = AddTicketItemRequest(
    menu_item_id=75,
    price_key="30ml",
    quantity=2
)

menu_item_found = {
    "id": 75,
    "name": "Macallan 12 Year",
    "prices": {
        "15ml": 1000,
        "30ml": 2000,
    },
}


#Write code that:

#Reads price_key and quantity from request
#Gets the nested prices dictionary
#Raises 400 Bad Request if the price key is invalid
#Creates selected_price
#Calculates line_total
#Prints selected_price and line_total


price_key = request.price_key
quantity = request.quantity
prices = menu_item_found["prices"]


if price_key not in prices:
    raise HTTPexception(status_code=http_status=HTTP_400_BAD_REQUEST, detail="Invalid price key")

selected_price = prices[price_key]

line_total = selected_price * quantity 


print(selected_price)
print(line_total)



#Question 3 — Create and Update the Ticket


ticket_found = {
    "id": 8,
    "name": "Emma",
    "status": "open",
    "items": [],
    "total": 0,
}

menu_item_found = {
    "id": 75,
    "name": "Macallan 12 Year",
}

price_key = "30ml"
quantity = 2
selected_price = 2000
line_total = 4000



#Write code that:

#Creates new_ticket_item containing:
#id
#name
#price_key
#quantity
#price
#Appends it to ticket_found["items"]
#Adds line_total to ticket_found["total"]
#Prints the updated ticket



prices = menu_item_found["prices"]

if price_key not in prices:
    raise  HTTPException(http.status.HTTP_400_BAD_REQUEST, detail="Invalid price key")


selected_price = prices[price_key]

total_price = selected_price * quantity 

new_ticket_item = {
    "id": menu_item_found["id"],
    "name": menu_item_found["name"],
    "price_key": price_key,
    "quantity": quantity,
    "price": selected_price
}

ticket_found["items"].append(new_ticket_item)
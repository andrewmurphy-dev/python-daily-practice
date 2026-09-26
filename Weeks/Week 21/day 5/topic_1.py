#practice question 1 



menu_item_found = {
    "id": 58,
    "name": "Gin & Tonic",
    "inStock": True,
    "prices": {
        "standard": 800,
        "double": 1400,
    },
}



#question 1 
#Write one line of code that stores the entire prices dictionary inside a variable called prices.



#rices = []


#for price in menu_item_found:
#you do not need !   
#because you are not searching through multiple items. You already have one menu item, and you know the exact key you need.


prices = menu_item_found["prices"]

print(prices)


#question 2 

item_name = menu_item_found["name"]
print(item_name)


#question 3 


is_in_stock = menu_item_found["inStock"]

print(is_in_stock)



#question 4 


## Next question

#Using:

#```python
#price_key = "standard"
##prices = menu_item_found["prices"]
#``

#Write an `if` statement that:

#* Prints `"Valid price key"` if `price_key` exists in `prices`
#* Otherwise prints `"Invalid price key"`


price_key = "standard"
prices = menu_item_found["prices"]

for price in menu_item_found:
    if price_key in prices:
        print("Valid price key")

else:
    print("Invalid price key")




#you did not need a loop here 
#you already have one dictionary 


#question 5


price_key = "15ml"
prices = menu_item_found["prices"]


if price_key in prices:
    print("Valid price key")

else:
    print("Invalid price key")



#question 6 



price_key = "standard"
prices = menu_item_found["prices"]
selected_price = []

#When the key is valid, store its price inside a variable called selected_price, then print selected_price.

if price_key in price:
    selected_price.append(price_key)

print(selected_price)

#would store "standard", but we want the value connected to "standard".


#see price key is an integer 

#why did we go selected_price = None , why not a list

#its supposed to hold 1 price , not a intger 


#selected_price = None

#No valid price has been selected yet



#so the solution is 

if price_key in price:
    selected_price = prices[price_key]

print(selected_price)




#question 7


## Next question

Use:

#```python
prices = {
    "standard": 800,
    "double": 1400,
}

#price_key = "double"
#```

#Write code that:

#* Checks whether `price_key` exists in `prices`
#* Stores the matching price in `selected_price`
#* Prints `selected_price`
#* Otherwise prints `"Invalid price key"`


prices = {
    "standard": 800,
    "double": 1400,
}


price_key = "double"

selected_price = None

if price_key in prices:
    selected_price = prices[price_key]
    print(selected_price)
    
else:
    print("invalid price key")



#question 8

prices = {
    "standard": 800,
    "double": 1400,
}

price_key = "15ml"

selected_price = None

if price_key not in prices:
    print("Invalid price key")

else:
    selected_price = prices[price_key]
    print(selected_price)



#question 9 

#easy 



#question 10 

#accessing a nested dictionary 


menu_item_found = {
    "name": "Whisky",
    "prices": {
        "standard": 900,
        "15ml": 1000,
    },
}


#access the outer dictionary 

menu_item_found["prices"]


#access the inner dictionary 

menu_item_found["prices"]["15ml"]




#question 

menu_item = {
    "id": 69,
    "name": "Japanese Whisky",
    "inStock": True,
    "prices": {
        "standard": 900,
        "15ml": 1000,
        "double": 1600,
    },
}


#Stores the nested "prices" dictionary in a variable called prices
#Stores the "15ml" price in a variable called selected_price
#Prints:

#Japanese Whisky - 1000


prices = menu_item["prices"]
selected_price = menu_item["prices"]["15ml"]

print(menu_item["name"], "-", selected_price)



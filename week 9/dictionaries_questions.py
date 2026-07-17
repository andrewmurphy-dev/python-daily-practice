#dictionaries questions ! 

inventory = {
    "apples": 50,
    "bananas": 30,
    "grapes": 20,
    "oranges": 15
}


#question 1 

print(inventory["oranges"])

##question 2 

result = inventory.get("grapes")
print(result)


#question 3 
fruit = inventory.get("mangos", "Out of stock")

if fruit is None:
    print("Out of stock")
else:
    print(fruit)


#question 4 
#little confused how to update but i remember we can use delete 

inventory["apples"] = 100
print(inventory["apples"])

#lets try to understand this !
import json

with open("expenses.json", "r", encoding="utf-8") as file:
    results = json.load(file)

    print(results)



#you can see we use the r mode !
#also again we need to store the data into a variable in memeory !
#for day 1 , when its loaded into memory , it becomes a python list
#because json file starts with square brackets

#output class list

#and each item inside the list is a dicitonary !

print(type(result))
#class , list



print(type(result[0]))
#class dict




#{'name': 'coffee', 'amount': 500}


print(result[0]["name"])
print(result[0]["amount"])
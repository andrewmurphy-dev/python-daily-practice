#so similar to week 10

#how do we do save_expenses for JSON file !??


#what does this mean ?


#this means take python data from RAM and write it into JSON file on disk

#sometimes you can set the expenses.json file as a variable !
#for example

#FILE_NAME = expenses.json





def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as f:
        json.dump(expenses, file, indent=4)




#why do some save_expenses have a parameter and some do not!?
#when a function needs data from the outside , we give it a parameter

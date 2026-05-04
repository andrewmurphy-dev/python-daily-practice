#json.dump()

json.dump(data, file)

#this means take python data from RAM and write it into JSON file on disk


json.dump("what you want to save", "where ypu want to save it")

RAM ----> DISK (JSON FORMAT)

#basic syntax


import json

with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file)





#you remember from week 10 , what mode means !
#what does "w" mode mean ?
#if the file exists , it clears the old content
#then writes new content from the beginning !

#for this you do not need to loop over the dicitionary !
#like you did for week 10 !


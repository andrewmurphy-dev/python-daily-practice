#what are keyword arguments?

#these are potional arguments where you explicity write which paramter recieves each value 

#for example


def introduce(name="Andy", age=29):
    print()




#name ← "Andy"
#age  ← 29

#python stil understands 

#position does not matter makes sense ! as python matches using the parmater names 

#one important rule:


#positional arguments must come before keyword arguments 

#practice questions 

#question 1 

def order_food(quantity, category, item):
    print(quantity, category, item)



order_food(category="pizza", quantity=2, item="Napoli Kitchen")



#2 pizza Napoli Kitchen

#question 2 

def create_profile(username, age, country, job):
    print(username, age, country, job)



create_profile(job="SWE", country="Japan", username="Andrew1234", age=29)

#Andrew1234 29 Japan SWE


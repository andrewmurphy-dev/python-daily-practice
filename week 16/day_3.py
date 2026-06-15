class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


expense_1 = Expense("Keyboard", 30000, "Tech")
expense_2 = Expense("Coffee", 500, "Food")
expense_3 = Expense("Train", 250, "Transport")

print(expense_1.__dict__)
print(expense_2.__dict__)
print(expense_3.__dict__)



#in day 2 we learned objects store data ! 
expense_1.title
expense_1.amount
expense_1.category


#in day 3 
#objects can do actions using their own data !



#a method is a function that lives inside a class 



#for example 

class Contact:
    def __init__(self, name, email, phone)
        self.name = name
        self.email = email 
        self.phone = phone 



       #below is the method
        def display(self):
            print(f"{self.name}, {self.email}, {self.phone}")


contact_1 = Contact("Andrew", "andrewmurphy@email.com", "0894766327")


contact_1.display()
#or we can use ___dict___
print(contact_1.__dict__)






#so it method a better way than using __dict__?

#method is a better way of making the object do with its own data 

#the __dict__ is good for debug cause you can see the raw data 

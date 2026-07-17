
#practice question 

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount 
        self.category = category 


        def display(self):
            print(f"{title} - ¥{amount} - {category}")
#mistake you must include self. in the method function 


expense_1 = Expense("Keyboard", 30000, "Tech")
expense_2 = Expense("Coffee", 500, "Food")
expense_3 = Expense("Train", 250, "Transport")





expense_1.display()


#we do not use print() 
#as it is already contained in the method function 







#question 2 

class Contact:
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email 
        self.phone = phone 


    def display(self):
        print(f"Name: {self.name} Email: {self.email} Phone {self.phone}")



contact_1 = Contact("Andrew", "andrew@gmail.com", 12345)
contact_2 = Contact("Sarah", "sarah@gmail.com", 65252552)


contact_1.display()
contact_2.display() 



#problems 

#this part is structurely wrong  just the UI 
#print(f"Name: {self.name} Email: {self.email} Phone {self.phone}")





    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print()



#here we do a real world example 

class Contact:
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email
        self.phone = phone



#bow we create a object of that class 


contact_1 = Contact("Andrew", "andrewmurphy@gmail.com", "12345")
print(contact_1)
print(contact_1.__dict__)



#so when i print this in the terminal !

#<__main__.Contact object at 0x100b8c6e0>


#so what is this saying ?

#so __main__
#this is saying your class was created here in this module 
#confusion 

#the module i am currently running on is actually practice.py 
#python treats it as the main running script 



#Contact 
#Class name 

# 0x100b8c6e0

#this is memory style identity 


#we can see the data !
#we can use __dict__


#{'name': 'Andrew', 'email': 'andrewmurphy@gmail.com', 'phone': '12345'}

#it is in dictionary structure ! 


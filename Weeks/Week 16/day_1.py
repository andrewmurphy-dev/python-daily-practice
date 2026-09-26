#what is a class ?
#a class defines what kind of object python can create 

class Contact:
    pass 


contact_1 = Contact() 



#Contact is the Class 
#Contact() creates a real object 
#contact_1 stores that object ! 





#class needs leading capital letters , not because python forces it , it is just standard 
#this style is called PascalCase




#questions 



class Contact:
    pass



name_contact = Contact()

#so when python reaches this line 
#name_contact = Contact()
#Contact() is not a object sitting in memory 
#it physically creates a new object in memory ! 
#name points to that object 
#it has a type /class (Blueprint)
#Then it has attriubutes






#this is also same for 

name = "Andrew"

#name
# ↓
#[ string object: "Andrew" ]



#so "Andrew", Contact() are expressions!
#An expression is a piece of code that python can evaulate into a value/object in memory
#Contact() is a call expression ! 
#"Andrew" string literal expression 
#"Andrew" is the data , called sttributes 


#name  ─────►  string object
#              value/data: "Andrew"
#              type: str
#              methods: .upper(), .lower(), .strip(), etc.




#contact_1 = Contact()
#the python interpreter reads Contact() first , then the name pointing to the object in memory !


#instantiation --> this is a fancy word for creating an object from a class ! 

#attributes are data stored inside the object ! 

#what does dot notation mean  !


#for example ! 

contact_1.name 

#means: go inside this object and access something 


#so get the name 


contact.name 


print(contact.name)

#result 

"Andrew"






#what about app = FastAPI() 

#1. Evaluate the right side first: FastAPI()
#2. Call the FastAPI class
#3. Create a new FastAPI app object in memory
#4. Bind the name app to that object


#so when you do this ! 

@app.get("/contacts")
def get_contacts():
    return {"message": "Hello"}


#you are saying , registure this function as a GET route for /contacts



#FastAPI is the class/object maker.
#FastAPI() is the call expression that creates the app object.
#app is the variable pointing to that FastAPI object.
#Then @app.get(...) adds routes to that app object.
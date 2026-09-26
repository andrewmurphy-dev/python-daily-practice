#what __init__ means ?

#this is teh method that sets up the object attributes when object is created 

#what does self mean ?

#it means this specfic object in memory 
#it refers to the whole object 

#for example viusally 

#self
 #↓
#[ Contact object ]
#├── name  = "Andrew"
#└── email = "andrew@email.com"


#so theres two things pointing at the object in memory 


#contact_1
#  ↓
#[ Contact object in memory ]
#   ↑
 #self  ← used inside the class while __init__ runs


#contact_1 = outside name for the object
#self      = inside-class name for the same object


#so theres basically two names pointing at the object 

#one outside 

#one inside 


#why is it important to have this ?

#they are used in different places !


#python needs a way to say to put this name, email into this object BEING CREATED
#for example

self.name = name
self.email = email



#after it is created you can use contact_1.name , contact_1.email 



#what is __dict__?

#it is a special attribute that shows the data stored inside the object 
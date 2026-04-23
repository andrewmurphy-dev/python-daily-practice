students = {
        "student1": {"name": "Andre", "age": 20, "grade": "A"},
        "student2": {"name": "Maria", "age": 22, "grade": "B"},
        "student3": {"name": "John",  "age": 19, "grade": "C"},
    }

#this finds outer keys!

print(students.keys())


#find the inner keys ! 
print(students["student1"].keys())



#good way t think of it in easy terms , anything before a colon is a key !


#the general structure ! 


#{
    #"name": "Andre"
#    ^       ^
#    |       └── value (right of colon)
#    └── key (left of colon)
#}



#students = {
#    "student1": {"name": "Andre", "age": 20}
#      ↑            ↑        ↑      ↑    ↑
#    outer        inner    inner  inner inner
#     key          key     value   key  value
#}



#what students.items() actually produces !?

("student1",  {"name": "Andre", "age": 20, "grade": "A"})
("student2",  {"name": "Maria", "age": 22, "grade": "B"})
("student3",  {"name": "John",  "age": 19, "grade": "C"})
("student4",  {"name": "Lea",   "age": 21, "grade": "A"})
   ↑                           ↑
 OUTER key                 OUTER value
(a string)              (an inner dict)
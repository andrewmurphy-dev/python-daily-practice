"""
Day 4 — Nested Dictionary Practice
Take it slow. Do one at a time. Write your answer under each question.
"""


students = {
    "student1": {"name": "Andre", "age": 20, "grade": "A"},
    "student2": {"name": "Maria", "age": 22, "grade": "B"},
    "student3": {"name": "John",  "age": 19, "grade": "C"},
    "student4": {"name": "Lea",   "age": 21, "grade": "A"},
}



# ============================================================
# LEVEL 1 — WARM UP (just accessing values)
# ============================================================

# Q1. Print the NAME of student1.
# Expected output: Andre

print(students["student1"]["name"])



# Q2. Print the AGE of student3.
# Expected output: 19
print(students["student3"]["age"])



# Q3. Print the GRADE of student4.
# Expected output: A
print(students["student4"]["grade"])




# ============================================================
# LEVEL 2 — LOOPING (single loop)
# ============================================================

# Q4. Loop through the students dictionary and print each student ID.
# Expected output:
# student1
# student2
# student3
# student4

for key in students.keys():
    print(key)

# Q5. Loop through the students and print ONLY their names.
# Expected output:
# Andre
# Maria
# John
# Lea

for value in students.values():
    print(value["name"])


#the value name is misleading ! 
#its technically not a value, its technically the outer key ! 


# Q6. Loop through the students and print each name with their grade,
# like this:  "Andre - A"
# Expected output:
# Andre - A
# Maria - B
# John - C
# Lea - A


for info in students.values():
    print(info["name"], "-", info["grade"])




# ============================================================
# LEVEL 3 — NESTED LOOP (loop inside a loop)
# ============================================================

# Q7. For every student, print their ID, then print all their info
# (key: value) indented under it.
# Expected output:
# student1
#    name: Andre
#    age: 20
#    grade: A
# student2
#    name: Maria
#    ...





# ============================================================
# LEVEL 4 — LOGIC + LOOPING (mixing if + loop)
# ============================================================

# Q8. Count how many students have grade "A".
# Expected output: 2



# Q9. Print the names of all students who are OLDER than 20.
# Expected output:
# Maria
# Lea



# Q10. Add a new field "passed" to each student:
#      True  if grade is "A" or "B"
#      False if grade is "C" or worse
# Then print the updated dictionary.





# ============================================================
# BONUS (only if you have energy) — MODIFYING
# ============================================================

# Q11. Add a new student "student5" with name "Tom", age 18, grade "B".



# Q12. Change John's grade from "C" to "B".



# Q13. Remove the "age" field from student1 only.





# ============================================================
# TIP
# ============================================================
# If you get stuck, remember:
#   students                        -> the whole dict
#   students["student1"]            -> one student (a dict)
#   students["student1"]["name"]    -> one value ("Andre")
#
#   for k, v in students.items():   -> k = "student1", v = {"name": ...}

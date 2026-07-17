

#question 1


car = {
    "brand": "Toyota",
    "model": "Supra",
    "year": 2024,
    "color": "red"
}



del car["color"]
print(car)



#question 2

car = {
    "brand": "Toyota",
    "model": "Supra",
    "year": 2024,
    "color": "red"
}




car.pop("color")
print(car)



#question 3

product = {
    "name": "Laptop",
    "price": 1200,
    "brand": "MSI"
}


removed_brand = product.pop("brand")
print(removed_brand)

#question 4
#delete two keys


student = {
    "name": "Mike",
    "age": 21,
    "grade": 88,
    "school": "Tokyo Uni"
}


del student["age"]
del student["school"]
print(student)



#question 5

session = {
    "username": "andrew",
    "token": "abc123",
    "login_time": "10:00",
    "temporary_data": "xyz"
}

del session["temporary_data"]
print(session)
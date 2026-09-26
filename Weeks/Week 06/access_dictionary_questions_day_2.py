#access dictionary questions

#question 1

car = {
    "brand": "Toyota",
    "model": "Supra",
    "year": 2024
}


print(car["model"])





#question 2
#store then print

user = {
    "username": "andrew",
    "age": 26,
    "country": "Japan"
}


name = user["username"]
print(name)


#question 3
#access multiple values

product = {
    "name": "Laptop",
    "price": 1200,
    "brand": "MSI"
}


print(product["name"])
print(product["price"])


#question 4
#access inside a loop

scores = {
    "math": 90,
    "science": 85,
    "english": 88
}


#loop though the dictionary and print the values only



for key, value in scores.items():
    print(value)


#question 5
#lookup pattern
phonebook = {
    "John": "555-1234",
    "Anna": "555-8888",
    "Mike": "555-4321"
}

search = "Anna"

print(phonebook[search])

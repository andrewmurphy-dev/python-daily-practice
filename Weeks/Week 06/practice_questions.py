

#question 1
numbers = [4, 9, 2, 11, 6, 3]
large = []
#build a new list

for i in numbers:
    if i > 5:
        large.append(i)

print(large)



#question 2
numbers = [2,5,7,3]

results = []

def square(x):
    return x * x


for i in numbers:
    results.append(square(i))

print(results)


#question 3
numbers = [1,4,6]
results = []


def double(x):
    return x * 2

def add_three(x):
    return x + 3


for i in numbers:
    results.append(add_three(double(i)))

print(results)


#question 4
numbers = [3, 7, 1, 9, 4, 8]
count = 0

for i in numbers:
    if i > 5:
        count += 1
print(count)



#question 5
numbers = [2, 4, 6, 8]
results = []

def add_five(x):
    return x + 5

for i in numbers:
    results.append(add_five(i))
print(results)



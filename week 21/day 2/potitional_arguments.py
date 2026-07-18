#what are positional arguments ?


#for example 


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Bob", 25) # here "Bob" and 25 are positional arguments because they are passed to the function in the order of the parameters defined in the function.

#name ← "Andy"
#age  ← 29

#the order of the arguments matters, if we change the order of the arguments, it will lead to incorrect output.

#practice questions 

#question 1
def player_info(username, level, character_class):
    print(f"Username: {username}, Level: {level}, Class: {character_class}")

player_info("andy", 28, "Mage")

#question 2

def Create_Character(name, character_class, level, server):
    print(f"Name: {name}, Class: {character_class}, level: {level}, Server: {server}")



Create_Character("Andy", "Mage", 23, "Firemaw")


#what does return do?

#1 
#It sends a value back from the function.

#2
#It immediately stops the function.


#for example 


def find_ticket():
    return "found"

    print("This never runs")


#return "found"


#for example


def test():
    print("A")
    return 10
    print("B")


#only A is printed.




#for example 


def test():
    return 5
    return 10



#5




#for example


def test():
    number = 3

    if number == 3:
        return "yes"

    return "no"

#yes 
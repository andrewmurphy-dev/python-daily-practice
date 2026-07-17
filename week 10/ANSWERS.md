# Return — your answers (add more as you go)

## A1 — Return vs print

**Your version (good start):**  
`return` stops the function and gives a result; `print` shows something on the terminal.

**Tighten one layer:**  
- **`return`** hands a value **to the code that called the function** (so you can do `x = f()` and use `x` later). It also **exits** the function right there.
- **`print`** only **displays** text; it does **not** give a value to the caller in a useful way (the function still “returns” `None` if you didn’t use `return` with a value).

So: same function can *print* (side effect) and *return* (value to caller), or one or the other.




## a2 question 
yes that means after the for loop based upon the final condition result ! 

but my question is what is storing this final condition result , it updates along with the tracking varible 


#this is wrong, return after the loop means the loop has already run and finished 

whatever u return is not a special condition result kept in a hidden place

for example     
largest = numbers[0]   # storage for “best so far”
for n in numbers:
    if n > largest:
        largest = n     # update storage each time
return largest         # one value: whatever `largest` is *now*

wwht stores the answer? 
the variable - largest
it changes each time the if or the body runs in a way that should update it

In order:

The loop runs and keeps updating the tracking variable (largest, second, total, etc.).
When the loop ends, that variable holds the last value — the one you care about for the whole list.
return that variable (or an expression using it) sends that value to whoever called the function (e.g. x = my_func(...) then x is that value).


#for example 



def total_of_three(a, b, c):
    s = a + b + c
    return s          # "send" the value of s back to whoever called this function

x = total_of_three(1, 2, 3)   # the function runs and return sends 6 back here
print(x)                      # 6


So the “comes back here” means: the call total_of_three(1, 2, 3) is replaced by 6 in that expression, then x stores 6.

x = (result of total_of_three(1,2,3)) → x = 6, not 6 = (1,2,3)


## question 3
numbers = [1, 3, 4, 5]

for i in numbers:
    if i > 2:
        return i


## question 4

numbers = [1, 3, 4, 5]

largest_number = numbers[0]

for i in numbers:
    if i > largest_numbers:
        largest_mumbers = i 

return largest_number

## question 5 
It depends. If the indentation is invalid, Python may not run at all; the first thing you see is usually an IndentationError (or SyntaxError) in the terminal. If the code still runs but return is in the wrong place logically (for example, return inside a loop when you meant to finish the whole list first), the first “wrong output” is often a wrong result (like the wrong max, or a value from only part of the list) — and you might not get an error at al




## question 6 

this question is about control flow ! 

and lines in a function body ! 

#the question is asking , if there are more lines in that same function below that return --- do the lines still run ? 


that is the effect of the return on the code that comes after it in the function ! 

so in that particular function , the lines below it will not run as the conditions have been met in the current loop iteration ! as a result it will stop the function ! 


this is a little wrong ! 

its not really about the "conditions have been met in the current loop iteration" 
in general the return stops the function whenever that line is executed in a for loop , after an if or no loop at all 

the reason you might hit return might be an if condition but the stopping is from return itself not from the loop or "condition is met" 

the current loop iteration 


## question 7 

yes a function can have two return paths ! 
depending what to call to the function caller result ! 


#a function can have many return statements 


each time you call the function , only one of those paths runs ! 

the caller gets one value per call 

### question 8 

i dont really know what none means but , i assume it means it cannot compute a value ! so return none is the value 

why might , second_largest return 'none' for '[8]'! 


#correct answer below ! 

none is a real python value , which means , "no value" "nothing here" , "no answer"

#for example 


def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags




what does debug=none mean? '

it does not mean "debugging is off" 

it means no value was supplied ! 


debug=none is not error handling , it is an arguement , you use none to mean "the caller did not pass this" 







### question 9 

`a < b < c` — write it as two comparisons with `and` using the *same* middle variable.


a < b and b < c



### question 10 
im not sure 


python chains comparisons this is two checks combined with implicit "and"

largest > n > second 

this means 

largest > n and n > largest 



#for example 

numbers = [10, 3, 8, 1]

# start: first number is both "best so far" and we fake second as very low
largest = numbers[0]   # 10
second = float("-inf") # "no real second yet"

for n in numbers[1:]:  # n will be 3, then 8, then 1
    if n > largest:
        second = largest
        largest = n
    elif largest > n > second:
        second = n

print(largest, second)   # 10 8





    elif largest > n > second:
        second = n

print(largest, second)   # 10 8


in this branch , on purpose , you do not set largest. 




#example 2 

scores = [72, 95, 88, 91]

highest = scores[0]
second_highest = float("-inf")

for score in scores[1:]:
    if score > highest:
        second_highest = highest
        highest = score
    elif highest > score > second_highest:
        second_highest = score

print(highest, second_highest)  # 95 91

### question 11

beacsue we can get every possible integer in the list 

### question 12 


x if cond else y 

this reads like 

use x if the condition is True, otherwise use y



###   question 13 
if/else can run blocks of code.
A ternary chooses one value/expression.
Use ternary for simple value choices, not complicated logic.

### question 14 

if key is missing python crashes with key error 

if there is a key, python gives a defualt ---> none 

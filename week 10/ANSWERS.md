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

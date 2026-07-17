# Practice 10 — ties to conceptual Q1–6 (return vs print, return placement, None, ternary, etc.)
# Fill the functions, then:  python practice_10_q1_6.py
# This runs `assert` checks. Fix failures until it prints: All checks passed.

# ==============================================================================
# Q1  (Q1) — "Return" hands a value to the caller. Write a function that
#     RETURNS the square of x. Do not print inside the function.
#     The caller (below, when you un-comment) can print the result.
# ==============================================================================

def square(x):
    return x ** 2


result = square(5)
print(result) 


#this means ** expontiation
#this is * multiplication 

# caller (optional):  print(square(5))   # should show 25


# ==============================================================================
# Q2  (Q1) — Contrast: no def. At module level, compute 7 ** 2 and print it.
#     Here there is no "return to a caller" — you only show output.
#     (This is a simple script-style answer.)
# ==============================================================================

square_of_seven = 7 ** 2

print(square_of_seven)



# your code (plain statements, e.g. print(...))


# ==============================================================================
# Q3  (Q4, no loop) — `return` can live after simple logic. Write a function
#     `sign(n)` that returns: 1 if n > 0, -1 if n < 0, 0 if n == 0.
#     Use if / elif / return. No for-loop.
# ==============================================================================

def sign(n):
    if n < 0:
        return -1 
    elif n > 0:
        return 1
    else:
        return 0



# ==============================================================================
# Q4  (Q3 + return) — "First match" — return INSIDE the loop. Write
#     `first_long_word(words)` where words is a list of str.
#     Return the first string with len > 5, or return None if none.
#     Hint: `for w in words:` and compare len(w).
# ==============================================================================

def first_long_word(words):
    for word in words:
        if len(word) > 5:
            return word 
    else:
        return None





# ==============================================================================
# Q5  (Q4) — "Full scan" — return AFTER the loop. Write `maximum(nums)` that
#     returns the largest int in a non-empty list. Use a loop, one tracking
#     variable, and one return when the loop ends. No max().
#     (You may assume len(nums) >= 1.)
# ==============================================================================

def maximum(nums):
    largest_number = nums[0]

    for num in nums:
        if num > largest_number:
            largest_number = num 

    return largest_number 

# ==============================================================================
# Q6  (Q5–6) — "Early exit" in one function, two return paths, no loop.
#     `clamp_zero(n)` : if n < 0, return 0. Otherwise return n.
#     Lines after a return on the same code path are skipped; keep your
#     return statements clear and readable.
# ==============================================================================

def clamp_zero(n):
    if n < 0:
        return 0
    else:
        return n 
    


# ==============================================================================
# Q7  (Q6) — "Unreachable" awareness. In `only_positive(n)`, if n is less
#     than 0, return 0. Otherwise return n * 2.
#     After you write it, add ONE comment line: which line (if any) is never
#     run when n is negative? (Mental check, not a second function.)
# ==============================================================================

def only_positive(n):
    if n < 0:
        return 0 
    else:
        return n * 2
  

# ==============================================================================
# Q8  (A1 + None) — `safe_second_item(items)`: if len(items) < 2, return None;
#     else return `items[1]`. No loop needed.
# ==============================================================================

def safe_second_item(items):
    if len(items) < 2:
        return None
    else: 
        return items[1]
  


# ==============================================================================
# Q9  (ternary / expression) — One line body is OK. `bigger(a, b)` should
#     return the larger of the two numbers (if equal, return a or b, your choice),
#     using the conditional expression:  x if condition else y
#     (No if-block with two separate returns, unless you prefer; the practice
#     is the ternary.)
# ==============================================================================

def bigger(a, b):
    return a if a > b else b 




#confusion 

def bigger(a, b):
    if a > b:
        return a
    return b

#we use two returns 

#Both versions do the same thing: the first computes which value to send back in one expression, 
#then returns once, while the second uses two separate return lines because return can’t sit inside a if c else b, only a and b can.
    


# ==============================================================================
# Q10 (mix) — A tiny program using both styles:
#   (a) A function `format_greeting(name)` that RETURNS the string
#       "Hi, {name}!"  (or your wording) — not print in the def.
#   (b) Below, assign `msg = format_greeting("You")` and print `msg` once.
#   This is one block: your function + two lines at module level for (b).
# ==============================================================================

def format_greeting(name):
    return f"hi, {name}"
    

# (b) your module-level two lines: assign msg, print
#     (The self-test below only checks the function, not the print. Add your (b) lines
#      here or in `if __name__ == "__main__"` to avoid double-printing during tests if needed.)


msg = format_greeting("andrew")
print(msg)

def _run_checks():
    """Call after you implement each `pass` — raises AssertionError on failure."""

    # Q1
    assert square(0) == 0
    assert square(5) == 25
    assert square(-3) == 9



    # Q2: no function — verify yourself: running this file should be able to print 49 = 7**2
    #     (put your print(7**2) inside `if __name__ == "__main__":` with `_run_checks()` to avoid
    #      two separate stories, or just run Q2 in the REPL.)

    # Q3
    assert sign(10) == 1
    assert sign(0) == 0
    assert sign(-5) == -1

    # Q4 — first with len *strictly* > 5
    assert first_long_word(["a", "bb", "ccccc"]) is None  # 5 is not > 5
    assert first_long_word(["a", "banana", "x"]) == "banana"  # len 6
    assert first_long_word([]) is None

    # Q5
    assert maximum([1, 2, 3, 0]) == 3
    assert maximum([-1, -5, -2]) == -1
    assert maximum([7]) == 7

    # Q6
    assert clamp_zero(-1) == 0
    assert clamp_zero(0) == 0
    assert clamp_zero(3) == 3

    # Q7
    assert only_positive(-1) == 0
    assert only_positive(4) == 8
    assert only_positive(0) == 0

    # Q8
    assert safe_second_item([1, 2]) == 2
    assert safe_second_item([1]) is None
    assert safe_second_item([]) is None
    assert safe_second_item([9, 8, 7]) == 8

    # Q9 (equal case: you may return either; both allowed)
    assert bigger(1, 3) == 3
    assert bigger(3, 1) == 3
    _eq = bigger(2, 2)
    assert _eq == 2

    # Q10 — exact string from the spec: "Hi, {name}!"
    assert format_greeting("You") == "Hi, You!"
    assert format_greeting("A") == "Hi, A!"

    return True


if __name__ == "__main__":
    # Optional: your Q2 script output (uncomment and align with "no def" exercise):
    # print(7**2)  # expect 49

    # Optional: your Q10(b)
    # msg = format_greeting("You")
    # print(msg)

    _run_checks()
    print("All checks passed.")


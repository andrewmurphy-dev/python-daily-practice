# `return` & loops — question bank (concept + code)

**How to use this file**

1. **Week 1 focus (do first):** Sections A + B, then the first ~8 coding items in C.  
2. **Week 2:** Finish C, then D and E.  
3. For each *coding* item: write, predict *before* you run, run, one-line “why”.

**Why this order?** `return` placement and loop scope show up in almost every script. Chained `if/elif` and ternaries build on the same “control flow” mental model.

---

## A) Recommended “question questions” (answer in plain English)

*These are not code — they check that you *understand* before you only memorize.*

1. In one sentence: what is the difference between a function *returning* a value and *printing* it?  
   *(Write your answer in `return/ANSWERS.md` or a notebook — keep this file as questions only.)*
2. When the lecture says “return is outside the if,” does that always mean *after* the `for` loop? Explain.
3. Give an example where `return` **inside** the `for` loop is the *right* design.
4. Give an example where `return` **after** the `for` loop is the *right* design.
5. If `return` is in the wrong indent level, what is the *first* kind of wrong output you might see?
6. What does `return` do to the rest of a function? (Lines below it, same function.)
7. Can a function have two `return` paths? Is that normal?
8. What is `None`? Why might `second_largest` return `None` for `[8]` or `[2,2,2]` (depending on your spec)?
9. `a < b < c` — write it as two comparisons with `and` using the *same* middle variable.
10. `elif largest > n > second` — in words, what are we requiring about `n`?
11. Why is `float("-inf")` sometimes used as a starting “max” or “second max” value?
12. Ternary: `x if cond else y` — what do `x` and `y` represent? When does it *not* run the other branch?
13. What is the difference between `if/else` and a ternary, besides line count?
14. `dict.get(k)` vs `d[k]` when the key is missing — how does that relate to “sometimes there is no answer”?

---

## B) Shorter self-checks (1–2 lines each)

1. `return` inside a loop: always means “we already have the final answer and can stop the whole function.” — True or false? Fix if false.
2. The body of a `for` runs once per item — the `return` that lines up with `for` (not inside `for`) runs how many times?
3. Name one bug class you fixed when `return` was accidentally inside a `for` in a max function.

---

## C) Coding questions — `return` and loops (core track)

*Write small functions. No `max()` / `min()` on the first pass if you want muscle memory.*

1. `largest_number(nums)` → return the largest; empty list → `None`.
2. `index_of_largest(nums)` → return the index of the first largest; empty → `None`.
3. `sum_list(nums)` → return total using a loop (no `sum()`).
4. `count_positive(nums)` → return how many numbers are `> 0`.
5. `first_negative(nums)` → return the *first* negative or `None` (good place to `return` *inside* loop).
6. `all_positive(nums)` → return `True` if all `> 0` else `False` (empty: decide and document; common choice `True` or `False` — be consistent).
7. `has_duplicate(nums)` → return `True` if any value appears twice (nested loop OK for training).
8. `second_largest_distinct(nums)` → return second largest *distinct* value, or `None` if it does not exist. Use a single pass and `-inf` trick, or do it with two passes; pick one and stick to it.

---

## D) Coding questions — edge cases (same track, harder)

1. `second_largest` with all equal numbers → `None` (or document returning “no second” another way, but be explicit).
2. `second_largest` for list length 0, 1, and 2; assert expected by hand.
3. Mixed positives and negatives: e.g. `[-5, -1, -10]`; largest and second from your function.
4. `clamp_list(nums, lo, hi)` — loop: build new list with each `n` replaced by in-range (use `if` in loop; return new list *after* loop).
5. Read a line of space-separated integers from `input()`; parse to list; return largest and second (no printing inside helper if you can avoid it).

---

## E) Ternary, `None`, and style (light practice)

1. Replace a 4-line `if/return` with one ternary `return` for: “`None` if `x` is 0 else `x`.”
2. At call site, handle `result is None` with a user-friendly message.
3. Same as (1) but the condition is: “if `name` is empty string, return `None` else return `name` stripped.”

---

## F) “Stretch” (optional — not required to move on)

1. `nth_largest(n, k)` — k-th largest *distinct* (k = 1 is largest) without sorting, or with sorting: pick one, justify.
2. `running_max(nums)` — return a new list: at each index, the max seen so far (O(n) single pass).

---

*End of bank. Revisit A every few days until answers feel instant.*

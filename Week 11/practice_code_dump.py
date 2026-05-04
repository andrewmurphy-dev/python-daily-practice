
import json

expenses = [
    {"name": "coffee", "amount": 500},
    {"name": "train", "amount": 220},
    {"name": "lunch", "amount": 900}
]



with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=4)



print("expenses saved to JSON file")

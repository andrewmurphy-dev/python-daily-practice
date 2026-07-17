

def load_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            expenses = []
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                #what does this do?
                #for each line do this ["milk", "250"]

                name = parts[0]
                price_text = parts[1]

                price = int(price_text)

             expense = {
                    "name": name,
                    "price": price
             }

                  expenses.append(expense)
            
             return expenses

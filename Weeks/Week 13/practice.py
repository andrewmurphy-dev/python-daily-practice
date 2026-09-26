





#question 2
#expense tracker


expense_lines = [
    "food,1200",
    "rent,60000",
    "coffee,450",
    "bad line",
    "transport,900",
    "snacks,abc",
    "",
    "gym,5000"
]



def parse_expenses(expenses):
    valid_lines = {}
    invalid_lines = []

    if not expenses:
        print("no data input found!")
        return

    for line in expenses:
        origional_line = line
        line = line.strip()



        if line == "":
            invalid_lines.append(origional_line)
            continue


        parts = line.split(maxsplit=1)

        if parts != 2:
            invalid_lines.append(parts)
            continue

        category = parts[0]
        amount_text = parts[1]

        if not amount_text.isdigit():
            invalid_lines.append(amount)
            continue

        amount = int(amount_text)

        valid_lines[category] = amount

    return valid_lines, amount





#there is one confusion i have  !
#the append aspedt but it technically makes sense cause, as we loop we loop with a tracking variable which is origional_text






















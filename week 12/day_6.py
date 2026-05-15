#so lets practice day 5 here

def load_file():

    with open("/Users/andrewmurphy/Downloads/Deck - Boros Aggro.txt", "r", encoding="utf-8") as file:
        x = []
        for line in file:
            line = line.strip()
            if line == "":
                continue

            quantity_text, name_card = line.split(maxsplit=4)

            quantity = int(quantity_text)

            card = {
                "card quantity": quantity,
                "card name": name_card
            }

            x.append(card)


        return x



#you forgot to @ut try in but its ok !


def line_fixing(x):
    if not x:
        return None

    if "card name" not in x:
        return False

    if "card quantity" not in x:
        return False

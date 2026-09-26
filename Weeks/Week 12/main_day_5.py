
def load_file():

    try:
        with open("/Users/andrewmurphy/Downloads/Deck - Boros Aggro.txt", "r",encoding="utf-8") as file:
            deck = []



            for line in file:
                line = line.strip()
                if line == "":
                    print("line cannot be empty!")
                    continue


                quantity_text, card_name = line.split(maxsplit=1)

                quantity = int(quantity_text)

                card = {
                    "quantity": quantity,
                    "name": card_name

                }

                deck.append(card)

            return deck


    except FileNotFoundError:
        print("deck is not found!")
        return []




result = load_file()
print(result)


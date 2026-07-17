#here we are doing some revision of da 4


def load_text():
    try:
        with open("/Users/andrewmurphy/Downloads/Deck - Boros Aggro.txt", "w", encoding="utf-8") as file:
            deck = []
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                quantity_text, name = line.split(maxsplit=1)
                quantity = int(quantity_text)

                deck_name = {
                    "card name": name,
                    "card quantity":  quantity
                }

                deck.append(deck_name)

            return deck



    except FileNotFoundError:
        print("file not found!")
        return []


result = load_text()
print(result)

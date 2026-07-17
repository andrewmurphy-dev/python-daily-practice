


def practice_day_four():

    try:
        with open("Deck - Boros Aggro.txt", "r", encoding="utf-8") as file:
            deck = []
            for line in file:
                line = line.strip()
                if line == "":
                    continue



                amount_text, card_name = line.split("", 1)

                amount = int(amount_text)

                card = {
                    "quantity": amount,
                    "card": card_name
                }

                deck.append(card)


            return deck








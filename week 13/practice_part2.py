deck_lines = [
    "4 Lightning Bolt",
    "2 Mountain",
    "3 Monastery Swiftspear",
    "bad line here",
    "1 Goblin Guide",
    "",
    "x Shock",
    "5"
]



#quantity , card name





def deck_lines_test(deck_lines):

    if not deck_lines:
        print("no input found")
        return


    for line in deck_lines:
        x = []

        line = line.strip()
        if line == "":
            print("line is blank!")
            continue


        quantity_text, card_name = line.split(maxsplit=4)

        quantity = int(quantity_text)


        valid_deck = {
            "card name": card_name,
            "quantity": quantity
        }


        x.append(valid_deck)

    return x







#this was actually wrong !

#so the solution you actually understood all of it !
#but didnt think of it
#so we need a better planning pattern
#

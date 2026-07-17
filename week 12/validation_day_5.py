#here below is validation for my card dist in ram


#so what happens if we miss quanitiy


def validation_card(card):
    if not card:
        return None

    if "name" not in card:
        print("missing name")
        return False


    if "quantity" not in card:
        print("missing quantity")
        return False

    return True



#we do not need to loop though the data, as we are dealing with one dictionary at a time

#also this is what it looks like in RAM

card = {
    "quantity": quantity,
    "name": card_name

}

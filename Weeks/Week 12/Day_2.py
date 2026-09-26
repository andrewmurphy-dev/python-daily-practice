#day 2 focuses on safe number conversion
#lets do some real world examples

def get_quantity():

    while True:
        quantity_text = input("Enter quantity: ").strip()

        if quantity_text == "":
            print("Quantity cannot be empty!")
            continue


        try:
            quantity = int(quantity_text)

        except ValueError:
            print("Quantity must be a number!")
            continue


        if quantity < 1:
            print("invalid quantity!")
            continue

        elif quantity > 10:
            print("invalid quanitity")
            continue


        return quantity

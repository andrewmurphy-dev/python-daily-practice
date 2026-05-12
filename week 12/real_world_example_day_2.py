def get_price():
    while True:
        price_text = input("Enter price of your product: ").strip()

        if price_text == "":
            print("Price cannot be empty.")
            continue

        try:
            price = float(price_text)
        except ValueError:
            print("Price must be a number.")
            continue

        if price < 0:
            print("Price cannot be negative.")
            continue

        return price


result = get_price()
print(result)

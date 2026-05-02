#so looks like we need to rewrite add_epenses function 


def add_expenses():
    product_name = input("enter the name of the product: ").lower().strip()

    if product_name == "":
        print("error, cannot be blank, please try again!")
        return 

    product_amount = input(f"enter amount of {product_name}: ")
    if product_amount == "":
        print("error, cannot be blank, please try again!")
        return

    if not product_amount.isdigit():
            print("error, invalid amount, please try again!")
            return
    
    try:
        amount = int(product_amount)
        
    except ValueError:
        print("error, invalid amount, please try again!")
        return
    
    expenses[product_name] = amount
    save_expenses()
    print("your expenses have been added")




def show_expenses():
    show = load_expenses()

    if not show:
        print("no expenses found")
        return

    print()
    print("show expenses")
    print("-" * 30)

    for product_name, amount in show.items():
        print("product name", product_name)
        print("size", amount)










#so looks like we need to rewrite add_epenses function 





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





def show_total():
    total = load_expenses()


    if not total:
        print("no expenses found")
        return

    print()
    print("Total expenses")
    print("-" * 30)



    total_amount = 0

    for amount in total.values():
        total_amount += amount
    print(f"total: {total_amount}")
    return total_amount









def display_contacts(contact):
    if not contact:
        print("no contacts found")
        return

    print()
    print("Display Contacts")
    print("-" * 30)

    for name, value in contact.items():
        print("username:\t", name)
        print("email:\t", value["email"])
        print("phone:\t", value["phone"])




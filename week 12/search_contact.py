

def search_contacts(contact):
    if not contact:
        print("no contacts found")
        return


    print()
    print("Search Contacts")
    print("-" * 30)

    email_search = input("enter the email address of the user you wish to search!: ").strip()
    
    if email_search == "":
        print("email search cannot be empty!")
        return 
    
    if not email_search in contact:
        print("no email address found!")
        search_contacts()
    
    for name, value in contact.items():
        if email_search == value["email"]:
            print("username:\t", name)
            print("email:\t", value["email"])
            print("phone:\t", value["phone"])
            

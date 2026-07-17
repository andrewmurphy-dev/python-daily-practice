
def add_contact():

    while True:
        print("welcome to add contact section!")

        name = input("Please enter your name: ").strip().lower()

        if name == "":
            print("name cannot be blank")
            continue

        phone_text = input("Please enter your email: ").strip()
        
        if phone_text == "":
            print("phone cannot be blank!")
            
        email = input("please enter your email address!: ").strip().lower()
        
        try:
            phone = int(phone_text)
            
            contacts[name] = {"email": email, "phone": phone}
            save_manager()
            
        except ValueError:
            continue 
            

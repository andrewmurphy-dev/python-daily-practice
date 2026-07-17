#safe username loader



def load_users():
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            users = []
            for line in file:
                username = line.strip()

                if username == "":
                    continue

                users.append(username)

            return users


    except FileNotFoundError:
        print("no users where found!")
        return []

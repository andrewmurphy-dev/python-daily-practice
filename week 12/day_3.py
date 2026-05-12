def load_file():

    try:
         with open("users.txt", "r", encoding="utd-8") as file:
             data = file.read()
             return data

    except FileNotFoundError:
        print("no file found, Starting empty!")
        return ""




result = load_file()
print(result)


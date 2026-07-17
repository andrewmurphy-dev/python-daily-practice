#what does it mean ?
import json
from json import JSONDecodeError


#open the json file , read it , and rebuilt it as a python data in RAM



#we do not need a parameter ! because we are not calling the function and implementing data into it !
#so we need to use try, except for this ducntion because there might be an error loading it from disk to ram !


def load_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
        #so here it gets a little out of the ordinary for patterns!

        return json.load(file)

    except FileNotFoundError:
        return []

    except JSONDecodeError:     #error if the file is not json file !
        print("Error: expenses.json exists, but it is not valid JSON.")
        return None

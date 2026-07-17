
#so we are not using a dicitonary here !
#we will use a list !

def save_score(name, score):
    with open('scores.txt', 'a', encoding="utf-8") as f:
            f.write(f"{name},{score}\n")

#we will be using append mode !
#this means open scores.txt
#do not delete old data !
#add new scores underneath the old scores !


#my wu



def read_scores():
    scores = [] #this is a list !
    try:
        with open('scores.txt', 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()



                if line == "":
                    continue


                name, score = line.split(",", 1)
                score = int(score)
                scores.append((name, score))

    except FileNotFoundError:
        print("File not found")

    return scores








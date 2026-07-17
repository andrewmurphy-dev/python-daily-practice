from quiz_storage import save_score, read_scores

def add_score():
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    score = input("Enter score: ").strip()

    try:
        score = int(score)
    except ValueError:
        print("Score must be a number.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    save_score(name, score)
    print("Score saved.")



def show_scores():
    scores = read_scores() #so we call this function !

    if not scores:
        print("No scores saved yet.")
        return

    print()
    print("Saved Scores")
    print("-" * 30)

    for score_data in scores:
        name = score_data[0]
        score = score_data[1]

        print(f"{name}: {score}")










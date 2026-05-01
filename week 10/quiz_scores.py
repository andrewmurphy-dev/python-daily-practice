from utils_scores import add_score, show_scores

def quiz_score(score):

    while True:
        print("welcome to score quiz game!")
        print("please choose from the options below!")

        print("press 1: add score")
        print("press 2: show scores")
        print("press 'exit' to quit")

        choice = input("please choose: ")
        if choice == "":
            print("choice cannot be empty")
            return

        elif choice == "1":
            add_score()

        elif choice == "2":
            show_scores()

        elif  choice == "exit":
            print("bye")
            break



quiz_score()



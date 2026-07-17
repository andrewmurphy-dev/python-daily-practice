#how do i make a dictionary !



#lets say we get a list of words


def words_dict():
    x = input("enter a long word sentence: ").strip().split()

    word_dict = {}

    for word in x:
        if word in word_dict:
            word_dict[word] += 1

        else:
            word_dict[word] = 1



    for words, value in word_dict.items():
        if value > 2:
            print(words)




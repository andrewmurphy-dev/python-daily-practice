#today we are going over unique words
#we put words into a dictionary and count how many words

#question 1

sentence = input("enter a long sentence: ").lower().split()

counts = {}


for word in sentence:
    if word in counts:
        counts[word] += 1

    else:
        counts[word] = 1

# it will turn into like this

counts = {
    word_1, 2
    word_2, 1
    word_3, 8
}

for word, count in counts.items():
    if count == 1:
        print(word)





#question 2


        def unique_word():

            words_sentence = input("enter a sentence: ").lower().strip()

            counts = {}

            for word in words_sentence:
                if word in counts:
                    counts[word] += 1

                else:
                    counts[word] = 1


            for word, count in counts.items():
                if count > 1:
                    print(word)



#you forgot #split()
#also when you make a function do not forget to call it ! 

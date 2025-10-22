word_1 = input()
word_2 = input()

prev_word = ""

for i in range(len(word_1)):
    word_final = word_2[:i + 1] + word_1[i + 1:]

    if word_final != word_1 and word_final != prev_word:
        print(word_final)
        prev_word = word_final
 
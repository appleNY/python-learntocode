# https://dmoj.ca/problem/ccc02j2

# change "or" to "our"
# The rules for the word has more than four letters
# has a suffix consisting of a consonant followed by or
# type "quit!", the program should terminate

# input:
# N lines of words
# quit!

american_words = []

while True:
    word = input()
    if word == "quit!":
        exit()
    # len(word) < 64
    index = 0
    #american_vowel = "a, e, i,o, u, y"
    while index < len(american_words):
       if len(word) >= 4 and word[-2:] == "or" and word[-3] != "a, e, i, o, u, y":
            american_words[index] = word[:-2] + "our"
        index += 1


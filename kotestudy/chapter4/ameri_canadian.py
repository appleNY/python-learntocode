# https://dmoj.ca/problem/ccc02j2

# change "or" to "our"
# The rules for the word has more than four letters
# has a suffix consisting of a consonant followed by or
# type "quit!", the program should terminate

# input:
# N lines of words
# quit!

canadian_words = []

while True:
    american_words = input()
    if american_words == "quit!":
        exit()
    canadian_words.append(american_words)
    # len(word) < 64

    index = 0
    #american_vowel = "a, e, i,o, u, y"
    while index < len(canadian_words):
        american_words = canadian_words[index]
        if len(american_words) >= 4 and american_words[-2:] == "or" and american_words[-3] != "a, e, i, o, u, y":
            canadian_words[index] = american_words[:-2] + "our"
        index += 1

# output:
# replaced words

    for american_words in canadian_words:
        print(canadian_words)
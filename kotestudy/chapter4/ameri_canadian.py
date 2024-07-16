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
    american_words = input()
    if american_words == "quit!":
        exit()
   # len(words) < 64

    if len(american_words) >= 4 and american_words[-3:-2] != "a, e, i, o, u, y" and american_words[-2:] == "or":
        canadian_words = american_words[:-2] + "our"
        # output:
        # replaced words
        print(canadian_words)
    else:
        print(american_words)


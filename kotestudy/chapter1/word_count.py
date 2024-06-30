#https://dmoj.ca/problem/dmopc15c7p2

line = input()
if len(line) > 80 or len(line) == 0:
    exit()
# 단어는 영문 소문자로만 제공됨

word_count = line.count(' ') + 1
print(word_count)

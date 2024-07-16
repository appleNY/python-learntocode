#https://dmoj.ca/problem/ccc11s2

test_num = int(input())
if test_num < 0 or test_num > 10000:
    exit()

answer = ""  #student answer
for i in range(test_num):
    answer = answer + input()
    if "ABCDE".find(answer[i]) == -1:
        exit()
    
correct = ""  #correct answer
for j in range(test_num):
    correct = correct + input()
    if "ABCDE".find(correct[j]) == -1:
        exit()

correct_num = 0  #number of correct
for z in range(test_num):
    if answer[z] == correct[z]:
        correct_num = correct_num + 1

print(correct_num)

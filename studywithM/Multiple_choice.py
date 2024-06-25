student_num = int(input())
if student_num < 0 or student_num > 10000:
    exit()

correct_answer = 0
for i in range(2):
    for j in range(student_num):
        if i == 0:      #student answer
            if j == 0:
                student1 = input()
                if len(student1) != 1 or "ABCDE".find(student1) == -1:
                    exit()
            elif j == 1:
                student2 = input()
                if len(student2) != 1 or "ABCDE".find(student2) == -1:
                    exit()
            elif j == 2:
                student3 = input()
                if len(student3) != 1 or "ABCDE".find(student3) == -1:
                    exit()
        else:           #correct answer
            if j == 0:
                correct1 = input()
                if len(correct1) != 1 or "ABCDE".find(correct1) == -1:
                    exit()
                if student1 == correct1:
                    correct_answer += 1
            elif j == 1:
                correct2 = input()
                if len(correct2) != 1 or "ABCDE".find(correct2) == -1:
                    exit()
                if student2 == correct2:
                    correct_answer += 1
            elif j == 2:
                correct3 = input()
                if len(correct3) != 1 or "ABCDE".find(correct3) == -1:
                    exit()
                if student3 == correct3:
                    correct_answer += 1

print(correct_answer)
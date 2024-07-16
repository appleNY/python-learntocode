#https://dmoj.ca/problem/coci08c1p2

#three students want to join bird lover's club
#pass the entrance exam
#they are trying to guess the correct answers
#each students suggest the best answer by sequence
#Adrian: ABCABCABC
#Bruno: BABCBABC
#Goran: CCAABBCCAABB

adria_pattern = ["A", "B", "C"]
branka_pattern = ["B", "A", "B", "C"]
goran_pattern = ["C", "C", "A", "A", "B", "B"]

adria_score = 0
branka_score = 0
goran_score = 0

#input:
#number of questions, N
#correct answer

N = number_of_questions = int(input())
correct_answer = input()

for i in range(N):
    if correct_answer[i] == adria_pattern[i % len(adria_pattern)]:
        adria_score += 1
    if correct_answer[i] == branka_pattern[i % len(branka_pattern)]:
        branka_score += 1
    if correct_answer[i] == goran_pattern[i % len(goran_pattern)]:
        goran_score += 1
# used the solution to the slot_machine
# if i = 0, 0 % 3 == 0: adria_pattern[0] = "A"
# if i = 1, 1 % 3 == 1: adria_pattern[1] = "B"
# if i = 2, 2 % 3 == 2: adria_pattern[2] = "C"
# the pattern repeats as i increases
# same as branka and goran

# output:
# the largest number of correct answers one of the three boys gets, max score
# determines who of the three was right

max_score = max(adria_score, branka_score, goran_score)

print(max_score)
if adria_score == max_score:
    print("Adrian")
if branka_score == max_score:
    print("Bruno")
if goran_score == max_score:
    print("Goran")
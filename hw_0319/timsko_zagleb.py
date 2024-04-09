# https://dmoj.ca/problem/coci10c1p1
# 문제 해설 : University of Zagreb 는 매년 informatics 경연대회에 참가할 학생팀을 결성하고 있다. 각 팀은 3명의 학생으로 이루어져 있다.
# 대체적으로 여학생들이 더 우수해서 남학생보다 많은 수가 뽑혔는데, 올해는 남학생들의 주장이 받아들여져 1명의 남학생과 2명의 여학생으로 팀을 구성하기로 했다.
# 학교장이 조금 더 어렵게 선수를 선발하기 위해 올해부터는 K명의 학생을 무조건 인턴십을 보내기로 했고, 그들을 경쟁에 참가하지 못한다.
# 여학생 경쟁자 M명과 남학생 경쟁자 N명, 그리고 인턴쉽을 가게 될 경쟁자 K명이 주어진다면 학교장이 경쟁자들로 구성된 최대 수의 참가 팀을 구성해야 한다.
# 예를 들어, M이 6 N이 3, K가 2라면 여학생 1명과 남학생 1명을 인턴쉽을 보내고 남은 여학생 5명과 남학생 2명으로 최대 2팀을 만들 수 있다.
# 이때 여학생이 1명 남는다.
# input: 한 칸의 빈칸으로 구분된 3개의 정수를 한줄로 입력받는다. 단, 0 <= M(여학생) <= 100, 0 <= N(남학생) <= 100, 0 <= K(인턴쉽) <= M + n
# output: 단 하나의 정수, 즉 구성할 수 있는 팀의 최대 수

# 인턴 수가 0이 될 때까지, 이 상황에서 여학생 수에서 2를 빼고 남학생 수에서 1을 빼 나가며 팀 구성을 하는 것.

female_num, male_num, intern_num = map(int, input().split(" "))

if (female_num < 0 or female_num > 100 or male_num < 0 or male_num > 100 or intern_num < 0
        or intern_num > female_num + male_num):
    exit()

teams = 0

while intern_num >= 0:
    for i in range(female_num):
        female_num -= 2
        male_num -= 1
        teams += 1
        if male_num == 0:
            exit()


print(teams)

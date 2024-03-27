#https://dmoj.ca/problem/coci10c1p1

female_num, male_num, intern_num = map(int, input().split(" "))

team_members = (female_num // 2) + (male_num // 1)

if female_num < 0 or female_num > 100 or male_num < 0 or male_num > 100 or intern_num < 0 or intern_num > female_num + male_num:
    exit()

while intern_num >= 0:
    teams = 0


for i in range(intern_num):



print(teams)
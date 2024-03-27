#https://dmoj.ca/problem/coci10c1p1

female_num, male_num, intern_num = map(int, input().split(" "))

if female_num < 0 or female_num > 100 or male_num < 0 or male_num > 100 or intern_num < 0 or intern_num > female_num + male_num:
    exit()

teams = 0
team_members = (female_num // 2) + (male_num // 1)

for i in range(intern_num):


print(teams)
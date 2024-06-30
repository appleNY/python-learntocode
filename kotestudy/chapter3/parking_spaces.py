#https://dmoj.ca/problem/ccc18j2

n = int(input()) #parking spaces
if n < 1 or n > 100:
    exit()

yesterday = input() #parking information in yesterday
for char in yesterday:
    if char != "C" or ".":
        exit()

today = input() #parking information in today
for char in today:
    if char != "C" or ".":
        exit()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1

print(occupied)

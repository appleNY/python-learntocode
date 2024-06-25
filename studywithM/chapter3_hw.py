n = int(input())
yesterday = input()
today = input()

occupied = 0
index = 0

for char in yesterday:
    if char == 'C' and today[index] == 'C':
        occupied = occupied + 1
    index = index + 1

print(occupied)

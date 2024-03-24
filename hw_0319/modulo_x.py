modulo = 42

text = str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)
text = text + ' ' + str(int(input()) % modulo)

unique_count = 1

numbers = text.split()

for x in range(len(numbers)):
    is_unique = True
    for y in range(x):
        if numbers[x] == numbers[y]:
            is_unique = False
            break
    if is_unique:
        unique_count = unique_count + 1

print(unique_count)
#https://dmoj.ca/problem/coci18c3p1

line = input()
if len(line) < 1 or len(line) > 100000:
    exit()

HONI_block = 0

finding_letter = 'H'

for char in line:
    if char == finding_letter:
        if finding_letter == 'H':
            finding_letter = 'O'
        elif finding_letter == 'O':
            finding_letter = 'N'
        elif finding_letter == 'N':
            finding_letter = 'I'
        elif finding_letter == 'I':
            HONI_block = HONI_block + 1
            finding_letter = 'H'

print(HONI_block)

line = input()
honi_block = 0

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
            honi_block = honi_block + 1
            finding_letter = 'H'

print(honi_block)

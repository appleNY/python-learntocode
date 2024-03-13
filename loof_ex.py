password = input()

lowercase_letter = 0
uppercase_letter = 0
digit_letter = 0

if 8 <= len(password) <= 12:
    for char in password:
        if char.islower():
            lowercase_letter = lowercase_letter + 1
        elif char.isupper():
            uppercase_letter = uppercase_letter + 1
        elif char.isdigit():
            digit_letter = digit_letter + 1
    if lowercase_letter >= 3 and uppercase_letter >= 2 and digit_letter >= 1:
        print('Valid')
    else:
        print('Invalid')

else:
    print('Invalid')
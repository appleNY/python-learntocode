#https://dmoj.ca/problem/ccc18j1

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1 < 0 or num1 > 9 and num2 < 0 or num2 > 9 and num3 < 0 or num3 > 9 and num4 < 0 or num4 > 9:
    exit()

if ((num1 != 8 and num1 != 9)
        or (num4 != 8 and num4 != 9)
        or (num2 != num3)):
    print('answer')
else:
    print('ignore')

if not ((num1 == 8 or num1 == 9)
        and (num4 == 8 or num4 == 9)
        and (num2 == num3)):
    print('answer')
else:
    print('ignore')

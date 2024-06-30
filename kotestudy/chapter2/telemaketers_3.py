#https://dmoj.ca/problem/ccc18j1

num1 = int(input())
if num1 != 8 and num1 != 9:
    print('answer')
    exit()

num2 = int(input())
num3 = int(input())
if num2 != num3:
    print('answer')
    exit()

num4 = int(input())
if num4 != 8 and num4 != 9:
    print('answer')
    exit()

else:
    print('ignore')

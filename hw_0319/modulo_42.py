#https://dmoj.ca/problem/coci06c1p1

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())
num9 = int(input())
num10 = int(input())

distinct_num = 1

if num1 % 42 != num2 % 42:
    distinct_num = distinct_num + 1
elif num1 % 42 != num3 % 42 and num2 % 42 != num3 % 42:
    distinct_num = distinct_num + 2
elif num1 % 42 != num4 % 42 and num2 % 42 != num4 % 42 and num3 % 42 != num4 % 42:
    distinct_num = distinct_num + 3
elif (num1 % 42 != num5 % 42 and num2 % 42 != num5 % 42 and num3 % 42 != num5 % 42
      and num4 % 42 != num5 % 42):
    distinct_num = distinct_num + 4
elif (num1 % 42 != num6 % 42 and num2 % 42 != num6 % 42 and num3 % 42 != num6 % 42
      and num4 % 42 != num6 % 42 and num5 %42 != num6 % 42):
    distinct_num = distinct_num + 5
elif (num1 % 42 != num7 % 42 and num2 % 42 != num7 % 42 and num3 % 42 != num7 % 42
      and num4 % 42 != num7 % 42 and num5 %42 != num7 % 42 and num6 % 42 != num7 % 42):
    distinct_num = distinct_num + 6
elif (num1 % 42 != num8 % 42 and num2 % 42 != num8 % 42 and num3 % 42 != num8 % 42
      and num4 % 42 != num8 % 42 and num5 %42 != num8 % 42 and num6 % 42 != num8 % 42
        and num7 % 42 != num8 % 42):
    distinct_num = distinct_num + 7
elif (num1 % 42 != num9 % 42 and num2 % 42 != num9 % 42 and num3 % 42 != num9 % 42
      and num4 % 42 != num9 % 42 and num5 %42 != num9 % 42 and num6 % 42 != num9 % 42
        and num7 % 42 != num9 % 42 and num8 % 42 != num9 % 42):
    distinct_num = distinct_num + 8
elif (num1 % 42 != num10 % 42 and num2 % 42 != num10 % 42 and num3 % 42 != num10 % 42
      and num4 % 42 != num10 % 42 and num5 %42 != num10 % 42 and num6 % 42 != num10 % 42
        and num7 % 42 != num10 % 42 and num8 % 42 != num10 % 42 and num9 % 42 != num10 % 42):
    distinct_num = distinct_num + 9

print(distinct_num)

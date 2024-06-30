#https://dmoj.ca/problem/ccc15j1

month = int(input()) # 1 == January, 12 == December
day = int(input())

if month <= 0 or month > 12:
    exit()
if day <= 0 or day > 31:
    exit()

if month < 2:
    print('Before')
elif month == 2:
    if day < 18:
        print('Before')
    elif day > 18:
        print('After')
    elif day == 18:
        print('Special')
else:
    print('After')

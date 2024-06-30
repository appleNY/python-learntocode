#https://dmoj.ca/problem/dmopc16c1p0

width = int(input())
if width < 1 or width > 3:
    exit()
extra_cheese = int(input())
if extra_cheese < 0 or extra_cheese > 100:
    exit()

if width == 3 and extra_cheese >= 95:
    a = 'absolutely'
elif width == 1 and extra_cheese <= 50:
    a = 'fairly'
else:
    a = 'very'

print('C.C. is ' + a + ' satisfied with her pizza.')
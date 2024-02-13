width = int(input())
extra_cheese = int(input())

if width == 3 and extra_cheese >= 95:
    a = 'absolutely'
elif width == 1 and extra_cheese <= 50:
    a = 'fairly'
else:
    a = 'very'

print('C.C. is ' + a + ' satisfied with her pizza.')
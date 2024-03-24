#https://dmoj.ca/problem/coci07c1p1

x1_count = 0
x2_count = 0
y1_count = 0
y2_count = 0

x1 = -1
x2 = -1
y1 = -1
y2 = -1

for i in range(3):
    points = input()
    x = int(points[:points.find(" ") + 1])
    y = int(points[points.find(" "):])

    if x1 == -1:
        x1 = x
        x1_count = 1
    elif x1 == x:
        x1_count = x1_count + 1
    elif x2 == -1:
        x2 = x
        x2_count = 1
    elif x2 == x:
        x2_count = x2_count + 1

    if y1 == -1:
        y1 = y
        y1_count = 1
    elif y1 == y:
        y1_count = y1_count + 1
    elif y2 == -1:
        y2 = y
        y2_count = 1
    elif y2 == y:
        y2_count = y2_count + 1

result = ""
if x1_count == 1:
    result = str(x1)
elif x2_count == 1:
    result = str(x2)
result = result + " "
if y1_count == 1:
    result = result + str(y1)
elif y2_count == 1:
    result = result + str(y2)

print(result)

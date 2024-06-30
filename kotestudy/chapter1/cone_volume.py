#https://dmoj.ca/problem/dmopc14c5p1

radius = int(input())
height = int(input())
if radius < 1 or radius > 100 and height < 1 or height > 100:
    exit()

#직원뿔 부피 공식 : (pi * r * r * h)/3

PI = 3.141592
cone_volume = (PI * (radius ** 2) * height) / 3

print(cone_volume)

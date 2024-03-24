#https://dmoj.ca/problem/coci06c2p1

r1, s = map(int, input().split(' '))

if (r1 < -1000 or r1 > 1000) or (s < -1000 or s > 1000):
    exit()

r2 = (s * 2) - r1

print(r2)

#completed
#https://dmoj.ca/problem/wc15c2j1

N = int(input())
if N < 1 or N > 5:
    exit()

S = 'A long time ago in a galaxy ' + 'far, ' * N
T = S.strip(', ') #마지막 쉼표 제거를 위한 코드
star_wars = T + ' away...'
print(star_wars)

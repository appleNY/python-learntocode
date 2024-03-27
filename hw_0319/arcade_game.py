#https://dmoj.ca/problem/wc18c4j1

play_money = int(input())
payed_quarter = int(input())

if play_money < 0 or play_money > 6:
    exit()
if payed_quarter < 0 or payed_quarter > 21:
    exit()

quarters = play_money * 4

print(quarters - payed_quarter)
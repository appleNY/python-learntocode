#https://dmoj.ca/problem/wc18c3j1

P = int(input()) #litres of leftover paint
B = int(input()) #litres of paint which artfully covered on bottlecap
D = int(input()) #Pokédollar earned from selling badges

if P < 1 or P > 100 and B < 1 or B > 100 and D < 1 or D > 100:
    exit()

earning_money = ((P // B) * D) + (P % B)
print(earning_money)

#https://dmoj.ca/problem/wc17c1j2

celsius = int(input())
if celsius < -40 or celsius > 40:
    exit()

fahrenheit = (1.8 * celsius) + 32
#celsius = 5/9 * (fahrenheit - 32)

print(fahrenheit)

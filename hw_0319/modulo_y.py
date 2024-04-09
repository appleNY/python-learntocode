# https://dmoj.ca/problem/coci06c1p1

uniquemodulo_count = 0
uniqueHistory = ""

for i in range(10):
    inputNumber = int(input())
    modulo = inputNumber % 42
    if uniqueHistory.find(str(modulo)) == -1:
        uniqueHistory += "%" + str(modulo) + "%"
        uniquemodulo_count += 1
#그래서 기억속에서 결국 고유한게 몇개야
print(uniquemodulo_count)



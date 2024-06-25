n = int(input())

if n < 0 or n > 10000:
    exit()
elif 0 < n < 10000:
    tCount = 0
    TCount = 0
    sCount = 0
    SCount = 0
    for i in range(n):
        line = input()
        tCount = tCount + line.count('t')
        TCount = TCount + line.count('T')
        sCount = sCount + line.count('s')
        SCount = SCount + line.count('S')

    if tCount + TCount > sCount + SCount:
        print('English')
    elif tCount + TCount <= sCount + SCount:
        print('French')

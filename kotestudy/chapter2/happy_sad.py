#https://dmoj.ca/problem/ccc15j2

line = input()
if len(line) < 1 or len(line) > 255:
    exit()

happy_emotion = line.count(':-)')
sad_emotion = line.count(':-(')

if happy_emotion > sad_emotion:
    print('happy')
elif sad_emotion > happy_emotion:
    print('sad')
elif happy_emotion == sad_emotion and happy_emotion + sad_emotion > 0:
    print('unsure')
else:
    print('none')


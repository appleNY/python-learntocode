line = input()
happy_emotion = line.count(':-)')
sad_emotion = line.count(':-(')

if happy_emotion > sad_emotion:
    print('happy')
elif happy_emotion < sad_emotion:
    print('sad')
elif happy_emotion == sad_emotion and happy_emotion + sad_emotion > 0:
    print('unsure')
else:
    print('none')

composition = input()
tone = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '|']

for i in range(len(tone)):
    if (composition.count('A') + composition.count('D') + composition.count('E')
            > composition.count('C') + composition.count('F') + composition.count('G')):
        composition = 'A-mol'
    elif (composition.count('A') + composition.count('D') + composition.count('E')
          < composition.count('C') + composition.count('F') + composition.count('G')):
        composition = 'C-dur'
    elif (composition.count('A') + composition.count('D') + composition.count('E')
          == composition.count('C') + composition.count('F') + composition.count('G')):
        if composition[-1] == 'A' or composition[-1] == 'D' or composition[-1] == 'E':
            composition = 'A-mol'
        elif composition[-1] == 'C' or composition[-1] == 'F' or composition[-1] == 'G':
            composition = 'C-dur'

print(composition)

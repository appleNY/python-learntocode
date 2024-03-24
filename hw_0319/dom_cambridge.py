#https://dmoj.ca/problem/coci12c1p1

line = input()
if len(line) < 3 or len(line) > 100:
    exit()
if line.isupper() == False and line.isalpha() == False:
    exit()
elif line.isalpha() == True and line.isupper() == True:
    finding_letter = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
    for char in finding_letter:
        line = line.replace(char, "")

print(line)

#completed


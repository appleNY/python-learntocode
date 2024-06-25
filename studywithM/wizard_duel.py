# https://dmoj.ca/problem/coci18c4p1

obeyed_wizard = input()
if len(obeyed_wizard) != 1 or obeyed_wizard.isupper() == False or obeyed_wizard.isalpha() == False:
    exit(f"invalid obeyed_wizard:{obeyed_wizard}")

duel_count = int(input())
if duel_count < 1 or duel_count > 100:
    exit(f" invalid duel_count:{duel_count} (1 <= duel_count <= 100)")

obeyed_history = obeyed_wizard
for i in range(duel_count):
    duel = input()
    if len(duel) != 3 or duel[1] != " " or duel[0].isupper() == "False" or duel[0].isalpha() == "False" or duel[2].isupper() == "False" or duel[2].isalpha() == "False":
        exit(f"invalid duel:{duel}")
    if obeyed_wizard != duel[0] and obeyed_wizard == duel[2]:
        obeyed_wizard = duel[0]
        if obeyed_history.find(obeyed_wizard) == -1:
            obeyed_history = obeyed_history + obeyed_wizard

print(obeyed_wizard)
print(len(obeyed_history))
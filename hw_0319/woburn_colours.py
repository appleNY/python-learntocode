#https://dmoj.ca/problem/wc15c1j1

colours1 = input("RED" or "BLUE" or "WHITE")
colours2 = input("RED" or "BLUE" or "WHITE")

colours3 = ""

if colours1 == "RED" and colours2 == "BLUE":
    colours3 = "WHITE"
elif colours1 == "RED" and colours2 == "WHITE":
    colours3 = "BLUE"
elif colours1 == "BLUE" and colours2 == "WHITE":
    colours3 = "RED"

print(colours3)

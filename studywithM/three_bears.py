weight1 = int(input())
weight2 = int(input())
weight3 = int(input())

if ((weight1 > weight2) and (weight1 < weight3)) or ((weight1 > weight3) and (weight1 < weight2)):
    mama_bowl = weight1
elif ((weight2 > weight3) and (weight2 < weight1)) or ((weight2 < weight3) and (weight2 > weight1)):
    mama_bowl = weight2
else:
    mama_bowl = weight3

print(mama_bowl)

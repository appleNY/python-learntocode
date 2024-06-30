#https://dmoj.ca/problem/ccc06j1

burger1 = 461
burger2 = 431
burger3 = 420
burger4 = 0

burger_select = int(input())
if burger_select == 1:
    burger_calorie = burger1
elif burger_select == 2:
    burger_calorie = burger2
elif burger_select == 3:
    burger_calorie = burger3
else:
    burger_calorie = burger4

side1 = 100
side2 = 57
side3 = 70
side4 = 0

side_select = int(input())
if side_select == 1:
    side_calorie = side1
elif side_select == 2:
    side_calorie = side2
elif side_select == 3:
    side_calorie = side3
else:
    side_calorie = side4

drink1 = 130
drink2 = 160
drink3 = 118
drink4 = 0

drink_select = int(input())
if drink_select == 1:
    drink_calorie = drink1
elif drink_select == 2:
    drink_calorie = drink2
elif drink_select == 3:
    drink_calorie = drink3
else:
    drink_calorie = drink4

dessert1 = 167
dessert2 = 266
dessert3 = 75
dessert4 = 0

dessert_select = int(input())
if dessert_select == 1:
    dessert_calorie = dessert1
elif dessert_select == 2:
    dessert_calorie = dessert2
elif dessert_select == 3:
    dessert_calorie = dessert3
else:
    dessert_calorie = dessert4

total_calorie = burger_calorie + side_calorie + drink_calorie + dessert_calorie

print('Your total Calorie count is ' + str(total_calorie) + '.')




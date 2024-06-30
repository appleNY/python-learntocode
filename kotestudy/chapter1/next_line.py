#https://dmoj.ca/problem/ccc13j1

youngest_age = int(input())
middle_age = int(input())
if youngest_age < 0 or youngest_age > 50 and middle_age < youngest_age or middle_age > 50:
    exit()

age_gap = middle_age - youngest_age
oldest_age = middle_age + age_gap
print(oldest_age)

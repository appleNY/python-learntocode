# https://dmoj.ca/problem/ccc20j2

# input:
# total amount of people, P
# number of people who infected on day0, N
# infected growth rate, R

P = total_amount_people = int(input())
N = infected_people_day0 = int(input())
R = infected_growth_rate = int(input())

# P <= 10 ** 7
# N <= P
# R <= 10

total_infected = N  # current_infected
days = 0

# output:
# number of the first day on which the total number of infected people is greater than P

while total_infected <= P:
    days = days + 1
    total_infected = total_infected + (N * (R ** days))
# repeat until the total number of infected people is equal to or less than P
# R times the number of infections per day
# total infected people is N + N(current infected people) * (growth rate * growth rate * growth rate...)

print(days)

#https://dmoj.ca/problem/ccc20j2

#input:
#total amount of people
#number of people who infected on day 1
#number of people infected the next day(day 2)

P = total_amount_people = int(input())  #P
N = infected_people_day0 = int(input())  #N
R = infected_people_next_day = int(input())  #R

days = 0

while P < N + (R * days):
    days = days + 1
    R = R * days
    if






#output: days until the entire population is infected
monthly_given_data = int(input())
n = int(input())

capacity = monthly_given_data

if monthly_given_data < 1 or monthly_given_data > 100:
    exit()
for i in range(n):
    usage = int(input())
    if usage > capacity:
        exit()
    elif usage <= capacity:
        capacity = capacity - usage + monthly_given_data
print(capacity + monthly_given_data)

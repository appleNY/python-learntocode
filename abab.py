k = int(input())

if k < 1 or k > 45:
    exit(f" invalid K:{k} (1 <= K <= 45)")

letter = "a"

for i in range(k):
    result = ""
    for d in letter:
        if d == "a":
            result = result + "b"
        elif d == "b":
            result = result + "ba"
    letter = result

count_a = 0
count_b = 0

for c in letter:
    if c == "a":
        count_a = count_a + 1
    elif c == "b":
        count_b = count_b + 1

print(f"{count_a} {count_b}")


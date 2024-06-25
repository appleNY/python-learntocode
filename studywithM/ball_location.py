swaps = input()
ball_location = 1

for swap_type in swaps:
    if swap_type == 'A':    # swap 1 and 2
        if ball_location == 1:
            ball_location = 2
        elif ball_location == 2:
            ball_location = 1
    elif swap_type == 'B':   # swap 2 and 3
        if ball_location == 2:
            ball_location = 3
        elif ball_location == 3:
            ball_location = 2
    elif swap_type == 'C':    # swap 1 and 3
        if ball_location == 1:
            ball_location = 3
        elif ball_location == 3:
            ball_location = 1
    # only A, B, C type

print(ball_location)

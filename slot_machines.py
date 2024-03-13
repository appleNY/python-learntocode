chips = int(input())
play_m1 = int(input())
play_m2 = int(input())
play_m3 = int(input())

play_num = 0

if chips < 0 or chips > 1000:
    exit()

while chips >= 1:
    chips = chips - 1
    machine_num = play_num % 3
    play_num = play_num + 1

    if machine_num == 0:
        play_m1 = play_m1 + 1
        play_m1 = play_m1 % 35
        if play_m1 == 0:
            chips = chips + 30
    elif machine_num == 1:
        play_m2 = play_m2 + 1
        play_m2 = play_m2 % 100
        if play_m2 == 0:
            chips = chips + 60
    elif machine_num == 2:
        play_m3 = play_m3 + 1
        play_m3 = play_m3 % 10
        if play_m3 == 0:
            chips = chips + 9

print(f'Martha plays {play_num} times before going broke.')

card = input().split(" ")

flag = True

left_players_A = 11
left_players_B = 11

for item in card:
    team, player = item.split('-')
    if left_players_A < 7 or left_players_B < 7:
        flag = False
        print(f'Team A - {left_players_A}; Team B - {left_players_B}')
        print("Game was terminated")
        break
    if team == "A":
        left_players_A -= 1
    else:
        left_players_B -= 1

if flag:
    print(f'Team A - {left_players_A}; Team B - {left_players_B}')
neighbourhood = list(map(int, (input().split('@'))))

input_command = input()
position = 0
hearts = 0
while input_command != 'Love!':
    jump_len = int(input_command.split()[1])
    position += jump_len

    if position >= len(neighbourhood):
        position = 0

    if neighbourhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighbourhood[position] -= 2
        if neighbourhood[position] == 0:
            print(f"Place {position} has Valentine's day.")


    #old elif position > len(neighbourhood):
    #     position = 0
    #     if neighbourhood[position] == 0:
    #         print(f"Place {neighbourhood[position]} already had Valentine's day.")
    #     else:
    #         neighbourhood[position] -= 2
    #     #         if neighbourhood[position] == 0:
    #     #             print(f"Place {position} has Valentine's day.")

    input_command = input()

print(f"Cupid's last position was {position}.")

if sum(neighbourhood) == 0:
    print(f'Mission was successful.')
else:
    counter = len([el for el in neighbourhood if el > 0])
    print(f'Cupid has failed {counter} places.')

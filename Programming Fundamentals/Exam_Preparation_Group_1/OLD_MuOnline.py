# rooms = input().split("|")
#
# health = 100
# bitcoins = 0
# is_alive = True
#
#
# for i in range(len(rooms)):
#     room = rooms[i]
#
#     command, number = room.split()   # different from the other code
#     number = int(number)             # different from the other code
#
#     if command == "potion":
#         temp = health
#         health += number
#         healed = number
#
#         if health > 100:
#             health = 100
#             healed = 100 - temp
#
#         print(f'You healed for {healed} hp.')
#         print(f'Current health: {health} hp.')
#
#     elif command == "chest":
#         bitcoins += number
#         print(f'You found {number} bitcoins.')
#     else:
#         health -= number
#         if health > 0:
#             print(f'You slayed {command}.')
#         else:
#             is_alive = False
#             print(f'You died! Killed by {command}.')
#             print(f'Best room: {i + 1}')
#             break
#
# if is_alive:
#     print(f"You've made it!")
#     print(f'Bitcoins: {bitcoins}')
#     print(f'Health: {health}')

rooms = input().split("|")

health = 100
total_bitcoins = 0
is_alive = True
for i in range(len(rooms)):
    room = rooms[i]

    args = room.split()
    command = args[0]
    number = int(args[1])

    if command == "potion":
        temp = health
        health += number
        healed = number

        if health > 100:
            health = 100
            healed = 100 - temp

        print(f'You healed for {healed} hp.')
        print(f'Current health: {health} hp.')

    elif command == "chest":
        total_bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            is_alive = False
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i + 1}')
            break

if is_alive:
    print(f"You've made it!")
    print(f'Bitcoins: {total_bitcoins}')
    print(f'Health: {health}')
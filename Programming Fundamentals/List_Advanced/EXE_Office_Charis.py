rooms = int(input())

room_counter = 0
free_chairs = 0
enough_chairs = True

while rooms > 0:
    # chairs_available, charis_count = input().split()
    room_counter += 1
    data = input().split()
    token = data
    chairs_available = len(token[0])
    people_taken_chairs = int(token[1])

    if chairs_available >= people_taken_chairs:
        free_chairs += chairs_available - people_taken_chairs
    else:
        enough_chairs = False
        print(f"{people_taken_chairs - chairs_available} more chairs needed in room {room_counter}")

    rooms -= 1

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')

# to_check

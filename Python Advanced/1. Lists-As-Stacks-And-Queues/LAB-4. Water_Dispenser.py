from collections import deque

water = int(input())

people = deque()

while True:  # пълни опашката с хора
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:  # извършва логиката на задачата
    tokens = input().split()  # разделя инпута
    command = tokens[0]
    if command == "End":
        print(f'{water} liters left')
        break
    elif command == "refill":
        water_to_refill = int(tokens[1])
        water += water_to_refill
    else:
        water_to_be_given = int(tokens[0])
        person = people.popleft()

        if water_to_be_given <= water:
            water -= water_to_be_given
            print(f'{person} got water')
        else:
            print(f'{person} must wait')

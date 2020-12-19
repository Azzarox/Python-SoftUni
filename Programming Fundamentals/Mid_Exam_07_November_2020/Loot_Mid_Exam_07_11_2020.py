treasure_chest = input().split("|")

line = input()
is_empty = False
while line != "Yohoho!":
    command, items = line.split(" ", 1)
    if command == "Loot":
        items = items.split()
        for i in range(len(items)):
            if items[i] not in treasure_chest:
                treasure_chest.insert(0, items[i])

    if command == "Drop":
        items = int(items)
        if 0 < items < len(treasure_chest):
            if treasure_chest[items] in treasure_chest:
                popped_item = treasure_chest.pop(items)
                treasure_chest.append(popped_item)

    if command == "Steal":
        count = int(items)
        if len(treasure_chest) <= count:
            is_empty = True

            print(", ".join(treasure_chest[:]))
            treasure_chest = []

        else:
            print(", ".join(treasure_chest[-count:]))
            treasure_chest = treasure_chest[:-count]

    line = input()

calculate = "".join(treasure_chest)

total = 0
for i in calculate:
    total += 1

if is_empty:
    print(f'Failed treasure hunt.')
else:
    total = total / len(treasure_chest)
    print(f'Average treasure gain: {total:.2f} pirate credits.')

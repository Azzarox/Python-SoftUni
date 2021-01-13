# 100/100 solo done

clothes_box = [int(el) for el in input().split()]

capacity_rack = int(input())

temp_cap_rack = capacity_rack
counter = 1

while clothes_box:
    cloth = clothes_box.pop()

    if cloth > temp_cap_rack:  # check if the item can be put in the rack (isn't bigger than rack capacity)
        temp_cap_rack = capacity_rack
        counter += 1

    if temp_cap_rack == 0:   # check if the rack is equal (no more space left) to 0
        temp_cap_rack = capacity_rack
        counter += 1

    temp_cap_rack -= cloth

print(counter)

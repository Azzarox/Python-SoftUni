# 100/100

clothes_box = [int(el) for el in input().split()]

capacity_rack = int(input())

temp_cap_rack = capacity_rack
counter = 1

while clothes_box:
    cloth = clothes_box.pop()
    if cloth > temp_cap_rack:
        temp_cap_rack = capacity_rack
        counter += 1
    if temp_cap_rack <= 0:
        temp_cap_rack = capacity_rack
        counter += 1
    temp_cap_rack -= cloth

print(counter)

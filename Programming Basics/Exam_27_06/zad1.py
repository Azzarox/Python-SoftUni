import math
count_bee = int(input())
count_flowers = int(input())

honey_made = count_flowers * count_bee * 0.21

honeycombs_made = honey_made / 100

thing = math.floor(honeycombs_made)

print(f'{thing} honeycombs filled.')
print(f'{honey_made - (thing*100):.2f} grams of honey left.')
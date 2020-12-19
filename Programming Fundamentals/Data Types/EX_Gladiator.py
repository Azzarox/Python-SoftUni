fights, helm_price,sword_price,shield_price,armor_price = \
int(input()),float(input()),float(input()),float(input()),float(input())

helmet,sword,shield,armor = 0, 0, 0, 0

counter = 0
for fight in range(1, fights + 1):
    if fight % 2 == 0:
        helmet += helm_price
    if fight % 3 == 0:
        sword += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        shield += shield_price
        counter += 1
        if counter == 2:
            armor += armor_price
            counter = 0

print(f"Gladiator expenses: {sum([helmet,sword,shield,armor]):.2f} aureus")


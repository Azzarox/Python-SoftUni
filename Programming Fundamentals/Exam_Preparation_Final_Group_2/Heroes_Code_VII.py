n = int(input())

heroes = {}


for _ in range(n):
    data = input()
    name, health, mana = data.split()
    health = int(health)
    mana = int(mana)
    heroes[name] = {"HP": health, "MP": mana}


command_data = input()

while not command_data == "End":
    command_data = command_data.split(" - ")
    command = command_data[0]

    if command == "CastSpell":
        hero_name = command_data[1]
        mp_needed = int(command_data[2])
        spell_name = command_data[3]
        if mp_needed <= heroes[hero_name]["MP"]:
            heroes[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        hero_name = command_data[1]
        damage = int(command_data[2])
        attacker = command_data[3]
        if damage < heroes[hero_name]["HP"]:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        elif damage >= heroes[hero_name]["HP"]:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        hero_name = command_data[1]
        amount = int(command_data[2])
        if heroes[hero_name]['MP'] + amount >= 200:
            temp = heroes[hero_name]['MP']
            heroes[hero_name]['MP'] = 200
            print(f'{hero_name} recharged for {200 - temp} MP!')
        else:
            heroes[hero_name]['MP'] += amount
            print(f'{hero_name} recharged for {amount} MP!')

    elif command == "Heal":
        hero_name = command_data[1]
        amount = int(command_data[2])
        if heroes[hero_name]['HP'] + amount >= 100:
            temp = heroes[hero_name]['HP']
            heroes[hero_name]['HP'] = 100
            print(f'{hero_name} healed for {100 - temp} HP!')
        else:
            heroes[hero_name]['HP'] += amount
            print(f'{hero_name} healed for {amount} HP!')

    command_data = input()

sorted_members = sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0]))

for member, value in sorted_members:
    print(member)
    print(f'  HP: {value["HP"]}')
    print(f'  MP: {value["MP"]}')

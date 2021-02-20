# # 60/100

# velizar

# def get_item_cost(item):
#     return items_cost_dict[item]
#
#
# def get_inventory_cost(inventory):
#     return sum([get_item_cost(item) for item in inventory])
#
#
# heroes = input().split(", ")
#
# heroes_dict = {hero: set() for hero in heroes}
# items_cost_dict = {}
#
# command = input()
# while not command == "End":
#     name, item, cost = command.split('-')
#     cost = int(cost)
#
#     heroes_dict[name].add(item)
#     items_cost_dict[item] = cost
#
#     command = input()
#
# [print(f"{name} -> Items: {len(inventory_items)}, Cost: {get_inventory_cost(inventory_items)}")
#  for name, inventory_items
#  in heroes_dict.items()]

# ines

names = input().split(", ")

data = input()

heroes = {name: {} for name in names}

while not data == "End":
    name, item, price = data.split("-")
    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    data = input()

print(
    *[f"{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}"
      for name, inventory in heroes.items()], sep="\n"
)

# heroes.items() = [('Peter', {'Sword': 20, 'Shield': 10}), ('George', {'Gem': 100, 'Sword': 20})]
# name = Peter
# inventory = {'Sword': 20, 'Shield': 10}
# for item in inventory = sword,shield # върти през ключовете защото няма .items() на дикт-а
# inventory[item] = 20,10 - достъпва числото value към ключ item


# refactored
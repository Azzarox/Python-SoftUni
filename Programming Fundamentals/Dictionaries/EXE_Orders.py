# With One Nested Dictionary

command = input()

journal_name = {}

while not command == "buy":
    args = command.split()
    name = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if name not in journal_name:
        journal_name[name] = {"price": price, "quantity": quantity}
    else:
        journal_name[name]["price"] = price
        journal_name[name]["quantity"] += quantity

    command = input()

for key in journal_name:
    total = journal_name[key]["price"] * journal_name[key]["quantity"]
    print(f'{key} -> {total:.2f}')


# With Two Dictionaries

# product_prices = {}
# product_quantities = {}
# data = input()
#
# while not data == "buy":
#     product, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product not in product_prices:
#         product_prices[product] = price
#         product_quantities[product] = quantity
#     else:
#         product_prices[product] = price
#         product_quantities[product] += quantity
#     data = input()
#
# for product, price in product_prices.items():
#     total = price * product_quantities[product]
#     print(f'{product} -> {total:.2f}')

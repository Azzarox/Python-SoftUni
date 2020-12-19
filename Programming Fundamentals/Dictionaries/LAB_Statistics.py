product_data = input()

dictionary = {}

while not product_data == "statistics":
    product, quantity = product_data.split(": ")
    quantity = int(quantity)
    if product not in dictionary:
        dictionary[product] = quantity
    else:
        dictionary[product] += quantity

    product_data = input()

print("Products in stock:")
for key, value in dictionary.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(dictionary)}')
print(f'Total Quantity: {sum(dictionary.values())}')

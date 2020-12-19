elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
    # value = int(elements[i + 1])
    # bakery[key] = value

print(bakery)


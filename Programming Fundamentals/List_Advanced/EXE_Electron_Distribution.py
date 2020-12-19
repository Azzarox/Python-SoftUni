total_electrons = int(input())

res = []
shield = 1
while total_electrons > 0:
    value = 2 * shield ** 2

    if total_electrons < value:
        res.append(total_electrons)
    else:
        res.append(value)

    total_electrons -= value
    shield += 1

print(res)

# to_check

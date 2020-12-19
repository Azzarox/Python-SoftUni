def total(text, num):
    if text == "coffee":
        return 1.50 * num
    elif text == "coke":
        return 1.40 * num
    elif text == "water":
        return 1.00 * num
    elif text == "snacks":
        return 2.00 * num


food = input()
quantity = int(input())

print(f'{total(food, quantity):.2f}')

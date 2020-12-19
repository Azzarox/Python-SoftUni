def calculator(text, num_1, num_2):
    if text == "multiply":
        return num_1 * num_2
    elif text == "divide":
        return num_1 // num_2
    elif text == "add":
        return num_1 + num_2
    elif text == "subtract":
        return num_1 - num_2


operator = input()
number_1 = int(input())
number_2 = int(input())

print(calculator(operator, number_1, number_2))

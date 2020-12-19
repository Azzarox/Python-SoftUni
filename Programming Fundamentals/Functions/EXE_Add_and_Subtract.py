def add_and_subtract(num_1, num_2, num_3):
    def total():
        return num_1 + num_2

    def subtract():
        return total() - num_3

    return subtract()


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))


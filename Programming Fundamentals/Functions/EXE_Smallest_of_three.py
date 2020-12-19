def smallest(num_1, num_2, num_3):
    minimum = min([num_1, num_2, num_3])
    return minimum
    # return min(num_1, num_2, num_3)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest(number_1, number_2, number_3))

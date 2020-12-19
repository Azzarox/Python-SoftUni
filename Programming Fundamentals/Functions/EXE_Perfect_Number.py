def perfect_number(num):

    divisors = []
    for number in range(1, num):
        if num % number == 0:
            divisors.append(number)

    if sum(divisors) == num:
        return True

    return False


number_input = int(input())
if perfect_number(number_input):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
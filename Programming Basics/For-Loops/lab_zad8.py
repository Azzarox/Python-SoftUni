# min_number = sys.maxsize
# max_number = -sys.maxsize

import sys

min_number = sys.maxsize
max_number = -sys.maxsize

number = int(input())

for i in range(number):                   #in range(number) - za da vkluchi i nulata
    current_number = int(input())
    if current_number < min_number:       #if1 trqbva da proveri i dvete a ne s elif
        min_number = current_number
    if current_number > max_number:       #if2 trqbva da proveri i dvete a ne s elif
        max_number = current_number


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
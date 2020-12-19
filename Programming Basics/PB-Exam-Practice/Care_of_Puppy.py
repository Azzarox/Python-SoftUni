food = int(input())

line = ''
total = 0
while True:
    line = input()
    if line == "Adopted":
        break
    food_eaten = int(line)
    total += food_eaten

diff = abs(total - (food*1000))
if total <= (food*1000):
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')

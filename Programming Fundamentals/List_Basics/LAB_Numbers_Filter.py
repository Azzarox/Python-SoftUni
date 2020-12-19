n = int(input())

negative = []
positive = []
odd = []
even = []
all = [negative,positive,odd,even]
for _ in range(n):
    number = int(input())
    if number < 0:
        negative.append(number)
    if number >= 0:
        positive.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

command = input()
if command == "positive":
    print(positive)
elif command == 'negative':
    print(negative)
elif command == "odd":
    print(odd)
else:
    print(even)


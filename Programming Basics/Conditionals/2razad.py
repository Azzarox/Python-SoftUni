number = int(input())
bonus_points = 0

if number <= 100:
    bonus_points += 5
elif number > 1000:
    bonus_points += number * 0.1
else:
    bonus_points += number * 0.2

if number % 2 == 0:
    bonus_points += 1
elif number % 10 == 5: # number % 5 == 0 no ako e 20 ili 40 vrustha 0 no ne zavursva na 5
    bonus_points += 2  #elif - zashtoto nqma kak da e chetno i da zavustvana 5

print(bonus_points)
print(number + bonus_points)
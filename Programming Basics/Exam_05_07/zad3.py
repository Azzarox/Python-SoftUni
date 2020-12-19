difficulty = int(input())
tricky = int(input())
pages_count = int(input())

type = ''
if difficulty >= 80 and tricky >= 80 and pages_count >= 8:
    type = "Legacy"

elif difficulty >= 80 and tricky <= 10 and (pages_count >= 0 or pages_count <= 0):
    type = "Master"

elif (difficulty >= 0 or difficulty<=0) and tricky >= 50 and pages_count >= 2:
    type = "Hard"
elif difficulty <= 30 and tricky <= 10 and pages_count <= 1:
    type = "Easy"
elif difficulty <= 10 and (tricky >= 0 or tricky <= 0) and (pages_count >= 0 or pages_count <= 0):
    type = "Elementary"
else:
    type = "Regular"


print(type)
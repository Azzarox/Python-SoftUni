factor = int(input())
count = int(input())

items = []

for item in range(1, count+1):
    if factor == 1:                        #ako factor 1 da subere items spisuka sus spisuk ot range(1,count+1)
        items.extend(range(1,count+1))
        break
    item *= factor
    items.append(item)

print(items)



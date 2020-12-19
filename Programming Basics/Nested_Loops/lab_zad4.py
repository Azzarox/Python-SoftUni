start = int(input())
end = int(input())
magic = int(input())

counter = 0
is_found = False

for first in range(start, end+1):
    for second in range(start , end+1):
        counter += 1
        if first + second == magic:
            is_found = True
            print(f'Combination N:{counter} ({first} + {second} = {magic})')
            break
    if is_found:
        break

if not is_found: # if is_found == False
    print(f'{counter} combinations - neither equals {magic}')
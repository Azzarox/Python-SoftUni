width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
cardbox_total = 0
while True:
    line = input()
    if line == "Done":
        if free_space > cardbox_total:
            print(f'{free_space - cardbox_total} Cubic meters left.')
            break
    new = int(line)
    cardbox_total += new
    if cardbox_total > free_space:
        print(f'No more free space! You need {abs(cardbox_total - free_space)} Cubic meters more.')
        break


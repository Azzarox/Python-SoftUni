
sizeA = int(input())
sizeB = int(input())
cake_size = sizeA * sizeB

total_pieces = 0
while True:
    line = input()

    if line == "STOP":
        if total_pieces < cake_size:
            print(f'{cake_size - total_pieces} pieces are left.')
            break
    pieces = int(line)
    total_pieces += pieces

    if total_pieces >= cake_size:
        print(f'No more cake left! You need {total_pieces - cake_size} pieces more.')
        break
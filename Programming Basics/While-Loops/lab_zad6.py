import sys

max_number = -sys.maxsize

while True:
    line = input()
    if line == "Stop":
        break
    number = int(line)              #trqbva da e int(line) a ne float(line)
    if number > max_number:
        max_number = number         #max_number = number , a ne number = max_number

print(max_number)

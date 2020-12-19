import sys

min_number = sys.maxsize

while True:
    line = input()
    if line == "Stop":
        break
    number = int(line)
    if number < min_number:
        min_number = number

print(min_number)

import re

pattern = r'(@#+)[A-Z][a-z0-9A-Z]{4,}[A-Z](@#+)'

n = int(input())

for _ in range(n):
    text = input()
    if re.match(pattern, text):  # re.match() - good for single line input
        digits = re.findall(r"\d", text)  # - re.findall() - returns a list and stores the digits, after we join them
        if digits:
            print(f'Product group: {"".join(digits)}')
        else:
            print('Product group: 00')
    else:
        print("Invalid barcode")




# my 

import re

text = input()

pattern = r">>(?P<item>([A-Za-z]+))<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"  # named groups

total = 0

print("Bought furniture:")

while text != "Purchase":
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group("item"))
        total += float(match.group("price")) * int(match.group("quantity"))

    text = input()

print(f"Total money spend: {total:.2f}")


# other

# import re
#
# pattern = r'>>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)'
#
# text = input()
#
# print('Bought furniture:')
#
# total = 0
# while text != "Purchase":
#
#     match = re.fullmatch(pattern,text)
#
#     if match is None:
#         text = input()
#         continue
#
#     print(match.group(1))
#     price = float(match.group(2))
#     quantity = int(match.group(4))
#     total += price * quantity
#
#     text = input()
#
# print(f'Total money spend: {total:.2f}')

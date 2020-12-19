# 100/100 - little_help - check for regex careful - regex

import re

text = input()
# pattern = r'(((?<=\s)|(?<=^))(::|\*\*)(?P<Word>[A-Z][a-z]{2,})\3)' #not working on 100 imo should be the better one (start of string/space)
# pattern = r((:{2} | \ * {2})(?P < Word >[A-Z][a-z]{2, })\2)

pattern = r'((::|\*\*)(?P<Word>[A-Z][a-z]{2,})\2)'
matches = re.finditer(pattern, text)

digits = re.findall(r"\d", text)

cool_threshold = 1
for digit in digits:
    digit = int(digit)
    cool_threshold *= digit

count = 0
emojis = []
emote_numbers = {}
for match in matches:
    count += 1
    match_dict = match.groupdict()
    num = [ord(el) for el in match_dict["Word"]]
    emote_name = match_dict["Word"]
    emote_numbers[emote_name] = sum(num)
    if emote_numbers[emote_name] > cool_threshold:
        emojis.append(match.group())

print(f'Cool threshold: {cool_threshold}')
print(f'{count} emojis found in the text. The cool ones are:')
for emoji in emojis:
    print(emoji)






# some other code
# import re
#
# text = input()
# pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
# matches = re.findall(pattern, text)
#
# threshold = 1
# for char in text:
#     if char.isdigit():
#         threshold *= int(char)
#
# cool_emojis = []
# for emoji in matches:
#     coolnes = 0
#     for char in emoji[1]:
#         coolnes += ord(char)
#
#     if coolnes > threshold:
#         cool_emojis.append(emoji)
#
# print(f'Cool threshold: {threshold}')
# if len(matches) > 0:
#     print(f'{len(matches)} emojis found in the text. The cool ones are:')
#     for emoji in cool_emojis:
#         print(''.join(emoji))

import re

pattern = r'(.+)>(?P<ONE>\d{3})\|(?P<TWO>[a-z]{3})\|(?P<THIRD>[A-Z]{3})\|(?!<|>)(?P<FOURTH>.{3})<\1'
number = int(input())

match_dict = {}
string = ""
for _ in range(number):
    text = input()
    matches = re.search(pattern, text)
    if matches is None:
        print('Try another password!')
    else:
        matches = re.finditer(pattern, text)
        for match in matches:
            match_dict = match.groupdict()
            string = match_dict["ONE"]+match_dict["TWO"]+match_dict["THIRD"]+match_dict["FOURTH"]
            print(f'Password: {string}')

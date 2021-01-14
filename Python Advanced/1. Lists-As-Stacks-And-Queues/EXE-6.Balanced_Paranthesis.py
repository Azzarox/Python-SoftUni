# 100/100 решение

line = input()

opening_brackets = []

mapper = {"{": "}", "[": "]", "(": ")"}

is_balanced = True

for ch in line:
    if ch in "{[(":                                     #
        opening_brackets.append(ch)                     # append-ваме само отварящите скоби в стака ex: ['{', '[', '(']
    else:                                               # щом е else значи със сигурност е затваряща скоба
        if not opening_brackets:                        # ако няма елементи в стака, прекъсва цикълът, защото няма как да pop() от empty list
            is_balanced = False
            break
        current_bracket = opening_brackets.pop()        # попваме последният item следователно е отваряща скоба
        if not mapper[current_bracket] == ch:           # проверяваме дали попнатият item е равен на текущият ch(затварящата скоба)
            is_balanced = False                         # щом не е значи break-ваме иначе продължава цикълаът до последният елемент от line
            break

if is_balanced:
    print("YES")
else:
    print("NO")

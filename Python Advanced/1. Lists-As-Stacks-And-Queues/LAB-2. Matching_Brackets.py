# по-сложното решение,  но fun

def brackets(text):
    stack = []

    string = []

    for index in range(len(text)):

        ch = text[index]

        if ch == "(":
            stack.append(index)  # append-ва индексът на който се намира скобата
        elif ch == ")":
            start_index = stack.pop()  # pop-ва индексът, на който е последната въведена скоба и запазва в start_index променливата
            string.append(text[start_index:index + 1])
            # ^^ добавя в нов лист string-ът от последната скоба (start_index) до индексът, на който се намира затварящата скоба

    for ele in string:
        print(ele)


brackets(input())

## по-лесно разбираемото решение

# stack = []
#
# brackets_input = input()
#
# for ch in brackets_input:  # върти през character-ите на string-а
#     if ch == "(":
#         stack.append("")  # ако намери "(" да добави място в stack-а
#
#     for index in range(len(stack)):
#         stack[index] += ch
#
#         # ^^  на индексът от стака да добавя character-ите (eдин по един те се въртят от външният for-loop
#     if ch == ")":
#
#         print(stack.pop())

# # stack python advanced lab 1
#
# string_input = input()
#
# stack = []
# for index in range(len(string_input)):
#     stack.append(string_input[index])
#
# # for _ in range(len(stack)): # същото като долното
# #     print(stack.pop(), end="")
#
# while stack:
#     print(stack.pop(), end="")

## NO:2 With function


from collections import deque


def stack_func_dq(text):
    stack = deque()

    for ch in text:  # for index in range(len(text)):
        stack.append(ch)  # stack.append(text[index])

    while len(stack) > 0:
        print(stack.pop(), end='')


stack_func_dq(input())

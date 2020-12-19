oscar = int(input())

if oscar == 88:
    print('Leo finally won the Oscar! Leo is happy')
elif oscar == 86:
    print(f'Not even for Wolf of Wall Street?!')
elif (oscar != 88 or oscar != 86) and oscar < 88:
    print(f'When will you give Leo an Oscar?')
elif oscar > 88:
    print(f'Leo got one already!')
#s=a^2 square
#s=a.b
#s = pi.r2
#s=a.ha

import math

name = input("")
s = 0
if name == "square":
    long = float(input())
    s = long**2
    print(f'{s:.3f}')
elif name == "rectangle":
    long_one = float(input())
    long_two = float(input())
    s = long_one * long_two
    print(f'{s:.3f}')
elif name == "circle":
    radius = float(input())
    s = math.pi * radius**2
    print(f'{s:.3f}')

elif name == "triangle":
    long = float(input())
    height = float(input())
    s = long * height / 2
    print(f'{s:.3f}')


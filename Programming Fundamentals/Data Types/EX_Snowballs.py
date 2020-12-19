import sys

n = int(input())
max_value = -sys.maxsize
snow = 0
time = 0
quality = 0

for i in range(n):
    snow,time,quality = int(input()),int(input()),int(input())
    value = (snow / time) ** quality
    if value > max_value:
        max_value = value
        ssnow,ttime,qquality = snow,time,quality


print(f'{ssnow} : {ttime} = {max_value:.0f} ({qquality})')

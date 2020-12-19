# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.

bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

bitcoin_to_leva = bitcoin_count * 1168
yuan_to_levas = yuan_count * 0.15 * 1.76
euros = (bitcoin_to_leva + yuan_to_levas) / 1.95

total = euros - (euros*(commission/100))
print(f'{total:.2f}')





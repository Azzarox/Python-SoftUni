pen_packets = int(input())
marker_packets = int(input())
cleaning_litre = float(input())
discount = int(input()) # / 100

total = (pen_packets * 5.80 + marker_packets * 7.20 + cleaning_litre * 1.20)
total -= total * discount/100
print(f'{total:.3f}')

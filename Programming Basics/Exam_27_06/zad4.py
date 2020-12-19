population = int(input())
years = int(input())

for i in range(1,years+1):  #tuka bqh prail mn promenlivi otkoito nqma smisul
    population += population//10 * 2                                             #population = population + (population//10 * 2)
    if i % 5 == 0: #tuka bqh pisal i == 5 koeto vadi drug reziltat
        population -= population//50 * 5                                         #population = population - (population//50) * 5
    population -= population // 20 * 2

print(population)
#soc stipendiq ili za uspeh
# soc stipendeiq trqbva:
    # dohod < minimal wage
    # uspeh nad 4.50
    # soc stipendiq e ravna na 0.35 * minimal wage

# stipendiq za uspeh
    # nad 5.50 vkluchitelno
    # stipendiqta e ravna na uspehut * 25
import math

income = float(input())
grade = float(input())
minimal_wage = float(input())

excellent_scholarship = 0
social_scholarship = 0

if grade >= 5.5:
    excellent_scholarship += grade * 25

if income < minimal_wage and grade > 4.5:
    social_scholarship += minimal_wage * 0.35

if social_scholarship > excellent_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
    else:
        print(f'You cannot get a scholarship!')

# summary
# nested ifs
# grade a e pogolqm ot 5.50 = > primerno 714lv stipendiq
# min wage-a e < ot dohod no imam 5.60 grade => zimam dvete stipendii
# ako socialnata e po golqma ot excelent -> vzimam neq (shott se vzima taq det e pogolqma suma)
# ako ne zimam excelent
# ako dvete sa ravni no ne sa nula zimam taq za otlichen uspeh
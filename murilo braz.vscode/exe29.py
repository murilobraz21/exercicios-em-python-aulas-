salario=float(input("digite o salario atual?"))

#salario ate 280
salario1=salario*0.20
salario2=salario1+salario
#salario de 280 ate 700 
salario3=salario*0.15
salario4=salario3+salario
#salario de 700 ate 1500
salario5=salario*0.10
salario6=salario5+salario
#salario maior que 1500
salario7=salario*0.5
salario8=salario+salario7

if salario <281.00:
    print("o salario era",salario)
    print("o valor do reajuste e de 20%")
    print("o valor do aumento e de",salario1)
    print("o novo valor do salario e de ",salario2)

if salario>282.00 and salario <700.00:
    print("o salario era",salario)
    print("o valor do reajuste e de 15%")
    print("o valor do aumento e de",salario3)
    print("o novo valor do salario e de ",salario4)

if salario>701.00 and salario <=1500.00:
    print("o salario era",salario)
    print("o valor do reajuste e de 10%")
    print("o valor do aumento e de",salario5)
    print("o novo valor do salario e de ",salario6)

if salario>1501.00:
    print("o salario era",salario)
    print("o valor do reajuste e de 10%")
    print("o valor do aumento e de",salario7)
    print("o novo valor do salario e de ",salario8)

else:
    print("fim do progama")



    



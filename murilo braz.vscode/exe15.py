#11% ir
#8% inss
#5% sindicato
#nao usar virgula(,) se nao ta erro use (.) se o valor da hora quanha diver centavos ex(4.75)< esta certo use (.)

ganhos=float(input("quanto voce ganha por hora?"))
horas=float(input("quantas horas voce trapalhar por mes?"))

mes=(ganhos*horas)
print(mes)


ir=mes*0.11
inss=mes*0.08
sind=mes*0.05

print("salario bruto por mes",mes)
print("desconto do imposto de renda",ir)
print("desconto do inss {:.2f} ".format(inss))
print("desconto do sindicato",sind)
salarioliquido=mes-ir-inss-sind
print("seu salario liquido e de{:.2f}".format(salarioliquido))


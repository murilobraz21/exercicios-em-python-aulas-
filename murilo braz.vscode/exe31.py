ganhos=float(input("quanto voce ganha por hora?"))
horas=float(input("quantas horas voce trapalhar por mes?"))

salario=(ganhos*horas)

sind=salario*0.03

fgts=salario*0.11


if salario>0 and salario <900:
    print("1")
    print("insento")

if salario>901 and salario <1500:
    print("2")
    ir=salario*0.05
    salarioliquido=salario-ir-sind
    totaldesconto=ir+sind
    print("seu salario bruto e de",salario)
    print("seu imposto de renda e",ir)
    print("seu valor do sindicato e de",sind)
    print("o valor do fgts e de",fgts)
    print("o valor do fgts nao e descontado")
    print("total de descontos e de",totaldesconto)
    print("o seu salario liquido e de",salarioliquido)


if salario>1501 and salario <2500:
    print("3")
    ir2=salario*0.10
    salarioliquido1=salario-ir2-sind
    totaldesconto1=ir2+sind
    print("seu salario bruto e de",salario)
    print("seu imposto de renda e",ir2)
    print("seu valor do sindicato e de",sind)
    print("o valor do fgts e de",fgts)
    print("o valor do fgts nao e descontado")
    print("total de descontos e de",totaldesconto1)
    print("o seu salario liquido e de",salarioliquido1)

if salario>2501:
    print("4")
    ir3=salario*0.20
    salarioliquido2=salario-ir3-sind
    totaldesconto2=ir3+sind
    print("seu salario bruto e de",salario)
    print("seu imposto de renda e",ir3)
    print("seu valor do sindicato e de",sind)
    print("o valor do fgts e de",fgts)
    print("o valor do fgts nao e descontado")
    print("total de descontos e de",totaldesconto2)
    print("o seu salario liquido e de",salarioliquido2)


  
  
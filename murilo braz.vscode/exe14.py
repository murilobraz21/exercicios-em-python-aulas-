#peso dopeixe nao pode ser maior que 50 quilos
#multa e de 4 reais por quilo
# variaveis quanto quilos passou e quanto de multa

peso=int(input("quanto quilos tem o peixe49?"))



if peso>49:
    print("seu peixe esta com ")
    print(peso,"quilos")
#quanto foi o exedente
    resultado1=peso-50
    print("o pesso exedente foi de")
    print(resultado1,"quilos")

#multa

    multa=resultado1*4
    print("sua multa por quilo exedente sera de")
    print(multa,"reais")


elif peso<50:
    multa0=print("liberado")   

     
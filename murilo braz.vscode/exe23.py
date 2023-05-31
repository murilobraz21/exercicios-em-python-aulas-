nota1=float(input("qual a primeira nota?"))
nota2=float (input("qual a segunda nota?"))

resultado=(nota1+nota2)/2

if resultado==10:
    print("aprovado com distincao")
elif resultado >6:
    print("aprovado")
elif resultado<7:
    print("reprovado")
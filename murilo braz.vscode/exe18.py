#tamanho de um arquivo para download (em MB) e a velocidade de
#um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
#este link (em minutos)

arquivomb=float(input("qual e o tamanho do arquivo?"))
velocidadembps=float(input("qual a velocidade do link"))

#1 mb = 1000ky
#1 megabit = 1000quilobit

resultado1=arquivomb*1000
resultado2=velocidadembps*8000

print(resultado1)
print(resultado2)

resultado4=resultado2*133,3
print(resultado4)

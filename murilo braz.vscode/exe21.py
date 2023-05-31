print("digite o nome de 6 cidades")
cidade1=str(input("cidade-1?"))
cidade2=str(input("cidade-2?"))
cidade3=str(input("cidade-3?"))
cidade4=str(input("cidade-4?"))
cidade5=str(input("cidade-5?"))
cidade6=str(input("cidade-6?"))

dic1={"cidade1":cidade1,"cidade2":cidade2,"cidade3":cidade3,"cidade4":cidade4,"cidade5":cidade5,"cidade6":cidade6}
dic2=cidade1+cidade2+cidade3+cidade4+cidade5+cidade6


if dic1==dic2:
    print("nao existe nomes iguais")
elif dic1!=dic2:
    print("existem nomes iguais porfavor tente novamente")

#terminar depois




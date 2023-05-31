num1=int(input("digite um numero?"))
num2=int(input("digite outro numero?"))
num3=float(input("digite outro numero?"))


#fazer depois

maior=num1
if num2>num1 and num2 > num3:
    maior=num2

if num3>num1 and num3>num2:
    maior=num3

menor=num1
if num2<num3 and num2<num1:
    menor=num2

if num3<num2 and num3<num1:
    menor=num3
print("o menor numero e {:.2f}".format(menor))
print("o maior numer e {:.2f}".format(maior))


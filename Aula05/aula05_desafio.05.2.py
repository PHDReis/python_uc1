nota1=float(input("Digite a primeira nota : "))
nota2=float(input("Digite a segunda nota : "))
tra_extra=input("Fez o trabalho extra ? <s/n> ")
tra_extra=tra_extra.lower()

nota_final=(nota1+nota2)/2

print (nota_final)
print (tra_extra)


if nota_final>=7:
    print("Parabéns, você passou! - nota ")

elif (nota_final<7) and (tra_extra=="s"):
    print("Parabéns, você passou! - trab ")

else:
    print("Infelizmente não foi dessa vez.")
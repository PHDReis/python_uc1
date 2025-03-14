print ("Quais os tipos de triângulos? ")
tri1=float(input("Digite o valor do 1º lado: "))
tri2=float(input("Digite o valor do 2º lado: "))
tri3=float(input("Digite o valor do 3º lado: "))

if (tri1==tri2==tri3): ## De forma mais segura pode ser usado assim: if (tri1==tri2)and(tri2==tri3):
    print("Esse é um triângulo Equilátero")
elif (tri1==tri2) or (tri1==tri3) or (tri2==tri3):
    print("Esse é um triângulo Isósceles")
else:
    print("Esse é um triângulo Escaleno")
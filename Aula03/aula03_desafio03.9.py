import math

a=float(input("Digite o valor para A: "))
b=float(input("Digite o valor para B: "))
c=float(input("Digite o valor para C: "))

delta=(b**2)-(4*a*c)

if delta < 0:
    print("Não existem raizes reais")

elif delta==0:
    x = -b/(2*a)
    print(f"A equação possui uma raiz real: {x}")

else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print(f"As raízes da equação são: {x1} e {x2}")

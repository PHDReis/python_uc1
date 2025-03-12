numero1_str=input("Digite o primeiro número: ")
numero1=float(numero1_str)
numero2_str=input("Digite o segundo número: ")
numero2=float(numero2_str)

if numero1>numero2:
    print(f"O maior número foi o {numero1} ")
elif numero2>numero1:
    print(f"O maior número foi o {numero2} ")
else:
    print("Os números foram iguais")
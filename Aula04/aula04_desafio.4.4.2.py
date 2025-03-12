idade_str=input("Digite sua idade : ")
idade=float(idade_str)

if idade>=16:
    print("Você pode votar!")
elif idade<16:
    print("Você ainda não pode votar.")

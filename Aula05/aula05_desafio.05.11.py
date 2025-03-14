prod=int(input("Quantos produtos você comprou? "))
valor=float(input("Qual o valor da compra? "))

if ((prod>=5) or (valor>=100)):
    print("Você ganhou desconto!")

else:
    print("Você não tem desconto :(")
prod=int(input("Quantos produtos você comprou? "))
valor=float(input("Qual o valor da compra? "))
desc=input("Usou cupom na última compra? <s/n> ")

if ((prod>=5) or (valor>=100)) and (desc=="n"):
    print("Você ganhou desconto!")

else:
    print("Você não tem desconto :(")
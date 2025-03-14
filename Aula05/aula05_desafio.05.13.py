idade=int(input("Digite sua idade : "))
acom=input("Você está com seus pais? <s/n>  ").lower()


if (idade>=18) or ((idade>=16) and (acom=="s")):
    print("Acesso liberado")
else:
    print("Acesso negado")
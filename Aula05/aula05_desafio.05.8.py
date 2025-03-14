idade=int(input("Digite sua idade: "))
cart=input("Você possui habilitação? <s/n> ").lower()

if (idade>=18) and (cart=="s"):
    print("Você pode dirigir!")
else:
    print("Você ainda não pode dirigir.")
idade=int(input("Digite sua idade: "))

if (idade>=18):
    print("Pode viajar! ")
elif (idade>=16):
    aut=input("Seus pais autorizaram? <s/n> ").lower()
    if (aut=="s"):
        print("Seus pais deixaram, pode viajar!")
    else:
        print("Sem autorização não dá!")
else:
    print("Você não pode viajar.")
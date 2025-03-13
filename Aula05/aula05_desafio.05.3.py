idade=int(input("Digite sua idade : "))
pais=input("Você está com seus pais? <s/n>  ")
pais=pais.lower()
lista=input("Está na lista de banidos? <s/n>  ")
lista=lista.lower()

if ((idade>=18) or (pais=="s")) and (lista=="n"):
    print("Acesso liberado")
else:
    print("Acesso negado")
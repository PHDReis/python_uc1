idade=int(input("Digite sua idade : "))
senha_correta=1234

if (idade>=18):
    senha=input("Informe a senha : ")
    if (senha==senha_correta):
        print("Acesso liberado")
    else:
        print("Acesso Negado")
else:
    print ("Acesso Negado - Idade")
login=input("Digite seu nome : ")
senha_str=input("Digite sua senha númerica : ")
senha=int(senha_str)
nome="admin"
liberado=1234

if login==nome:    
    if senha==liberado:
        print("Acesso permitido")
    else:
        print("Acesso negado")
else:
    print("Usuário não cadastrado")


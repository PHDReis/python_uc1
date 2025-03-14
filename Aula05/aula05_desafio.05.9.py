login=input("Digite seu Login: ").lower()


if (login=="admin"):
    senha=int(input("Digite sua senha: "))

    if (senha==1234):
        print("Acesso liberado! ")

    else:
        print("Senha inválida")
        
else:
    print("Usuário não autorizado.")
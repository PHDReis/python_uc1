nome=input("Digite um nome de usuário: ")
senha=input("Digite uma senha: ")


if (len(nome)<3):
    print("Nome Invalido")

elif (len(senha)<6):
    print("Senha Invalida")

elif (senha=="123456") or (senha=="senha"):
    print("Senha Fraca")

else:
    print("Cadastro realizado com sucesso")

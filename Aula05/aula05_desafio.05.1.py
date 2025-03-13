idade_str=int(input("Digite sua idade : "))
senha_str=int(input("Digite sua senha : "))

senha=1234

if (idade_str>=18) and (senha==senha_str):
    print("Acesso liberado")
else:
    print("Acesso negado")

    
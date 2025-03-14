idade=int(input("Digite sua idade: "))
renda=float(input("Qual sua renda atual? R$ "))
serasa=input("Seu nome está sujo? <s/n> ").lower()

if (idade>=21) and (renda>=2000) and (serasa=="n"):
    print("Você tem direito a um empréstimo!")
else:
    print("Você não tem empréstimo liberado no momento.")
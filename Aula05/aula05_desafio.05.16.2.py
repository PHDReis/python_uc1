idade=int(input("Digite sua idade: "))

if (idade>=21):
    renda=float(input("Qual sua renda atual? R$ "))

    if (renda>=2000):
        serasa=input("Seu nome está sujo? <s/n> ").lower()
        
        if (serasa=="n"):
            print("Você tem direito a um empréstimo!")
        
        else:
            print("Seu nome está sujo.")
    
    else:
        print("Você não tem renda suficiente.")
    
else:
    print("Você não tem idade mínima.")
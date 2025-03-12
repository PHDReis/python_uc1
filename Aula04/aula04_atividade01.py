idade_str=input("Qual a sua idade ? ")
idade=int(idade_str)

if idade>= 18 :
    print("Você é maior de idade.")
elif idade>=16 :
    print("Você é adolescente.")
else : 
    print("Você é criança.")
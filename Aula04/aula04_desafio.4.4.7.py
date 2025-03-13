print("Vamos calcular seu Indice de Massa Corporal? ")
peso_str=input("Digite seu peso atual: ")
peso=float(peso_str)
altura_str=input("Digite sua altura: ")
altura=float(altura_str)

imc=((peso**10)/(altura**2))

if imc<18.5:
    print("Você está abaixo do peso. ")
elif imc>=18.5 and imc<=24.9:
    print("Você está no seu peso ideal! ")
elif imc>=25 and imc<=29.9:
    print("Você está com sobrepeso. ")
else:
    print("Você está obeso.")
    
    
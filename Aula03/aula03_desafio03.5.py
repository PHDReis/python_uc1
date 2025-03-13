print("Vamos calcular seu índice de massa corporal?")
peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura centimetros: "))

imc=peso/(altura/100)**2

print("Seu IMC é: ", imc)
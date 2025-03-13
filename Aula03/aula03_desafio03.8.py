valor_invest=float(input("Digite o valor investido: "))
taxa=float(input("Digite a taxa de juros: "))
tempo=int(input("Digite por quantos meses o valor ficará investido: "))

juros=valor_invest*(taxa/100)*tempo
valor_final=valor_invest+juros

print(f"O valor final será de R$ {valor_final:.2f}")
print(f"O valor ganho de juros foi R$ {juros:.2f}")


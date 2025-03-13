salario=float(input("Digite o salário: "))
aumento=float(input("Qual o percentual de aumento? "))

valor=salario*(aumento/100)

print("O novo salário será de R$", salario+valor)
print("O aumento foi de R$", valor)
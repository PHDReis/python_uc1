print("Nuúmero mágico, você terá 3 tentativas para acertar um número entre 1 e 10")
numero1=int(input("Tentativa 1, digite o número: "))
numero2=int(input("Tentativa 2, digite o número: "))
numero3=int(input("Tentativa 3, digite o número: "))

numero_magico=5

if (numero1==numero_magico):
    print(f"Parabens, você acertou! O número mágico é {numero1} da 1ª tentativa")

elif (numero2==numero_magico):
    print(f"Parabens, você acertou! O número mágico é {numero2} da 2ª tentativa")

elif (numero3==numero_magico):
    print(f"Parabens, você acertou! O número mágico era {numero3} da 3ª tentativa")

else:
    print("Não foi dessa vez :(")

distancia=input("Qual a distancia em Km que você vai percorrer ? ")
distancia=float(distancia)
velocidade=input("Qual a velocidade média que você vai andar ? ")
velocidade=float(velocidade)

tempo=distancia/velocidade

print(f"Você levará {tempo:.2f} horas para chegar no seu destino")
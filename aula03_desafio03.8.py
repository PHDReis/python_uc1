real=input("Qual o valor em reais que você possui ?")
real=float(real)
dolar=input("Qual a cotação do dólar hoje ?")
dolar=float(dolar)

valor=real/dolar

print(f"Você possui $ {valor:.2f} em dólar")
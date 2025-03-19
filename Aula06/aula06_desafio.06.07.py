numero=float(input("Digite um número: "))
fatorial=1
contador=numero

while contador>1:
    fatorial*=contador
    contador-=1    

print(f"O fatorial do {numero} é {fatorial}")
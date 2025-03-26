"""
Aula 09 - Atividade 1
"""

vet_dados=[10, 20, 30, 40, 50]
vet_dados2=[3, 7, 2, 9, 4, 5, 1, 8, 6]
vet_dados3=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vet_dados4=[1, 3, 3, 4, 3, 5, 3, 7, 9, 8, 2, 1, 3]
vet_dados5=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



"""
Exemplo 1: Criando e imprimindo uma lista
"""

def criar_imprimir(vetor):
    print(f"\n\tO conteudo do vetor é: {vetor}\n")

"""
Exemplo 2: Interando sobre uma lista
"""
    
def interando(vetor):
    for elemento in vetor:
        print(f"\n\tOs elementos no vetor são: {elemento}\n")

"""
Exemplo 5: Calcular a soma dos elementos de um vetor
"""

def calcular(vetor):
    soma=sum(vetor)
    print(f"\n\tA soma dos elementos é: {soma}\n")

"""
Exemplo 6: Encontrar o maior e menor valor em um vetor
"""

def maior_menor(vetor):
    maior=max(vetor)
    menor=min(vetor)
    print(f"\n\tO maior valor do vetor é: {maior}\n")
    print(f"\n\tO menor valor do vetor é: {menor}\n")

"""
Exemplo 7: Inverter a ordem dos elementos de um vetor sem usar reverse()
"""

def inverter(vetor):
    vetor_invertido=vetor[::-1]
    print(f"\n\tA inversão do vetor fica assim: {vetor_invertido}\n")

"""
Exemplo 8: Multiplicar cada elemento do vetor por 2 e armazenar em um novo vetor
"""

def multiplicar(vetor):
    multi=2
    vetor_mult=[elemento*multi for elemento in vetor]
    print(f"\n\tA multiplicação dos elementos no vetor é: {vetor_mult}\n")

"""
Exemplo 9: Contar quantas vezes o valor 3 aparece em um vetor
"""

def contador(vetor):
    ocorrencias=vetor.count(3)
    print(f"\n\tO nº 3 aparece {ocorrencias} vezes\n")

"""
Exemplo 10: Ordenar um vetor em ordem crescente
"""

def ordenar(vetor):
    vetor_ordenado=sorted(vetor)
    print(f"\n\tOrdedando o vetor, temos o seguinte resultado: {vetor_ordenado}\n")

"""
Exemplo 11: Remover elementos duplicados do vetor
"""

def remover_dupli(vetor):
    sem_duplicatas=list(dict.fromkeys(vetor))
    print(f"\n\tO vetor sem os números repetidos fica assim: {sem_duplicatas}\n")

"""
Exemplo 12: Separar os elementos pares e ímpares em duas listas
"""

def separar_elementos(vetor):
    pares=[num for num in vetor if num % 2 == 0]
    impares=[num for num in vetor if num % 2 != 0]
    print(f"\n\tOs números pares são: {pares}\n")
    print(f"\n\tOs números ímpares são: {impares}\n")

"""
Exemplo 13: Calcular a média e exibir elementos acima da média
"""

def calcular_media(vetor):
    media=sum(vetor)/len(vetor)
    acima_media=[num for num in vetor if num>media]
    print(f"\n\t A média dos valores é: {media}\n")
    print(f"\n\tOs elementos que estão acima da média são: {acima_media}\n")


"""
Testando Funções:
"""


if __name__ == "__main__":
    #criar_imprimir(vet_dados)
    #interando(vet_dados)
    #calcular(vet_dados)
    #maior_menor(vet_dados2)
    #inverter(vet_dados3)
    #multiplicar(vet_dados)
    #contador(vet_dados4)
    #ordenar(vet_dados4)
    #remover_dupli(vet_dados4)
    #separar_elementos(vet_dados5)
    calcular_media(vet_dados5)

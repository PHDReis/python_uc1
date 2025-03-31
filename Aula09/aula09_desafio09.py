"""
Aula 09 - Desafio 09
"""



"""
Desafio 01 - Soma de Elementos:
"""
def soma():
    
    conjunto=[]

    for numero in range(5):
        numeros=int(input(f"\n\tDigite seu numero {numero + 1}: "))
        conjunto.append(numeros)

    soma=sum(conjunto)

    print(f"\n\tA soma dos números {conjunto} é {soma}")
    

"""
Desafio 02 - Números Ímpares de um intervalo
"""
def num_impar():

    for conjunto in range(1,51):
        
        impares=[num for num in conjunto if num % 2 != 0]

    print(f"\n\tOs números ìmpares são: {impares}")

if __name__ == "__main__":
    #soma()
    num_impar()
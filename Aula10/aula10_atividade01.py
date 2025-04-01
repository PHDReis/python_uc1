"""
Aula 10 - Atividade 01
"""

matriz_4_4=[
    [91,2,3,4],
    [5,6,57,8],
    [9,10,111,12],
    [19,14,55,16]
]



"""
matrizes 01.2
"""

def matrizes():

    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(f"O elemento na posição (0,0) é:  {matriz[0][0]}")
    print(f"O elemento na posição (2,1) é:  {matriz[2][1]}")

    for linha in matriz:
        print(f"|", end="")
        for elemento in linha:
            print(f"{elemento}", end='|')
        print()



"""
Exercício 01 - Criando e Exibindo uma Matriz
"""
def criar_exibir():

    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor=int(input(f"\n\n\tDigite os valores para [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    for linha in matriz:
        print(f"|", end="")
        for elemento in linha:
            print(f"{elemento}", end='|')
        print()


"""
Exercício 02 - Soma dos Elementos da Matriz
"""
def soma_elementos(matriz):
    soma=0

    for i in range(4):
        for j in range(4):
            soma += matriz[i][j]


    print(f"A soma dos elementos na matriz é: {soma}")

"""
Exercício 02.2
"""

def soma_elementos_2(matriz):
    soma=0

    for i in range(4):
            soma=soma + sum(matriz_4_4[i])


    print(f"A soma dos elementos na matriz é: {soma}")


"""
Exercício 02.3
"""

def soma_elementos_3(matriz):
    soma=0

    for linha in matriz:
            soma=soma + sum(linha)


    print(f"A soma dos elementos na matriz é: {soma}")


"""
Exercício 04 - Maior valor de cada linha
"""

def maior_valor_linha(matriz):
     
     #for i, linha in enumerate(matriz):
          #print(f" O maior valor da linha {i}: {max(linha)}")

     
     for i in range(4):
          maior=matriz[i][0]
          for j in range(4):
              if matriz[i][j]>maior:
                maior = matriz[i][j]

          print(f" O maior valor da linha {i}: {maior}")

    #Ta retornando o maior valor de cada linha!

     #for i in range(4):
         #maior=max(matriz[i])
         #print(f"Maior valor da linha {i}: {maior}")

"""
Exercício 04.2
"""

def maior_valor_linha_2(matriz):

    maior=0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > maior:
                maior=matriz[i][j]

    print(f"{maior}")

    # Retorna o maior valor da matriz


"""
Exercício 05 - Contagem de Números Pares
"""

def contagem_pares(matriz):

    pares=0
    impares=0
    n_par=[]
    n_impar=[]

    for i in range(4):
        

        for j in range(4):
            if matriz[i][j] % 2 == 0:
                n_par.append(matriz[i][j])
                pares += 1
            
            else:
                impares += 1
                n_impar.append(matriz[i][j])
                

    print(f"A quantidade de números pares na matriz é: {pares}")
    print(f"Já a quantidade de impares é: {impares}")

    print(f"Os numeros pares são: {n_par}")
    print(f"Os numeros impares são: {n_impar}")



"""
Exercício 6 - Multiplicação de linhas por um número
"""

def multiplicacao(matriz,num=2):

    num = int(input(f"Digite um numero para multiplicação: "))
    qual_linha = int(input(f"Digite qual linha para multiplicada (0-3): "))

    for j in range(4):
        matriz[qual_linha][j] *= num

    for linha in matriz:
        print(linha)



"""
Testando as funções:
"""

if __name__=="__main__":
    #matrizes()    
    #criar_exibir()
    #soma_elementos(matriz_4_4)
    #soma_elementos_2(matriz_4_4)
    #soma_elementos_3(matriz_4_4)
    #maior_valor_linha(matriz_4_4)
    #maior_valor_linha_2(matriz_4_4)
    contagem_pares(matriz_4_4)
    multiplicacao(matriz_4_4)
    
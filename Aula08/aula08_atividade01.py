def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")



"""
Função soma(numeros)
- recebe um vetor com numeros e calcula da soma dos mesmos
"""

def soma(a, b):
    return a + b

def testar_soma():
    resultado = soma(5, 7)
    print("A soma é:", resultado)    


"""
Função Fatorial
"""

def fatorial(n):
    if n <0:
        return "Numero inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def testar_fatorial():
    numero=int(input("\n\n\tInforme um numero: "))
    resultado=fatorial(numero)
    print(f"\n\n\tFatorial de {numero} é igual à {resultado}!\n\n")

"""
Verifica se o arquivo está sendo carregado como
um módulo ou como um executável. 
Se for carregado como um executavel 
chama a função principal do programa
"""


if __name__ == "__main__": 
    testar_fatorial()
a=input("Digite o primeiro número : ")
a=float(a)
b=float(input("Digite o segundo número : "))

## Para que o codigo não dê erro, quando é utilizado o comando input ele lê uma string.
## Para que seja possivel utilizar em uma conta aritmética é preciso mudar o tipo da variavel, podendo ser feita de qualquer uma das duas formas acima. A mais elegante é o da variável B.
## Float é ponto flutuante, ou seja, numeros reais (que podem ser quebrados). Se fosse utilizado o int para transformar em inteiro, poderia dar erro quando o usuário digitasse um valor quebrado.

soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
div_inteiro=a//b
resto=a%b
exponenciacao=a**b

print(f"O resultado da soma é {soma}")
print(f"O resultado da subtração é {subtracao}")
print(f"O resultado da multiplicação é {multiplicacao}")
print(f"O resultado da divisão é {divisao:.2f}") #a formatação ":.2f" significa que vai ser formatado para apenas duas casas decimais e o "f" significa que é do tipo float.
print(f"O resultado da parte inteira da divisão é {div_inteiro}")
print(f"O resultado do resto da divisão é {resto}")
print(f"O resultado da exponenciação é {exponenciacao:.2f}")
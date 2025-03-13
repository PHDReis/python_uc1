idade_str=input("Digite a sua idade: ")
idade=int(idade_str)
print("Você possui carteira? Digite S para sim e N para não.")
tem_carteira_str=input("Digite sua resposta: ")
tem_carteira_str=tem_carteira_str.lower() ## o .lower faz com que as respostas do usuário, ou a leitura do input, fiquem minusculas.
## Fazendo isso, não corre o risco do usuário responder S com a letra maiusca e mesmo assim apresentar a resposta que le não pode dirigir, porque colocamos no if que a resposta tem que ser um s minusculo.
## O contrário, podemos usar o .uper para deixar as letras maiusculas.


if (idade >= 18) and (tem_carteira_str=="s"):
      print("Você pode dirigir!")
else:
    print("Desculpe, sem carteira não dá!")

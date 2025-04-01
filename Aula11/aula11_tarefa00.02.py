frase = "o rato roel a roupa do rei de roma"
palavras = frase.split()
palavras_2 = ["dia", "claro", "dia", "escuro", "todo", "dia"]


contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra,0)+1
print(contagem)

contagem = {}
for palavra in palavras_2:
    contagem[palavra] = contagem.get(palavra,0)+1
print(contagem)
alunos = {}

quant_alunos = int(input(f"Qual a quantidade de alunos que você quer adicionar?: "))

for aluno in quant_alunos:
    nome = input("Digite o nome do aluno: ")
    notas = list(map(float, input(f"Digite as notas de {nome} separadas por espaço: ").split()))

    media = sum(notas)/len(notas)

    alunos[nome] = {"notas":notas, "media": media}

print("Dados dos Alunos: ")
for nome, dados in alunos.items():
    print(f"Nome: {nome}")
    print(f"Notas: {dados['notas']}")
    print(f"Media: {dados['media']:.2f}")
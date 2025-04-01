aluno_1 = {"nome": "Pedro", "notas":[7,8,9]}
aluno_2 = {"nome": "Matheus", "notas":[8,7,10]}
aluno_3 = {"nome": "Gervásio", "notas":[6,8,8]}

alunos = [aluno_1, aluno_2, aluno_3]

for aluno in alunos:
    media=sum(aluno["notas"])/len(aluno["notas"])

    aluno["media"]=media
    print(f"Os dados atualizados do aluno {aluno["nome"]} são: {aluno}")
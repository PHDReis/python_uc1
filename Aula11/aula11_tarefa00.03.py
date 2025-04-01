aluno_1 = {"nome": "Pedro", "notas":[7,8,9]}
aluno_2 = {"nome": "Matheus", "notas":[8,7,10]}
aluno_3 = {"nome": "Gervásio", "notas":[6,8,8]}

media=sum(aluno_1["notas"])/len(aluno_1["notas"])

print(f"Os dados do aluno 1 são: {aluno_1}")
print(f"As notas do aluno {aluno_1["nome"]} são {aluno_1["notas"]}")

aluno_1["media"]=media
print(f"Os dados atualizados do aluno 1 são {aluno_1}")
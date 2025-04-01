pessoa = {"nome": "Pedro", "idade":"30", "cidade":"Petrópolis"}
print(f"Dados da pessoa: {pessoa}")

pessoa["email"]="pedro@yahoo.com"
print(f"Dados da pessoa: {pessoa}")

pessoa["idade"]=31
print(f"Dados da pessoa: {pessoa}")

del pessoa["cidade"]
print(f"Dados da pessoa: {pessoa}")
alunos = ['Netinho']
alunos.append('Dumato')
while True:
    nome=input('Digite o nome do aluno: ')
    alunos.append(nome)
    respota = input('Deseja adicionar mais um aluno? S/N: ')
    if respota.upper() == 'N' :
        break
print(f"Alunos cadastrados: {alunos}")
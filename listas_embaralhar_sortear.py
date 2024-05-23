import random
alunos =['Mateus', 'joão', 'Gabriel', 'Felipe', 'Ana Clara', 'Ana Beatriz']
#Embaralhar a lista
random.shuffle(alunos)
print(f'Listas embaralhada: {alunos}')
#Escolher um aluno aleatoriamente
aluno_sorteado = random.choice(alunos)
print(f'O aluno(a) sorteado(a) foi: {aluno_sorteado}')
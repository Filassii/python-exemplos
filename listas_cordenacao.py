import random
alunos =['Mateus', 'joão', 'Gabriel', 'Felipe', 'Ana Clara', 'Ana Beatriz']
#Embaralhar a lista
random.shuffle(alunos)
print(f'Listas embaralhada: {alunos}')
#Ordena a Lista Crescente
alunos.sort()
print(f'Lista crescente: {alunos}')
#Ordenar a Lista Decrescente
alunos.sort(reverse=True)
print(f'Lista descrecente: {alunos}')
import random
n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite o último nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('\nOrdem dos alunos:', lista)

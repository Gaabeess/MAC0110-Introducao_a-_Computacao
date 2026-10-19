Alunos = [int(input('A[%d]: ' % i)) for i in range(10)]
Notas = [float(input('B[%d]: ' % i)) for i in range(10)]

# Verifica a posição do maior e menor elemento no vetor Notas
posição_maior = 0
posição_menor = 0
for i in range(10):
    if max(Notas) == Notas[i]:
        posição_maior = i
    if min(Notas) == Notas[i]:
        posição_menor = i


print(f'Maior Nota: {max(Notas)}; Aluno com maior nota: {Alunos[posição_maior]}')
print(f'Menor Nota: {min(Notas)}; Aluno com menor nota: {Alunos[posição_menor]}')
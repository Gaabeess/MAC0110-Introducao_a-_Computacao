A = []

# Recebe e inclui os valores no Vetor
for i in range(5):
    num = int(input('A[%d]: ' % i))
    A.append(num)


# Realiza o cálculo da média dos valores do vetor
soma = 0
for j in A:
    soma += j
média = soma / 5

# Imprime os valores
print(f'Vetor A = {A}')
print(f'Maior valor: {max(A)}')
print(f'Menor Valor: {min(A)}')
print(f'Média dos valores: {média}')
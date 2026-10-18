A = []

# recebe os valores e adiciona no vetor A
for i in range(10):
    num = int(input('A[%d]: ' %  i))

    # garante que o número esteja entre 0 e 50
    while num < 0 or num > 50:
        print('Número inválido. Digite um número entre 0 e 50.')
        num = int(input('A[%d]: ' %  i))

    A.append(num)

# verifica os números ímpares e os adiciona no vetor impares
impares = []
for j in A:
    if j % 2 == 1:
        impares.append(j)

# imprime os valores ímpares do vetor impares, dois por linha
for k in range(0, len(impares), 2):
    if k+1 < len(impares):
        print('impares[%d]: %d, impares[%d]: %d' % (k, impares[k], k+1, impares[k+1]))
    else:
        print('impares[%d]: %d' % (k, impares[k]))

print(f'Valores ímpares: {impares}')
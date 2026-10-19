A = [int(input('A[%d]: ' % i)) for i in range(10)]
B = [int(input('B[%d]: ' % i)) for i in range(10)]
C = []

# Verifica se o índice é par ou ímpar e adiciona os valores ao vetor C
for i in range(10):
    if i % 2 == 0:
        C.append(A[i])
    else:
        C.append(B[i])

print(f'Vetor C: {C}')
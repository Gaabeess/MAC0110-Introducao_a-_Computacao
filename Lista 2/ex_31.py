A = [int(input('A[%d]: ' % i)) for i in range(10)]
B = [int(input('B[%d]: ' % i)) for i in range(10)]

C = []

# Adiciona valores de A em C, sem repetições
for i in A:
    if i not in C:
        C.append(i)

# Adiciona valores de B em C, sem repetições
for i in B:
    if i not in C:
        C.append(i)

print(f'Vetor C: {C}')
A = [float(input('A[%d]: ' % i)) for i in range(10)] # recebe os valores e adiciona no vetor A

# substitui os valores negativos por zero
for i in range(len(A)):
    if A[i] < 0:
        A[i] = 0

print(f'Vetor A com os valores negativos substituídos por zero: {A}')
A = [int(input(f'A[{i}]: ')) for i in range(10)] # Solicitando ao usuário que insira 10 elementos para o vetor A
B = [int(input(f'B[{i}]: ')) for i in range(10)] # Solicitando ao usuário que insira 10 elementos para o vetor B
C = []

# Calculando a diferença entre os elementos correspondentes de A e B
for i in range(10):
    C.append(A[i] - B[i])

print(f'Vetor C: {C}')
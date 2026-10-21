A = []

for i in range(10):
    num = float(input('A[%d]: ' % i))
    A.append(num)
    A.sort()  # Ordena o vetor A do menor para o maior valor a cada inserção


print(f'Vetor ordenado: {A}')


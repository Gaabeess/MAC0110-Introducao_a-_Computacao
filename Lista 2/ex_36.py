A = [float(input('A[%d]: ' % i)) for i in range(10)]

# Realiza a ordenação do menor para o maior valor do vetor A
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]: # verifica se o elemento atual é maior que o próximo elemento
            A[i], A[j] = A[j], A[i]
        

print(f'Vetor ordenado: {A}')

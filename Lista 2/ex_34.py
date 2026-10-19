A = []

# Adiciona valores de A em C, sem repetições
for i in range(10):
    num = int(input('A[%d]: ' % i))
    # Verifica se o número já está presente em A
    while num in A:
        print('Número repetido! Digite outro número.')
        num = int(input('A[%d]: ' % i))

    A.append(num)
print(f'Vetor A: {A}')
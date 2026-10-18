A = []

# Receb aos valores e adiciona no Vetor
for i in range(10):
    num = float(input('A[%d]: ' % i))
    A.append(num)

positivos = 0
qtd_negativos = 0

# Verifica se o valor é positivo ou negativo
for j in A:
    if j < 0:
        qtd_negativos += 1
    else:
        positivos += j

# Imprime a soma dos valores positivos e a quantidade de negativos
print(f'Soma dos Positivos: {positivos}')
print(f'Quantidade de valores negativos: {qtd_negativos}')
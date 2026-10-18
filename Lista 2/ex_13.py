A = []

# Recebe e inclui os valores no Vetor
for i in range(5):
    num = int(input('A[%d]: ' % i))
    A.append(num)

# Busca o indice do maior valor do vetor
posicao = 0
for i in range(1,5):
    if A[i] == max(A):
        posicao = i

#imprime os resultados
print(f'o Maior valor é {max(A)} e seu índice é {posicao}')
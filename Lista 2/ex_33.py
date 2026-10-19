A = [int(input('A[%d]: ' % i)) for i in range(15)]

# Compacta o vetor A, removendo os elementos iguais a 0 e puxando em 1 posição todos os elementos à direita do elemento removido
i = 0
while i < len(A):
        if A[i] == 0:
            # Puxa todos os elementos à direita do elemento removido em 1 posição para a esquerda
            for j in range(i, len(A)-1):
                A[j] = A[j+1]
            A.pop()
        else:
            i += 1

print(f'Vetor A compactado: {A}')
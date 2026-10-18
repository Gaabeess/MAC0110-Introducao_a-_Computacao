A = [int(input('A[%d]: ' % i)) for i in range(10)] # recebe os valores e adiciona no vetor A

# Filtra os números duplicados do vetor A
A_sem_duplicados = []
for j in A:
    if j not in A_sem_duplicados:
        A_sem_duplicados.append(j)


print(f'Vetor A sem os números duplicados: {A_sem_duplicados}')
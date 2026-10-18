A = []

# recebe os valores e adiciona no vetor A
for i in range(10):
    num = int(input('A[%d]: ' %  i))
    A.append(num)

# verifica os números duplicados
duplicados = []
for j in A:
    if A.count(j) > 1 and j not in duplicados:
        duplicados.append(j)

print(f'Números duplicados: {duplicados}')



A = [1,2,3,4,5,6,5,4,3,2,1,]
Ordenado = []

inicio = 0
fim = len(A) - 1

# Ordena o vetor A do menor para o maior valor, utilizando dois ponteiros (inicio e fim)
while inicio <= fim:
    if A[inicio] <= A[fim]:
        Ordenado.append(A[inicio])
        inicio += 1   

    else:
        Ordenado.append(A[fim])
        fim -= 1

print(f'Vetor ordenado: {Ordenado}')
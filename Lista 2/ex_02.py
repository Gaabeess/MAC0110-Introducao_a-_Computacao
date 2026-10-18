A = []

# Recebe os valores e inclui no vetor
for i in range(0, 7):
    valor = int(input("A[%d]: " % i))
    A.append(valor)

# imprime um valor por linha
for valor in A:
    print(valor)
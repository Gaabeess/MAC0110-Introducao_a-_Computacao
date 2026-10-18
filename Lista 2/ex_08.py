A = []

#Solicita ao usuários 6 valores inteiros para incluir no vetor
for i in range(6):
    num = int(input('A[%d]: ' % i))
    A.append(num)

# Imprime a ordem inversa do vetor
for j in A[:: -1]:
    print(j)
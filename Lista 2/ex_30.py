A = [int(input('A[%d]: ' % i )) for i in range(10)]
B = [int(input('B[%d]: ' % i ))for i in range(10)]

C = []

# Verifica se algum valor de A está presente em B e adiciona em C 
for i in A:
    if i in B:
        C.append(i)

print(f'Vetor Intersecção: {C}')
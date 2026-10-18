A = []
B = []

# Recebe os valores e inclui no vetor
for i in range(10):
    num = int(input('A[%d]: ' % i))
    A.append(num)

# Calcula o quadrado dos valores de A e adiciona em B
for  j in A:
    B.append(j**2)

print(f'Vetor A: {A}')
print(f'Vetor B: {B}')
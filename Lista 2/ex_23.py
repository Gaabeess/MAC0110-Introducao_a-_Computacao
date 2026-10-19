A = [int(input('A[%d]: ' % i)) for i in range(5)]
B = [int(input('B[%d]: ' % i)) for i in range(5)]

C = []

# Realiza o cálculo do produto escalar de A e B
soma = 0
for i in range(5):
    soma += A[i]*B[i]

print(f'Produto escalar: {soma}')
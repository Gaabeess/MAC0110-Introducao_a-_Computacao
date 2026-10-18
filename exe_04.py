A = []

for i in range(8):
    num = int(input('A[%d]: ' % i))
    A.append(num)

x = int(input('Escolha um valor entre 0 a 7: '))
y = int(input('Escolha um valor entre 0 a 7: '))

soma = A[x] + A[y]

print(soma)
A = []

# Recebe os valores e inclui no vetor
for i in range(8):
    num = int(input('A[%d]: ' % i))
    A.append(num)


print(f'Vetor A: {A}')
# Solicita a escolha do indice a ser somado
x = int(input('Escolha um valor entre 0 a 7: '))
y = int(input('Escolha um valor entre 0 a 7: '))

soma = A[x] + A[y]

print(soma)
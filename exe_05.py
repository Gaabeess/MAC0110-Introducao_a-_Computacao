A = []

for i in range(10):
    num = int(input('A[%d]: ' % i))
    A.append(num)

par = 0

for j in A:
    if j % 2 == 0:
        par += 1
        print(j)

print(f'Quantidade de pares: {par}')
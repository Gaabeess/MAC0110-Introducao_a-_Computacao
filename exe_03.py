A = []
B = []

for i in range(10):
    num = int(input('A[%d]: ' % i))
    A.append(num)

for  j in A:
    B.append(j**2)

print(f'Vetor A: {A}')
print(f'Vetor B: {B}')
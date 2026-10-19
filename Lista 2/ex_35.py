a = input('Digite um valor menor que 10000: ')
b = input('Digite outro valor menor que 10000: ')

# Verifica se os valores estão dentro do intervalor
while (int(a) <= 0 or int(a) >= 10000) or (int(b) <= 0 or int(b)) >= 10000:
    print('Valor inválido! Digite novamente.')
    if int(a) <= 0 or int(a) >= 10000:
        a = input('Digite um valor menor que 10000: ')
    if int(b) <= 0 or int(b) >= 10000:
        b = input('Digite outro valor menor que 10000: ')

# Separa os algarismo de a e os adiciona no vetor A e inverte o vetor
A = []
for i in range(len(a)):
    A.append(int(a[i]))
A = A[::-1]
print(f'Vetor A: {A}')

# Separa os algarismo de b e os adiciona no vetor B e inverte o vetor
B = []
for i in range(len(b)):
    B.append(int(b[i]))
B = B[::-1]
print(f'Vetor B: {B}')

# Realiza a soma das posições i dos vetores A e B, caso a soma > 10, diminui 10 e adiciona 1 na próxima posição
Soma = []
vai_um = 0
for i in range(max(len(A), len(B))):
    algarismo_a = A[i] if i < len(A) else 0
    algarismo_b = B[i] if i < len(B) else 0

    num = algarismo_a + algarismo_b + vai_um

    if num >= 10:
        num -=10
        vai_um = 1
    else:
        vai_um = 0

    Soma.append(num)
if vai_um == 1:
    Soma.append(vai_um)

print(f'Vetor Soma(A+B): {Soma}')
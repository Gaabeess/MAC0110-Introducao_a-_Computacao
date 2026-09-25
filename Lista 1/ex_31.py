n = int(input("Digite um número inteiro: "))

while n % 2 != 0:
    print(f'{n} não é um número par')
    n = int(input("Digite um número inteiro: "))

for i in range(n, -1, -2):
    if i % 2 == 0:
        print(i)
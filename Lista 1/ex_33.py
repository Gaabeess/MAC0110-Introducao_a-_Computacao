n = int(input("Digite um número inteiro: "))

while n % 2 == 0:
    print(f'{n} não é um número ímpar')
    n = int(input("Digite um número inteiro: "))

for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i)
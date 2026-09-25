n = int(input("Digite um número inteiro: "))

while n % 2 != 0:
    print(f'{n} não é um número par')
    n = int(input("Digite um número inteiro: "))

for i in range(0, n + 1):
    if i % 2 == 0:
        print(i)   


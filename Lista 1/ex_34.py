n = int(input("Digite um número inteiro: "))

soma = 0

for i in range(0, n + 1):
    soma += i

print(f'A soma dos números de 0 até {n} é: {soma}')
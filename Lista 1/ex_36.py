n = int(input("Digite um número inteiro: "))

def soma(n):
    soma = 0
    for i in range(0, n + 1):
        soma += i
    return soma

print(f'A soma dos números de 0 até {n} é: {soma(n)}')

def soma_invertendo(n):
    soma = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            soma -= i
        else:
            soma += i
    return soma

print(f'A soma dos números de 0 até {n} invertendo os sinais é: {soma_invertendo(n)}')

def soma_impares(n):
    soma = 0
    for i in range(0, n + 1):
        if i % 2 != 0:
            soma += i
    return soma

print(f'A soma dos números ímpares de 0 até {n} é: {soma_impares(n)}')
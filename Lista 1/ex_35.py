n = int(input("Digite um número inteiro de três dígitos: "))

while n < 100 or n > 999:
    print(f'{n} não é um número de três dígitos')
    n = int(input("Digite um número inteiro de três dígitos: "))

algarismos = [int(digito) for digito in str(n)]

for i in range(len(algarismos)):
    print(f'O {i + 1}º algarismo é: {algarismos[i]}')
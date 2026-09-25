n = int(input("Digite um número inteiro: "))

original = n

invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

if original == invertido:
    print(f'{original} é um palíndromo')
else:
    print(f'{original} não é um palíndromo')

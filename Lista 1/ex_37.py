n = int(input("Digite um número inteiro: "))

b = 2
p = (b+(n/b))/2

while abs(n-p**2) >= 0.0001:
    b = p
    p = (b+(n/b))/2

print(f'A raiz quadrada de {n} é: {p}')
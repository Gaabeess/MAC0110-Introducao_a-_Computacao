i = 9
valores = []

while i >= 0:
    a = int(input("Digite o valor inteiro: "))
    valores.append(a)
    i -= 1

print(f'O maior valor digitado foi: {max(valores)}')
print(f'O menor valor digitado foi: {min(valores)}')
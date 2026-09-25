
soma = 0
for i in range(0, 51):
    if i % 2 == 0:
        soma += i
        print(i, soma)
print(f'A soma dos números pares entre 0 e 50 é: {soma}')
A = []

# Preenche o vetor A com os 100 primeiros números naturais que são múltiplos de 7 ou que possuem o dígito 7
numero = 0
while len(A) < 100:
    if numero % 7 == 0 or numero % 10 == 7:
        A.append(numero)
    numero += 1

print(f'Vetor A: {A}')
A = [int(input(f'A[{i}]: ')) for i in range(6)]  # recebe os valores e adiciona no vetor A

PAR = []
IMPAR = []

for i in A:
    if i % 2 == 0:
        PAR.append(i)  # adiciona os números pares no vetor PAR
    else:
        IMPAR.append(i)  # adiciona os números ímpares no vetor IMPAR

print(f'Vetor PAR (números pares): {PAR}\nSoma dos pares: {sum(PAR)}')
print(f'Vetor IMPAR (números ímpares): {IMPAR}\nQuantidade de ímpares: {len(IMPAR)}')
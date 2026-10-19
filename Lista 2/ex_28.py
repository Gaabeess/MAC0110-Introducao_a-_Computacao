V = [int(input(f'V[{i}]: ')) for i in range(10)]  # recebe os valores e adiciona no vetor V
V1 = []
V2 = []

for i in V:
    if i % 2 !=0:
        V1.append(i)  # adiciona os números ímpares no vetor V1
    else:
        V2.append(i)  # adiciona os números pares no vetor V2

print(f'Vetor V1 (números ímpares): {V1}')
print(f'Vetor V2 (números pares): {V2}')
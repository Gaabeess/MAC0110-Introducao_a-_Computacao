Notas = []

# Recebe as notas e adiciona no Vetor
for i in range(15):
    num = float(input('A[%d]: ' % i))
    Notas.append(num)


# Faz a soma das notas
soma = 0
for j in Notas:
    soma += j

# Calcula e imprime a média arredondando o valor para 2 casa decimais
média = soma / 15
print(f'A Média da sala é: {round(média, 2)}')
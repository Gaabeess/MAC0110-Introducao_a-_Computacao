A = [] # Vetor vazio

# Percorre até 10 valores a serem recebidos pelo usuário e adiciona ao vetor A
for i in range(10):
    num = int(input('A[%d]: ' % i))
    A.append(num)


# Considerando o maior valor o primeiro do Vetor 
maior = A[0]
indice = 0

#Percorre os próximos 9 valores do vetor e compara com o {maior} e retorna o maior valor do vetor e seu índice
for j in range(1,10):
    if A[j] > maior:
        maior = A[j]
        indice = j

# Imprime o resultado
print(f'Vetor A: {A}')
print(f'Maior valor em A: {maior}')
print(f'Índice do maior valor: {indice}')
A = []

# Recebe os valores e inclui no vetor
for i in range(10):
    num = int(input('A[%d]: ' % i))
    A.append(num)

# Verifica qual valor de A é menor e qual é maior
maior = A[0]
menor = A[0]

for num in A:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(menor)
print(maior) # podemos também print(max{A}) e print(min{A}) sem verificar por if
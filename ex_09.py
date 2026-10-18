A = []

#Solicita ao usuários 6 valores inteiros pares para incluir no vetor
for i in range(6):
    num = int(input('A[%d]: ' % i))

    # Verifica se o valor digitado é par
    while num % 2 != 0:
        print('OS valores precisam ser pares!')
        num = int(input('A[%d]: ' % i))

    A.append(num)

# Imprime os valores na ordem inversa
print(f'Vetor A: {A[::-1]}')

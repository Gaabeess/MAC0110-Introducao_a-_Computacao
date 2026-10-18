A = [int(input('A[%d]: ' % i)) for i in range(10)] # recebe os valores e adiciona no vetor A

x = int(input('Digite um número: ')) # recebe o número para verificar os múltiplos

# verifica os múltiplos de x no vetor A
for j in A:
    if j % x == 0:
        print('%d é multiplo de %d' % (j, x))

A = [float(input('A[%d]: ' % i)) for i in range(5)] # recebe os valores e adiciona no vetor A

código = int(input('código: ')) # recebe o código

while código != 0 and código != 1 and código != 2: # verifica se o código é válido
    print('Código inválido')
    código = int(input('código: ')) # recebe o código novamente

# verifica o código e imprime o vetor A ou o vetor A invertido
if código == 0:
    print('Processo encerrado')
elif código == 1:
    print(f'Vetor A: {A}')
elif código == 2:
    print(f'Vetor A invertido: {A[::-1]}')
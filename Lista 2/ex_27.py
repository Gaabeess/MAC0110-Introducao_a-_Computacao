A = [int(input(f'A[{i}]: ')) for i in range(10)]  # recebe os valores e adiciona no vetor A

# Verifica se cada número no vetor A é primo
for posicao, numero in enumerate(A):
    if numero < 2:
        continue  # ignora números negativos

    primo = True
    divisor = 2

    # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada do número
    while divisor*divisor <= numero:
        # Se o número for divisível por algum divisor, ele não é primo
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    # Se o número for primo, imprime a posição e o número
    if primo:
        print(f'O número {numero} na posição {posicao} é primo.')
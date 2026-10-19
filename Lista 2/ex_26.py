A = [int(input(f'A[{i}]: ')) for i in range(10)]  # recebe os valores e adiciona no vetor A

média = sum(A) / len(A)  # calcula a média dos valores do vetor A

desvio = (sum((x - média) ** 2 for x in A) / (len(A)-1)) ** 0.5  # calcula o desvio padrão dos valores do vetor A

print(f'Desvio padrão: {desvio:.2f}')  # imprime o desvio padrão com duas casas decimais
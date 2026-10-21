n = int(input('Digite o número de linhas do triângulo de Pascal: '))

# Cria uma lista para armazenar o triângulo de Pascal
triangulo = []

# Gera o triângulo de Pascal
for i in range(n):
    linha = [1] * (i + 1)  # Inicializa a linha com 1s
    for j in range(1, i):
        linha[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]  # Calcula os valores internos da linha
    triangulo.append(linha)  # Adiciona a linha ao triângulo

# Imprime o triângulo de Pascal
for linha in triangulo:
    print(linha)
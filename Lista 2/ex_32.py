Y = [int(input('Y[%d]: ' % i)) for i in range(5)]
X = [int(input('X[%d]: ' % i)) for i in range(5)]

# Realiza a soma de cada elemento de Y com o elemento correspondente de X e armazena em Soma
Soma = []
for i in range(len(Y)):
    num = Y[i] + X[i]
    Soma.append(num)

print(f'Vetor Soma: {Soma}')

# Realiza a multiplicação de cada elemento de Y com o elemento correspondente de X e armazena em Multiplicacao
Multiplicacao = []
for i in range(len(Y)):
    num = Y[i] * X[i]
    Multiplicacao.append(num)
print(f'Vetor Multiplicação: {Multiplicacao}')

# Cria o conjunto diferença entre X e Y
Diferenca = []
for i in range(len(X)):
    if X[i] not in Y:
        Diferenca.append(X[i])
print(f'Vetor Diferença: {Diferenca}')

# Cria o conjunto intersecção entre X e Y
Intersecao = []
for i in range(len(Y)):
    if Y[i] in X:
        Intersecao.append(Y[i])
print(f'Vetor Intersecção: {Intersecao}')

# Cria o conjunto união entre X e Y
Uniao = X.copy() # Cria uma cópia de X para Uniao
for i in Y:
    if i not in X:
        Uniao.append(i)
print(f'Vetor União: {Uniao}')

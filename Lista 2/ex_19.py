A = [] # A = [(i+5*i)%(i+1) for i in range(50)] # Calcula os valores e adiciona no vetor A

# Calcula os valores e adiciona no vetor A
for i in range(50):
    valor = (i+5*i)%(i+1)
    A.append(valor)

print(f'Vetor A: {A}')
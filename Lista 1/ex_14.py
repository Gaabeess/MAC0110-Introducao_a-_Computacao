a = int(input('Digite um número inteiro: '))
b= int(input('Digite outro número inteiro: '))


if a > b:
    print(f'O maior número é {a}')
elif b > a:
    print(f'O maior número é {b}')

print('A diferença entre os dois números é', abs(a - b))


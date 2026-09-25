a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Lados inválidos')
elif a + b <= c or a + c <= b or b + c <= a:
    print('Não é um triângulo') 
else:
    if a == b and b == c:
        print('Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
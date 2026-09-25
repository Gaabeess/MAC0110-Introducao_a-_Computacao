n = int(input("Digite um número inteiro: "))

for i in range(0, n):
    if (i % 1 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0) and i % 2 != 0:
        print(i)
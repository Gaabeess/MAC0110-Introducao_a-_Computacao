
a = int(input("Digite o valor inteiro: "))

for i in range(3, a):
    if i % 2 != 0:
        primo = True
        j = 3
        while j < i:
            if i % j == 0:
                primo = False
                break
            j += 2
        if primo == True:
            print(f'{i} é um número primo')

if a == 0 or a == 1:
    print(f'{a} não é um número primo')
elif a == 2:
    print(f'{a} é um número primo')
else:
    primo = True
    i = 3
    while i < a:
        if a % i == 0:
            primo = False
            break
        i += 2
    if primo == True:
        print(f'{a} é um número primo')
    else:
        print(f'{a} não é um número primo')
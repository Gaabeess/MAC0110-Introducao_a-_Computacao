a = int(input("Digite o valor inteiro: "))

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
    if primo == False:
        print(f'{a} é um número primo')
    else:
        print(f'{a} não é um número primo')
a = input("Digite um valor inteiro: ")

if int(a) <= 0:
    print("Número Invalido")
else:
    digitos = list(a)
    soma = 0
    for i in digitos:
        soma += int(i)
    print(f"A soma dos dígitos é: {soma}")

print("Digite um número inteiro positivo: ")
numero = int(input())
valores = []

while numero > 0:
    valores.append(numero)
    print("Digite um número inteiro positivo: ")
    numero = int(input())

soma = 0
for j in valores:
    soma += j

media = soma / len(valores)
    

print(f"A soma dos números digitados é: {soma}")
print(f"Quantidade de números digitados: {len(valores)}")
print(f"A média dos números digitados é: {media}")

            

        
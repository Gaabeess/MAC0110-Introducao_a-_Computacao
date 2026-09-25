deposito_inical = float(input('Digite o valor do depósito inical: '))
taxa = float(input('Digite a taxa de juros (em %): '))
i = 24

while i > 0:
    deposito_inical += deposito_inical * (taxa / 100)
    i -= 1

print(f'O valor do depósito após 24 meses é: R${deposito_inical:.2f}')
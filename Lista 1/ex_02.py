salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o percentual de aumento: "))

novo_salario = salario + (salario * aumento / 100)
print(f"O novo salário é: {novo_salario}")
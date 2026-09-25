preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

novo_preco = preco - (preco * desconto / 100)
print(f"O novo preço é: {novo_preco}")
codigo = 1
total = 0

while codigo > 0:

    codigo = int(input("Digite o código do produto: "))
    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 4 and codigo != 5 and codigo != 0:
        print("Código inválido")

    elif codigo > 0:

        qnt = int(input("Digite a quantidade comprada: "))
        
        match codigo:

            case 1:
                preco = 0.5
                total += qnt * preco
            case 2:
                preco = 1.00
                total += qnt * preco
            case 3:
                preco = 4.00
                total += qnt * preco
            case 4:
                preco = 7.00
                total += qnt * preco
            case 5:
                preco = 8.00
                total += qnt * preco

        print(f"Produto {codigo} adicionado ao carrinho. Quantidade: {qnt}. Preço unitário: R$ {preco:.2f}. Total parcial: R$ {total:.2f}")

    if codigo <= 0:
        print("Finalizando compra...")
        print(f"Total a ser pago: R$ {total:.2f}")
        break

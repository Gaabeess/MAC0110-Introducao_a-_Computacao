km_percorridos = float(input("Quantos Km foram percorridos: "))
dias_aluguel = int(input("Quantos dias de aluguel do carro: "))

aluguel = 60*dias_aluguel + 0.15*km_percorridos
print(f"O valor total a pagar é: R${aluguel:.2f}")
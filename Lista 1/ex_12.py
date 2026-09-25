kWh_cons = float(input("Insira a quantidade de kWh consumida: "))
instalacao = input("Insira o tipo de instalação (R para residencial, C para comercial, I para industrial): ")

match instalacao.upper():
    case "R":
        if kWh_cons <= 500:
            valor = kWh_cons * 0.40
        else:
            valor = kWh_cons * 0.65
    case "C":
        if kWh_cons <= 1000:
            valor = kWh_cons * 0.55
        else:
            valor = kWh_cons * 0.60
    case "I":
        if kWh_cons <= 5000:
            valor = kWh_cons * 0.55
        else:
            valor = kWh_cons * 0.60
    case _:
        print("Tipo de instalação inválido!")
        valor = 0

print(f"O valor a ser pago é: R$ {valor:2f}")
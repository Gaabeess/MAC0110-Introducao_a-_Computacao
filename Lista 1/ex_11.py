vel_atual = float(input("Qual a sua velocidade atual: "))

if vel_atual > 80:
    print("Você foi multado!")
    multa = (vel_atual - 80) * 5
    print(f"O valor da multa é: R${multa:.2f}")
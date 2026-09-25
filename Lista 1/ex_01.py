dados = ["dias","horas","minutos","segundos"]
valores = []

for i in dados:
    valores.append(int(input(f'Digite a quantidade de {i}: ')))
    

TotalSeg = valores[0]*86400 + valores[1]*3600 + valores[2]*60 + valores[3]

print(f"O total de segundos é: {TotalSeg}")
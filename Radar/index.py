velocidade = float(input('Qual a velcidade do veículo em km?'))
if velocidade > 80:
    print('velocidade acima do limite, você receberá uma multa de {}'.format((velocidade - 80) * 7))
else:
    print('Boa viagem')
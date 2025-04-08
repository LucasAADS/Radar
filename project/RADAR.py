speed = float(input('Qual a velocidade atual do carro? '))
if speed > 100:
    print('\033[31m' + 'O veículo está acima da velocidade permitida!' + '\033[0m')
    multa = (speed-100) * 7 # 7 reais por km ultrapassado.
    print('\033[31m' + 'Aplicaremos multa no valor de ' + '\033[0m''\033[33m' + f'R${multa:.2f}' + '\033[0m')

else:
    print('O veículo esta dentro da velocidade permitida, Você é um ótimo motorista!')
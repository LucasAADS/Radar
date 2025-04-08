num = int(input('Digite um número: '))
print('''Escolha uma das opções para conversão
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} Quando convertido para binário é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} Quando convertido para Octal é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'Quando convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção INVALIDA!!! Tente novamente')
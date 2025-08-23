
def calcular():
    print('\nBem-Vindo a calculadora!')
    print('=-' * 30)
    print('Escolha a operação: ')
    print('[ 1 ] - Adição (+)')
    print('[ 2 ] - Subtração (-)')
    print('[ 3 ] - Multiplicação (*)')
    print('[ 4 ] - Divisão (/)')
    print('=-' * 30)

    while True:
        try:
            operacao = int(input('\nDigite a operação desejada (1/2/3/4): '))
            if operacao not in [1, 2, 3, 4]:
                raise ValueError('Operação inválida. Tente novamente.')
            break
        except ValueError as e:
            print(e)

    try:
        num1 = float(input('Digite o primeiro número: ').strip())
        num2 = float(input('Digite o segundo número: ').strip())

        if operacao == 1: 
            resultado = num1 + num2
            print(f' {num1} + {num2} = {resultado}')
        elif operacao == 2: 
            resultado = num1 - num2
            print(f' {num1} - {num2} = {resultado}')
        elif operacao == 3: 
            resultado = num1 * num2
            print(f' {num1} * {num2} = {resultado}')
        elif operacao == 4:
            if num2 == 0:
                print('Erro: Divisão por zero não é permitida.')
            else:
                resultado = num1 / num2
                print(f' {num1} / {num2} = {resultado}')
    except ValueError:
        print('Erro: Por favor, insira números válidos.')

while True:
    calcular()
    reiniciar = input('\nDeseja realizar outro cálculo? (s/n): ').strip().lower()
    if reiniciar != 's':
        print('Obrigado por usar a calculadora. Até mais!')
        break

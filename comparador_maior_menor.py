def comparador_de_numero():
    resposta = ""
    while resposta != 'sair':
        primeiro_valor = float(input('Digite o primeiro valor: '))
        segundo_valor = float(input('Digite o segundo valor: '))
        if primeiro_valor > segundo_valor:
            print(f'O maior valor é {primeiro_valor}')
        elif primeiro_valor < segundo_valor:
            print(f'O maior valor é {segundo_valor}')
        else:
            print('Os valores são iguais')
        resposta = input('Deseja continuar? (sair para sair): ')

comparador_de_numero()
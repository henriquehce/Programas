nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em kg): '))

altura_f = float(altura)
peso_f = float(peso)
imc = peso_f / (altura_f ** 2)

print(f'{nome}, seu IMC é {imc:.2f}')
import random

numero_sorteado = random.randint(1, 100)

print('Chute um numero:')
seu_chute = int(input())

if seu_chute == numero_sorteado:
    print('Acertou!')
else:
    print('Errou! O numero era:')
    print(numero_sorteado)

# -*- coding: UTF-8
from random import randint
v = 0
print("="*24)
print("VAMOS JOGAR PAR OU IMPAR")
print("="*24)
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' 
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print("-"*40)
    print(f"Voce jogou {jogador} e o computador {computador}.Total de {total} ", end='')
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    print("-"*40)
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!!!")
            v += 1
        else:
            print("Você PERDEU :(")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você VENCEU!!!")
            v += 1
        else:
            print("Você PERDEU :(")
            break
    print("Vamos jogar novamente...")
    print("=-"*20)
print(f"GAME OVER! Você venceu {v} vezes.")


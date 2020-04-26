# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:10:10 2020

@author: paulo
"""


from random import randint
from time import sleep
import emoji

lista = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
perguntar = int(input('''Oi, escolha uma opção do JO-KEN-POOOO para jogar contra o computador:
[0] Pedra
[1] Papel
[2] Tesoura
Digite sua escolha: '''))

if perguntar > 2 or perguntar < 0:
    print(emoji.emojize(":skull: Bug de usuário :skull: comece de novo e digite uma opção válida.", use_aliases=True))

else:
    print("\nJO\n")
    sleep(0.8)
    print("KEEEEEEN\n")
    sleep(0.8)
    print("POOOOOOOOOOOOO!!!\n")
    sleep(1.0)
    print("-"*30)
    print("O computador escolheu: {}".format(lista[computador]))
    if computador ==0:
        print(emoji.emojize(":punch:", use_aliases=True))
    elif computador ==1:
        print(emoji.emojize(":raised_hand:", use_aliases=True))
    else:
        print(emoji.emojize(":v:", use_aliases=True))
    print("-"*30)
    print("O ser humano escolheu: {}".format(lista[perguntar]))
    if perguntar ==0:
        print(emoji.emojize(":punch:", use_aliases=True))
    elif perguntar ==1:
        print(emoji.emojize(":raised_hand:", use_aliases=True))
    else:
        print(emoji.emojize(":v:", use_aliases=True))
    print("-"*30)
if computador == 0:
    if perguntar == 0:
        print(emoji.emojize("Empate! Jogue de novo se quiser ganhar :trophy:", use_aliases=True))
    elif perguntar == 1:
        print(emoji.emojize("O ser humano venceu! :sunglasses:", use_aliases=True))
    elif perguntar == 2:
        print(emoji.emojize("Computador venceu :computer:", use_aliases=True))
    else:
        print("")
elif computador == 1:
    if perguntar == 0:
        print(emoji.emojize("Computador venceu :computer:", use_aliases=True))
    elif perguntar == 1:
        print(emoji.emojize("Empate! Jogue de novo se quiser ganhar :trophy:", use_aliases=True))
    elif perguntar == 2:
        print(emoji.emojize("O ser humano venceu! :sunglasses:", use_aliases=True))
    else:
        print("")
elif computador == 2:
    if perguntar == 0:
        print(emoji.emojize("O ser humano venceu! :sunglasses:", use_aliases=True))
    elif perguntar == 1:
        print(emoji.emojize("Computador venceu! :computer:", use_aliases=True))
    elif perguntar == 2:
        print(emoji.emojize("Empate! Jogue de novo se quiser ganhar :trophy:", use_aliases=True))
    else:
        print("")
else:
    print("Operacao inválida")
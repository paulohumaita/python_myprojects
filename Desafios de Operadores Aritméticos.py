# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:34:16 2020

@author: paulo
"""


#OPERADORES ARITMÉTICOS

#DESAFIO 005
#faça um programa que leia um número inteiro e mostre na tela o seu sucessor 
# e o seu antecessor


n = int(input('Digite um número: '))
x = n - 1
y = n + 1
print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, x, y))


#quanto menos variáveis, menos uso de memória, mais rápido o programa fica...
#uma forma mais otimizada, para esse exemplo seria:


n = int(input('Digite um número: '))
print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))


#DESAFIO 006
#crie um algorítmo que leia um número e mostre o seu dobro, tripo e raiz quadrada


n = float(input('Digite um número: '))

d = n * 2
t = n * 3
r = n**(1/2) #uma das formas de calcular raiz quadrada é elevar um número a 1/2
#outra forma de calcular raiz quadrada no Python é usando a função .sqrt da biblioteca math
#neste caso, ficaria r = math.sqrt(n), lembrando que daí teria que importar a biblioteca utilizando import math 

print(' O dobro de {} é {:.2f}, \n seu triplo é {:.2f} \n e sua raiz quadrada é {:.2f}'.format(n, d, t, r))


#DESAFIO 007
#desenvolva um programa que leia as duas notas de um aluno, 
#calcule e mostre a sua média


n1 = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('Qual foi a segunda nota do aluno? '))

nf = (n1 + n2) / 2 

print('\n Sendo a primeira nota {:.1f} e a segunda nota {:.1f}, \n a média final do aluno é {:.1f}'.format(n1, n2, nf))


#DESAFIO 008
#escreva um programa que leia um valor em metros e o exiba convertido em 
#centímetros e milímetros


m = float(input('Quanto que mede em metros? '))

cm = me * 100

mm = ce * 100

print('Este valor de {:.1f} em metros, corresponde a {:.1f} centímetros e a {:.1f} milímetros'.format(m, cm, mm))


#DESAFIO 009
#faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada


n = int(input('Ferinha, digite um número: '))

print('{} x {} = {}'.format(n, 1, (n*1))
print('{} x {} = {}'.format(n, 2, (n*2))
print('{} x {} = {}'.format(n, 3, (n*3))
print('{} x {} = {}'.format(n, 4, (n*4))
print('{} x {} = {}'.format(n, 5, (n*5))
print('{} x {} = {}'.format(n, 6, (n*6))
print('{} x {} = {}'.format(n, 7, (n*7))
print('{} x {} = {}'.format(n, 8, (n*8))
print('{} x {} = {}'.format(n, 9, (n*9))
print('{} x {} = {}'.format(n, 10, (n*10))


#ou poderia ser resolvido conforme abaixo também, já aplicando o método while
#o que deixaria o código bem mais limpo, leve e bonitão ;)


n = int(input('Ferinha, digite um número: '))
i = 1
print(':'*12) #dá pra colocar essa firulinha também pra ficar mais bonitim, em cima e em baixo da tabuada
while i <=10:

    print('{} x {:2} = '.format(n, i), n*i) #se quiser que fique alinhado ainda mais bonitinho é só usar {:2} na parte do multiplicador
    i = i + 1
print(':'*12)


#DESAFIO 010
#crie um programa que leia quanto dinheiro uma pessoa tem na carteira em reais
#e mostre quantos dólares ela pode comprar
#em época de pandemia, considere US$ 1.00 = R$ 5.80 (tá tenso heim Waldisney...)


dimdim = float(input('Waldisney, quanto dinheiro você tem na carteira? R$'))
cambio = 5.8

dolares = dimdim / cambio

print('Meu caro Waldisney, com essa quantidade de {:.1f} reais, você pode comprar {:.1f} dólares, considerando o câmbio durante a pandemia em torno de {:.1f}.'.format(dimdim, dolares, cambio))


#DESAFIO 011
#faça um programa que leia a altura e a largura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de dois metros quadrados.


alt = float(input('Qual é a altura dessa parede, em metros? '))
lar = float(input('Qual é a largura dessa parede, em metros? '))

area = alt * lar
tinta = area/2

print(' Como esta parede tem {:.1f}m²  de área, \n vamos precisar de {:.1f} litros de tinta para pintá-la.'.format(area, tinta))

#para fazer o 2 do m² basta segurar a tecla ALT direita do teclado e o número 2 


#DESAFIO 012
#faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.


p1 = float(input('Qual o preço do produto sem desconto? R$'))

p2 = p1 - (p1*0.05) #poderia ser também p2 = p1*95/100

print('Com 5% de desconto, o preço de produto passou de R${:.2f} para R${:.2f}'.format(p1, p2))


#DESAFIO 013
#faça um algoritmo que leia o salário de um funcionário e mostre seu novo
#salário, com 15% de aumento.


s1 = float(input('Quanto é o salário atual do funcionário? R$'))

s2 = s1 + (s1*0.15) #também poderia ser s2 = s1*115/100

print('O salário tinha o salário de R${:.2f}, mas com o aumento de 15% seu nome salário é de R${:.2f}.'.format(s1, s2))


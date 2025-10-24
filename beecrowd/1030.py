'''

BEE 1030 - A lenda de Flavius Josephus
Python 3.11
Autor: thealg0
Resolvido em: 24.10.2025

''' 

nc = int(input())

for i in range(0, nc):    

    n, k = map(int, input().split())

    lista = [i for i in range(0, n + 1)]

    posicao = lista.index(lista[-1]) # (4) ultimo item da lista
    tamanho_da_lista = n
    ultimo = 0


    while True:
        posicao = (posicao + k) % tamanho_da_lista
        ultimo = lista.pop(posicao)
        tamanho_da_lista -= 1
        posicao -= 1

        if(tamanho_da_lista == 1):
            ultimo = lista[0]
            print(f'Case {i+1}: {ultimo}')
            break









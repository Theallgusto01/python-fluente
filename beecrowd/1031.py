

#teste =  [{"regiao": regiao, "status": "ligado"} for regiao in range(1,17 + 1)]



passo = 5
teste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
proximo = 0

tamanho_da_lista = len(teste)

while True:

    print(f'Desligando {teste[proximo]}')
    ultimo = teste.pop(teste.index(teste[proximo]))
    proximo = (proximo + passo) % tamanho_da_lista
    tamanho_da_lista -= 1
    proximo -= 1
   

    if tamanho_da_lista == 1:
        print(f"ultimo {ultimo}")
        break
    
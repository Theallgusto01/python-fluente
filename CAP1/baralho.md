```python


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # def __len__(self):
    #     return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


```

### Ordenamento

Para mim, ficou meio confusa a expressão de retorno da função `spades_high`.

Acontece o seguinte:

Temos 4 cartas de cada numero, por exemplo: 
- 2 de espadas
- 2 de copas
- 2 de ouros
- 2 de paus

Logo, teremos blocos de 4 cartas. Por isso a multiplicação do valor da carta pelo numero de naipes (quatro) 

`rank_value * 4`

Exemplo:

2 de espadas = 0 * 4 = 0

2 de copas   = 0 * 4 = 0

2 de outos   = 0 * 4 = 0

2 de paus    = 0 * 4 = 0


Agora, precisamos ordenar as cartas de valores iguais, como as 4 cartas de número 2 do exemplo anterior, dentro do bloco. Por isso somar com o valor de cada naipe.


`rank_value * len(suits) + suits_value[card.suit] `

Valor : Espadas - 3, Copas - 2, Ouros - 1, Paus - 0

Exemplo:

2 de espadas = 0 * 4 = 0 + *3* -> *3*

2 de copas   = 0 * 4 = 0 + *2* -> *2*

2 de ouros   = 0 * 4 = 0 + *1* -> *1*

2 de paus    = 0 * 4 = 0 + *0* -> *0*


Pronto, o primeiro bloco está ordenado! Genial né?



```python
deck = FrenchDeck()
suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
      # ranks = [2,3,4,5,6,7,8,9,10,J,Q,K]
      # Pega o indice do item na lista ranks da classe frenchDeck para cada numero de carta
      # no baralho.
      # Ex. Priemeira carta: 2 de espadas Índice 0
      #     Segunda carta:   3 de espadas índice 1
     rank_value = FrenchDeck.ranks.index(card.rank)

     #Retorna o Índice do valor da carta na lista X quantidade de naipes X valor de cada naipe
     
     # Ex. 2 de espadas -> 0 X 4 + 3 = 3     2 de copas -> 0 X 4 + 2 = 2    2 de ouro -> 0 X 4 + 1 = 1  2 de paus -> 0 X 4 + 0 = 0
     #     3 de espadas -> 1 X 4 + 3 = 7     3 de copas -> 1 X 4 + 2 = 6    3 de ouro -> 1 X 4 + 1 = 5  3 de paus -> 1 X 4 + 0 = 4
     #     4 de espadas -> 2 X 4 + 3 = 11    4 de copas -> 2 X 4 + 2 = 10   4 de ouro -> 2 X 4 + 1 = 9  4 de paus -> 2 X 4 + 0 = 8
     
     return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
    
```

    Card(rank='2', suit='clubs')
    Card(rank='2', suit='diamonds')
    Card(rank='2', suit='hearts')
    Card(rank='2', suit='spades')
    Card(rank='3', suit='clubs')
    Card(rank='3', suit='diamonds')
    Card(rank='3', suit='hearts')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='clubs')
    Card(rank='4', suit='diamonds')
    Card(rank='4', suit='hearts')
    Card(rank='4', suit='spades')
    Card(rank='5', suit='clubs')
    Card(rank='5', suit='diamonds')
    Card(rank='5', suit='hearts')
    Card(rank='5', suit='spades')
    Card(rank='6', suit='clubs')
    Card(rank='6', suit='diamonds')
    Card(rank='6', suit='hearts')
    Card(rank='6', suit='spades')
    Card(rank='7', suit='clubs')
    Card(rank='7', suit='diamonds')
    Card(rank='7', suit='hearts')
    Card(rank='7', suit='spades')
    Card(rank='8', suit='clubs')
    Card(rank='8', suit='diamonds')
    Card(rank='8', suit='hearts')
    Card(rank='8', suit='spades')
    Card(rank='9', suit='clubs')
    Card(rank='9', suit='diamonds')
    Card(rank='9', suit='hearts')
    Card(rank='9', suit='spades')
    Card(rank='10', suit='clubs')
    Card(rank='10', suit='diamonds')
    Card(rank='10', suit='hearts')
    Card(rank='10', suit='spades')
    Card(rank='J', suit='clubs')
    Card(rank='J', suit='diamonds')
    Card(rank='J', suit='hearts')
    Card(rank='J', suit='spades')
    Card(rank='Q', suit='clubs')
    Card(rank='Q', suit='diamonds')
    Card(rank='Q', suit='hearts')
    Card(rank='Q', suit='spades')
    Card(rank='K', suit='clubs')
    Card(rank='K', suit='diamonds')
    Card(rank='K', suit='hearts')
    Card(rank='K', suit='spades')
    Card(rank='A', suit='clubs')
    Card(rank='A', suit='diamonds')
    Card(rank='A', suit='hearts')
    Card(rank='A', suit='spades')



```python
print(len(deck))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[12], line 1
    ----> 1 print(len(deck))


    TypeError: object of type 'FrenchDeck' has no len()


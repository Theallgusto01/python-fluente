"""
Tuplas são utilizadas para armazenar multiplos itens em uma única variável
Itens de uma tupla são ordenados, imutáveis e permitem valores duplicados
Pode conter tipos diferentes de itens

"""


tupla = ("maça", "banana", "abacate")

#  Direrente das listas, não é possível adicionar,
#  modificar ou remover itens depois que a tupla é criada 

print(tupla)
print(len(tupla))

# Podemos criar uma tupla com apenas um item, mas uma vírgula deve ser adicionada
# após o item, senão o Python não reconhece como uma tupla

tupla = ("Fulano",)
print(type(tupla))

tupla = ("Fulano")
print(type(tupla))

tupla = ("abc", 123, 34, 4.5, True)
print(tupla)

# É possivel usar o construtor da tupla -> tuple()

tupla = tuple(("maça", 123, False))

print(tupla)
print(type(tupla))

lista = ['maçã', 'banana', 'abacate']

print(reversed(lista))
tupla = reversed(tupla)

print(type(tupla))
print(type(lista))
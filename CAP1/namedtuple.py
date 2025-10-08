# namedtuple()

# 1. Mutabilidade -> Instancias de uma classe podem ser mutáveis ou imutáveis
#                    enquanto namedtuple() são imutáveis
# 2. Métodos -> Classes podem conter métodos, enquanto namedtuples primariamente
#               fornecem uma maneira de armazenar dados com campos nomeados
# 3. Herança -> Classes suportam herança, namedtuples não as suportam



import collections


Estudante = collections.namedtuple("Estudante", ["nome", "idade", "matricula"])

#Instanciando 

E1 = Estudante("Thiago", "22", "20211135000278")

print(E1)


# Operações de conversão de uma tupla nomeada
# _make() - Usada para retornar um namedtuple() de um iterável passado como argumento
#           no exemplo abaixo, uma lista para para uma tupla nomeada
#  _asdict() - Retonra o dicionario ordenado como contrução dos valores mapeados
#              da namedtuple()
# ** - Usado para converter um dicionario em uma namedtuple()

li = ["Milena", "23", "40028922"]

di = {'nome': "Fulano", 'idade': 23, 'matricula': '12345667' }

print(Estudante._make(li))
print(Estudante(**di))
print(E1._asdict())
print(Estudante._fields) #Retorna as chaves


# _replace() - Usado para alterar valores de um objeto namedtuple()

print(E1._replace(nome='Augusto'))

# __new__ - Retorna uma nova instância da classe estudante, tomando os valores
# passados como parametro

print(Estudante.__new__(Estudante,'Thiago','25','4321'))


# __getnewargs__ - Retorna a namedtuple() como uma tupla simples

print(E1.__getnewargs__())


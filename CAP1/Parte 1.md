# Um baralho pytônico

Uso o `collection.namedtuple` para criar uma classe simples

`Card = collection.namedtuple('Card', ['rank', 'suit'])`

Sintaxe: `namedtuple(nomeTipo, atributos)`

nomeTipo - O nome da tupla nomeada
atributos - Lista de atrbutos armazenados na tupla nomeada

### Collections

Implementa datatypes containerizados especializados em alternativa aos containers genéricos dict, list, set e tuple.


> O underscore (_) antes do inicio do atributo é uma convenção em python que indica que o método é interno/privado e não deveria ser 

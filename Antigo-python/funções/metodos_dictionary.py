### dictionary
pessoa = {
    'nome' : 'Jonathan',
    'sobrenome' : 'Nogueira',
}
### pega as chaves
print(pessoa.keys())

### pega values
print(pessoa.values())

### Usando items = pegar chave e valor
novaPessoa = pessoa.items()
print(novaPessoa)
for chave, valor in novaPessoa:
    print(chave, valor)

### setdefault = set chave e valor se a chave nao existir ou nao tiver um valor
pessoa.setdefault('idade', 100)
print(pessoa['idade'])

###copy - shallow copy
copia = {
    'name' : 'jonathan',
    'empresa': 'gerdau',
    'lista' : [0,1,2] 
}

copia2 = copia.copy()
print(copia)
print(copia2)


###Usando get
print(pessoa.get('valor', 'nao existe'))


### Pop
nome = pessoa.pop('nome')
print(nome)
print(pessoa) ### imprime pessoa (dictionary) sem a chave ('nome')



### Usando popItem metodo
itemEscuro = {
    'escova' : 'azul',
    'pasta' : 'colgate',
}


ultimaChaveDeletada = itemEscuro.popitem()
print(ultimaChaveDeletada)

### usando o UPDATE cria ou altera uma chave
itemEscuro.update({
        'escova' : 'vermelho',
        'nome' : 'colgate-luminus-white-update-agora',
    }
)
### Outra forma de atualizar tambem
itemEscuro.update(nome='jonathan', escola='verde')



print(itemEscuro)
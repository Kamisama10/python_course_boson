#dicionarios permitem adicionar dados em pares ou valor é uma coleção mutável
# e desordenada de itens armazenados como pares chave-valor.

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais alcalinos',
    'densidade': 0.534
}

print(f'elemento:  {elemento['nome']}')
print(f'densidade:  {elemento['densidade']}')
print(f'O dicionário possui {len(elemento)} elementos.')


#atualizar uma entrada do dicionário
elemento ['grupo'] = 'alcalinos'
print(elemento)

#adicionar uma entrada
elemento['período'] = 1
print(elemento)

#Exclusao de items em dicionarios
del elemento['período'] 
print(elemento)

#apagar todos os itens
elemento.clear()
print(elemento)
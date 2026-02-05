#manipular buscar uma letra do nome 
# nome = "kamila"
# letra = nome[2]
# print(letra)

#concatenacao
# nome = "Curso de Python"
# instrutor = "Kamila"
# print(nome + " com " + instrutor)
# print(len(nome))

#divide a string por partes
# frase = "vamos aprender Python hoje."
# palavras = frase.split()
# print(palavras[1])
# #separando palavras
# for palavra in palavras:
#     print(palavra)

# frase = "Vamos aprender Python hoje."
# print(frase[2:5])

# #metodo find encontrar uma palavra na frae
# email = input('Digite seu nedereço de email: ')
# arroba = email.find('@')
# print(arroba)

#encontrar uma palavra dentro de uma frase
# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

#pesquisar uma sequência de caracteres 
# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

#trabalhar com maiuscula e minusculo tambem upper é pra deixar tudo com letra maiuscula e lower minusculo tem o capitalize somente a primeira letra em maiusculo title tbm
# objeto_celeste = 'galaxia esPiral M31'
# print(objeto_celeste.upper())

#substituir uma palavra com replace
# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)

#trabalhar com espaços em branco com metodo lstrip
# frase = '       Omega 3 é bom para a saúde!      '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

#trabalhar com justificar texto com rjust
# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20))

#pergunta se começa com essas letras iniciais
# p = 'testando treinamentos'
# print(p.startswith('te'))
# print(p.endswith('s'))

#docstrings strings que usamos para documentar trechos especificos do codigo
"""
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função, ou classe no python entre outros locais
Respeita deslocamento do texto e é multilinhas 

"""

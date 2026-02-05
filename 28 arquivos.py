# Manipulação de arquivos de texto.

# Método read
# manipulador = open('arquivo.txt', 'r', encoding='utf-8')

# print(f'\Método read():\n')
# print(manipulador.read())

# Método readline

# manipulador = open('arquivo.txt', 'r', encoding='utf-8')

# print(f'\Método read():\n')
# print(manipulador.readline())



# Tratar exceções
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        print(linha)
except IOError:
    print(f'Não foi possível abr o arquivos')
else:
    manipulador.close()
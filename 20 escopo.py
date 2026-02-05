# Escopo Global e Local

var_global = 'Curso completo de Python'

def escreve_texto():
    global var_global
    var_global = 'Banco de dados com SQL'
    var_local = 'Kamila'
    print(f'Variavél Global: {var_global}')
    print(f'Variavél Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()


    print('Tentar acessar as varipaveis diretamente')
    print(f'Variavél Global: {var_global}')

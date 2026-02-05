# Exceção é um objeto que representa um erro que ocorreu ao executar o programa. 
# Blocos try ... except

# Tratar divisão por zero

def div(k, j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite um número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente.')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
    except:
        print(f'Ocorreu um erro desconhecido....')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\nFim do cálculo')









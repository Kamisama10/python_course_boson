from math import sqrt

if __name__=='__main__':
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'Foi fornecido um número negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do cálculo!')

# Exceções definidas pelo usuário
# from math import sqrt

# class NumeroNegativoError(Exception):
#     def __init__(self):
#         pass

# if __name__=='__main__':
#     try:
#         num = int(input('Digite um número positivo: '))
#         if num < 0:
#             raise NumeroNegativoError
#     except NumeroNegativoError:
#         print(f'Foi fornecido um número negativo!')
#     else:
#         print(f'A raiz quadrada de {num} é {sqrt(num)}')
#     finally:
#         print(f'Fim do cálculo!')

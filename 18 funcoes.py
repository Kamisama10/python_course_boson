#funcao é um bloco de codigo que executa uma determinada tarefa
#Modularização criando um bloco de codigo e usando posteriormente promovendo o reuso de código e melhora a legibilidade

# def <nome_funcao> ([argumentos]):
#     <intruções>

# def mensagem():
#     print('Teste em tecnologia')
#     print('Curso completo de python')

# mensagem()

#funcao com argumentos
# def soma(a, b):
#     print(a+b)

# soma(5,5)

#funcao que multiplica dois vlaores
# def mult(x, y):
#     return x * y

# a = 5
# b = 5
# c = mult(a, b)
# print(f'O produto de {a} e {b} é {c} ')

# def div(k, j):
#     if j != 0:
#         return k / j 
#     else:
#         return 'Impossível dividir por zero!'
    

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite um número: '))

#     r = div(a,b)
#     print(f'{a} dividido por {b} é igual a {r}')

#calcular valores de quadrados
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados 

if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)










#calcular nota do aluno com uma funcao e condicionais 
# def nota(x, y):
#     return (x + y) / 2

# nota1 = float(input('Digite a primeira nota:'))
# nota2 = float(input('Digite a segunda nota: '))
# media = nota(nota1, nota2)
# print(f'Nota final: {media} ')

# if media >= 7:
#     print('Aluno APROVADO')
# else:
#     print('Aluno REPROVADO!')
    
    
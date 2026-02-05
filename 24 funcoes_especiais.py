# Funções lambda (anônimas)
# Sintaxe:

# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# Dobrar números
# dobrar = lambda x: x * 2
# print(dobrar(5))


# Verificar se é par
# par = lambda x: x %2 == 0
# print(par(9))

# Verificar fa
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(212))

# Função map()
# Sintaxa
# map(função, iterável)

# valores da lista duplicados 
# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# TUDO EM MAIUSCULO A CADA ITEM DA LISTA PALAVRAS
# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# Função filter() ela filtra elementos de uma sequência
# Sintaxe:
# filter(função, sequência)
# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# Numeros impar
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)

# Funcao reduce()
# Sintaxa:
# reduce(função, sequência, valor_inicial)

from functools import reduce 

# def mult(x,y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# total = reduce(mult, numeros)
# print(total)

#Soma cumulativa dos quadrados de valores, usando expressão lambda 

numeros = [1,2,3,4]

total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)
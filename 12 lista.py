#Lista representa uma sequencia de valores armazenados na memoria 
#Listas em Python são coleções de valores mutáveis e ordenados, definidas entre colchetes [] e acessíveis por índices a partir de 0.
#sintaxe: nome_lista = [valores]

#lista basica
# notas = [5,7,8,6,9]
# print(notas)

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,4]
valores = n1 + n2

#print(type(valores))

#filtrar por posicao/indice
#valores[0] = 9 
#funcoes de tamanho da lista, soma, minimo, maximo e sequencia. 
# print(len(valores))
# print(sorted(valores, reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

#metodos para manipular dados da lista (alterando)

# valores.append(13) #adiciona valores a lista
# print(valores)
# valores.pop() #remove/retira elementos da lista se eu nao colocar nenhum parametro ele remove qualquer um
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21) #dois argumentos numeros da posicao onde vou inserir o item e logo apos o valor a ser adicionado
# print(valores)
# print(12 in valores) #o valor 12 esta dentro da lista valores? ele vai retornar true ou false

# planetas = ["Mercurio", "Venus", "Marte", "Saturno", "Urano", "Netuno"]
# for planeta in planetas:
#     print(planeta)

#exercicio crie um script que peça ao usuario digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
bebidas = []

for i in range(5):
    print(f"Digite uma bebida favorita: ")
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f"\n Bebidas escolhidas: ")
for bebida in bebidas:
    print(bebida)

print(f"\nSaúde!")







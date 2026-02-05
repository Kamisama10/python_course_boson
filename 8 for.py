#for em Python cria um loop que percorre elementos de uma sequência (lista, string, range, etc.)

#laço for
# for item in sequência:
#instruções executadas para cada item da sequência

# lista = [2,6,9,4,0,12,3,7]

# #para cada item dentro da lista faça alguma coisa com esse item
# for item in lista:
#     print(item)


# lista = [2,6,9,4,0,12,3,7]
# palavra = "Aula"
# #para cada letra em palavra mostre na tela a letra
# for letra in palavra:
#     print(letra)


# for numero in range(1,10):
#     print(numero)

#repetir um nome digitado pelo usuario 10 vezes
# nome = input("Digite seu nome:")
# for x in range(10):
#     print(f"{x+1} {nome}")

#range (valor_inicial, valor_final, incremento)
# for x in range(2,20,2):
#     print(x)

pedras = ("Rubi", "Esmeralda", "Quartzo", "Safira", "Diamante", "Turmalina")

for pedra in pedras:
    if pedra == "Quartzo":
        continue
    print(pedra)
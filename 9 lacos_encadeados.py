#Laços encadeados em Python sao loops dentro de loops usados quando precisamos percorrer varias dimensoes ou combinacoes

# for cont_ex in range(1,6):
#     print(f"\nRodada: {cont_ex}")
#     for cont_in in range(5,0,-1):
#         print(f"Valor: {cont_in}")

# print("Fim dos laços de repetição")

#gerar conjuntos diferentes de valores
import random 

#Isso cria um loop que vai repetir 5 vezes. A vai valer 1, 2, 3, 4 e 5 em cada repetição.
for A in range(1,6):
    print(f"\nConjunto {A}")
    #Aqui tem um loop dentro do loop (chamado de loop aninhado).Esse loop vai repetir 5 vezes para cada valor de A.
    for B in range(5):
        #Gera um número aleatório entre 1 e 100. Cada vez que o loop roda, num muda para um novo valor.
        num = random.randint(1,100)
        print(f"Valor: {num}")

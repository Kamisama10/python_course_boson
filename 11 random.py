import random 

#Essa linha de código gera números aleatórios de 1 a 20 como colocado no parametro
# valor = random.randint(1,20)
# print(valor)

#essa linha gerar 5 numeros INTEIROS aleatorios de 1 a 50 aleatorios 5 vezes com laço for 5 vezes.
# print("Gerar cinco números aleatórios entre 1 e 50: \n")
# for i in range(5):
#     n = random.randint(1,50)
#     print(f"Número gerado: {n}")

#gerar numero aleatorio com ponto flutuante float e multiplicando por outros valores. o round é pra arrendodar as casas decimais
#random.random nao aceita parametros ja o random.uniform aceita parametros.
# valor = random.random()
# print(f"Número gerado: {round(valor * 10, 2)}")

#com parametros numeros aleatorios float
# valor = random.uniform(1,100)
# print(f"Número: {round(valor, 4)}")

#escolhe um número dentro da lista declarada na variavel a funcao random.choice 
L = [1,2,3,4,5,6,7,8,9]
# n = random.choice(L)
# print(f"Número escolhido:  {n}")

#extrair varios valores de uma vez dentro da lista declarada com metodo sample significa amostragem
# n = random.sample(L,3)
# print(f"O números extraidos: {n}")

#funcao para embaralhar os números metodo shuffle
print(f"Exigir a lista original: {L}")
print(f"Embaralhar a lista e exibir-la: ")
n = random.shuffle(L)
print(L)

#Operadores lógicos em Python servem para combinar condições e retornam True ou False

#TABELA VERDADE
# OPERADOR AND
# false + false = false
# true + false = false
# false + true = false
# true + true = true

# OPERADOR OR
# false + false = false
# true + false = true
# false + true = true
# true + true = true

#OPERADOR NOT
# false + true
# true + false

#idade = 15
#altura = 1.75

#resultado = (idade >= 18) and (altura >= 1.70)
#msg = "Pode participar do evento?" + str(resultado)

#print(msg)

#Programa de disparo de alarme
# porta = "f"
# janela = "f"

# alarme = (porta == "a") or (janela == "a")
# msg = "Alarme disparado?" + str(alarme)
# print(msg)

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = "Tem dinheiro?" + str(tem_dinheiro)
print(msg)
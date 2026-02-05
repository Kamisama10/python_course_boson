#set significa conjunto é uma coleção não ordenada e mutável de elementos únicos

planeta_anao = {'Plutão', 'Ceres','Eris', 'Haumena', 'Makemake'}
print(len(planeta_anao))
#print('Ceres' in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley' }
print(astros1 == astros2)
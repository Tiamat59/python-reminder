
dict = {'name':'brown','prenom':'alphonse'}
print('Affichage dict par index')
print(dict['name'])

print('Parcours dict index et value')
for i,v in dict.items():
    print(i)
    print(v)
print('Parcours dict sur la value')
for v in dict.values():
    print(v)
print('Parcours dict seulement sur l\'index')
for i in dict:
    print(i)


list = ('test1','test2','test3')
print('Affichage liste par index')
print(list[0])

print('Parcours list juste la value')
for v in list:
    print(v)
print('Parcours list index et value')
for i,v in enumerate(list):
    print(i)
    print(v)




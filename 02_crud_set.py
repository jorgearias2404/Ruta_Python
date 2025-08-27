set_countries = {'col','mex','bol','col'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add agrega un unico elemento
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update agrega subconjunto
set_countries.update({'ar','ecu','pe'})
print(set_countries)

#remove eliminaun elemnto del conjunto
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

"""
este caso arrojara error porque ese elemento
no eciste dentro del conjunto 

set_countries.remove('arge')
print(set_countries)

en su lugar si no sabemos con certeza la 
existencia de un objeto utilizamos discard
"""

#discard asi evitas errores en caso de que no exista
set_countries.discard('arge')
print(set_countries)

#clear elimina todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
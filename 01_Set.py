"""
Los conjuntos no tienen orden
los conjuntosno tienen duplicados
se pueden modificar los conjuntos
"""

set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,3,4,5,6,6,6,}
print(set_numbers)

set_mix = {1,3,"Hola",'saludo',float}
print(set_mix)

set_from_string = set("Hola") #conjunto a partir de un string
print(set_from_string)

set_from_tuples = set(('abc','cbv','cab','abc'))
print(set_from_tuples)

numbers = [1,2,3,4,5,6,6,6]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
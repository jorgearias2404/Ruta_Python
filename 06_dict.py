
import random

countries = ['col','mex','per']

population_v2 = {country:random.randint(1,100) for country in countries }
print(population_v2)

result = {country:population for (country,population) in population_v2.items() if population >20}

print(result)


text = 'Hola, soy jorge'
unique={C:C.upper() for C in text if C in 'aeiou'}
print(unique)

text = 'Hola, soy jorge'
unique={C:text.count(C) for C in text if C in 'aeiou'}
print(unique)
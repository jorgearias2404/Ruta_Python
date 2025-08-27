numbers = []

for element in range(1,11):
    numbers.append(element * 2)
    
print(numbers)

#usando list compression
numbers_V2 = [element * 2 for element in range(1,11)]
print(numbers_V2)


numbers_v3 = []

for element in range(1,11):
    if element%2 == 0:
        numbers_v3.append(element *2)
print(numbers_v3)

numbers_V4 = [element*2 for element in range(1,11) if element%2 ==0]
print(numbers_V4)
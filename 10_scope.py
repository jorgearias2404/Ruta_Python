price = 100 #global

def increment():
    price = 200
    price = price + 10 #local
    print(price)

increment()
print(price) 
    
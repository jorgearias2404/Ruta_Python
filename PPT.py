import random

options = ['piedra','papel,','tijera']

computer_wins = 0
user_wins = 0

rounds = 1
while True:
    print('='*10)
    print('ROUND',rounds)
    print('='*10)
    
    print('computer', computer_wins)
    print('user',user_wins)
    
    user_op = input('piedra,papel o tijeras =>')  
    user_op = user_op.lower()
    
    comp_op = random.choice(options)
    
    if user_op == 'piedra' and comp_op =='tijera':
        print('ganador user')
        user_wins+=1
    elif user_op == 'tijera' and comp_op =='papel':
        print('ganador user')
        user_wins+=1
    elif user_op == 'papel' and comp_op =='piedra':
        print('ganador user')
        user_wins+=1
    else:
        print('ganador comp')
        computer_wins+=1
        
    if rounds ==3:
        print("GANADOR ES:")
        if user_wins > computer_wins:
            print("User")
        else:
            print("Comp")
        break
    rounds+=1
    
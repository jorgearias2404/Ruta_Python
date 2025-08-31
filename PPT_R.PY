import random

def winner(j1, j2):
    if j1 > j2:
        print("GANADOR: User")
    elif j1 < j2:
        print("GANADOR: Computer")
    else:
        print("EMPATE")

def Round(j1, j2):
    if j1 == 'piedra' and j2 == 'tijera':
        print('ganador Round: user')
        return True
    elif j1 == 'tijera' and j2 == 'papel':
        print('ganador Round: user')
        return True
    elif j1 == 'papel' and j2 == 'piedra':
        print('ganador Round: user')
        return True
    elif j1 == j2:
        print('EMPATE en el Round')
        return None  # Empate
    else:
        print('ganador Round: Computer')
        return False

def Points():
    options = ['piedra', 'papel', 'tijera']  
    
    while True:
        j1_op = input('piedra, papel o tijera => ').lower().strip()
        if j1_op in options:
            break
        else:
            print("Opción no válida. Elige entre: piedra, papel, tijera")
    
    pc_op = random.choice(options)
    print(f"User: {j1_op} vs Computer: {pc_op}")
    
    result = Round(j1_op, pc_op)
    if result is True:
        print('Punto para user')
        return 1, 0
    elif result is False:
        print('Punto para computer')
        return 0, 1
    else:
        print('Empate, nadie gana punto')
        return 0, 0
        
def Game():
    rounds = 1
    j1, pc = 0, 0
    
    while True:
        print('='*20)
        print(f'ROUND {rounds}')
        print('='*20)
        
        print(f'Computer: {pc} puntos')
        print(f'User: {j1} puntos')
        print()
        
        r1, r2 = Points()
        j1 += r1
        pc += r2
        
        print(f"Marcador actual - User: {j1} | Computer: {pc}")
        
        if j1 >= 3 or pc >= 3:
            winner(j1, pc)
            break
        
        rounds += 1
        print('#'*20)
        print()  # Línea en blanco para separar rounds

# Ejecutar el juego
Game()
import numpy as np
import time
import random

def buscador_objetos():
    grid = np.zeros((5,5), dtype=int)
    x, y = 0, 0  # Posición inicial del agente
    obj_x, obj_y = random.randint(0, 4), random.randint(0, 4)
    grid[obj_x, obj_y] = 2  # Posición del objeto
    
    while (x, y) != (obj_x, obj_y):
        grid[x, y] = 1
        print(grid)
        time.sleep(1)
        grid[x, y] = 0
        if x < obj_x:
            x += 1
        elif x > obj_x:
            x -= 1
        elif y < obj_y:
            y += 1
        elif y > obj_y:
            y -= 1
    print("Objeto encontrado!")

if __name__ == "__main__":
    buscador_objetos()

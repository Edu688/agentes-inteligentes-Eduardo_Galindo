import time
import random


def semaforo_inteligente():
    estados = ['Verde', 'Amarillo', 'Rojo']
    
    while True:
        vehiculos = random.randint(0, 20)  # Simula el tráfico
        
        if vehiculos > 10:
            tiempo_verde = 10
        else:
            tiempo_verde = 5
        
        print(f"Estado: {estados[0]} - Duración: {tiempo_verde} segundos")
        time.sleep(tiempo_verde)
        print(f"Estado: {estados[1]} - Duración: 2 segundos")
        time.sleep(2)
        print(f"Estado: {estados[2]} - Duración: 5 segundos")
        time.sleep(5)

if __name__ == "__main__":
    semaforo_inteligente()

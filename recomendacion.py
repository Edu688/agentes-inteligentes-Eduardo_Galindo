import random

def recomendacion_peliculas():
    peliculas = {
        "accion": ["Mad Max", "John Wick", "Gladiador"],
        "comedia": ["Superbad", "The Hangover", "Step Brothers"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "El Padrino"]
    }
    
    genero = input("Ingrese su género favorito (accion, comedia, drama): ").lower()
    if genero in peliculas:
        print(f"Te recomendamos: {random.choice(peliculas[genero])}")
    else:
        print("Género no disponible.")
if __name__ == "__main__":
    recomendacion_peliculas()

def diagnostico():
    sintomas = input("Ingrese los síntomas separados por comas: ").lower().split(",")

    
    enfermedades = {
        "gripe": ["fiebre", "tos", "dolor de garganta"],
        "migraña": ["dolor de cabeza", "náuseas", "sensibilidad a la luz"],
        "alergia": ["estornudos", "picazón en ojos", "congestión nasal"]
    }
    
    
    for enfermedad, lista_sintomas in enfermedades.items():
        if all(sintoma.strip() in lista_sintomas for sintoma in sintomas):
            print(f"Posible diagnóstico: {enfermedad.capitalize()}.")
            return
    print("Diagnóstico no encontrado.")

if __name__ == "__main__":
    diagnostico()

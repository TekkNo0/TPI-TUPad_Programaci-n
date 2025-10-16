import csv

# Defino el nombre de la base de datos
DATABASE = "DataBase.csv" 

def busqueda_pais(nombre_a_buscar):
    """Busca un país por nombre en el archivo CSV."""
    
    # Abro el archivo
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        # Creo el lector que recibe el objeto archivo
        lector = csv.reader(archivo, delimiter=";")
        
        # Salto el encabezado
        next(lector, None) 
        
        # Iterar sobre las filas (países)
        for fila in lector:
            # La columna del nombre del país es la primera (índice 0)
            nombre_pais = fila[0]
            
            # Comprobar si el país coincide (ignorando mayúsculas/minúsculas)
            if nombre_pais.lower() == nombre_a_buscar.lower():
                # Si lo encuentra, devuelve la fila completa
                return fila 
                
    # Si el bucle termina sin encontrar el país
    return f"País '{nombre_a_buscar}' no encontrado."


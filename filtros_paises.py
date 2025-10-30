import csv

# Defino el nombre de la base de datos
DATABASE = "DataBase.csv" 

def paises_en_continente(paises_en_continente):
    """Filtra los paises por continente en el archivo CSV."""
    
    # Abro el archivo
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) 

        #Se crea una lista para agregar los paises pertenecientes al continente
        paises = []

        #Iteración sobre las filas (continentes)
        for fila in lector:
            # La columna del nombre del país es la primera (índice 0)
            nombre_continente = fila[1] 

            # Comprobar si el país coincide (ignorando mayúsculas/minúsculas)
            if nombre_continente.lower() == paises_en_continente.lower():
                #Se agregan los paises que cumplan con las condiciones a la lista
                paises.append(fila)
        if paises:
            return paises
        
    # Si el bucle termina sin encontrar el continente
    return f"Continente '{paises_en_continente}' no encontrado."

def paises_por_poblacion(rango_poblacion):
    """Filtra los paises por rango de población en el archivo CSV."""
    # Abro el archivo
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) 
        #Se crea una lista para agregar los paises pertenecientes al rango de población
        paises = []
        #Iteración sobre las filas (población)
        for fila in lector:
            # La columna de la población es la tercera (índice 2)
            # Intentar convertir valores que puedan contener separadores o decimales
            quitar_separadores = fila[2].strip()
            poblacion = int(quitar_separadores.replace(".", "").replace(",", ""))

            # Comprobar si la población está dentro del rango dado
            if rango_poblacion[0] <= poblacion <= rango_poblacion[1]:
                #Se agregan los paises que cumplan con las condiciones a la lista
                paises.append(fila)
        if paises:
            return paises

        # Si no se encontraron países en el rango
        return f"No se encontraron países con población en el rango {rango_poblacion}."
    
def paises_por_superficie(rango_superficie):
    """Filtra los paises por rango de superficie en el archivo CSV."""
    # Abro el archivo
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) 
        #Se crea una lista para agregar los paises pertenecientes al rango de superficie indicado
        paises = []
        #Iteración sobre las filas (superficie)
        for fila in lector:
            # La columna de la población es la tercera (índice 3)
            # Intentar convertir valores que puedan contener separadores o decimales
            quitar_separadores = fila[3].strip()
            poblacion = int(quitar_separadores.replace(".", "").replace(",", ""))

            # Comprobar si la población está dentro del rango dado
            if rango_superficie[0] <= poblacion <= rango_superficie[1]:
                #Se agregan los paises que cumplan con las condiciones a la lista
                paises.append(fila)
        if paises:
            return paises
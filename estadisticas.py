import csv

DATABASE = "DataBase.csv"

#Función para limpiar los . de los numeros y los datos hacerlos int
def _limpiar_numero(numero_str):
    return int(numero_str.replace(".", ""))

#Función para encontrar el pais con la maxima población
def pais_maxpoblacion():
    maxpob_valor = -1 #Variables para guardar y comparar los resultados de los paises.
    pais_max = None

    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) # Saltar encabezado
            
        for fila in lector:
            poblacion = _limpiar_numero(fila[2]) #Llama a la función y limpia los . de la poblacion 
            if poblacion > maxpob_valor: #Compara el numero y si es mayor entra a la condición y actualiza los valores de las variables
                maxpob_valor = poblacion 
                pais_max = fila
    return f"País con Mayor Población: {str(pais_max)}"

#Encuentra el país con la menor población
def pais_minpoblacion():
    minpob_valor = float('inf') #Se asigna valor infinito para comparar
    pais_min = None
    
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) # Saltar encabezado
            
        for fila in lector:
            poblacion = _limpiar_numero(fila[2])
            if poblacion < minpob_valor: #Compara el numero y si es menor entra a la condición y actualiza los valores de las variables
                minnpob_valor = poblacion
                pais_min = fila
        return f"País con Menor Población: {str(pais_min)}"

#Funcion para definir el promedio de población y superficie
def promedio():
    total_poblacion = 0 #Variables para calcular
    total_superficie = 0
    total_paises = 0
    
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) 
            
        for fila in lector: #Bucle que recorre la base de datos y va sumando la población y superficie 
            total_poblacion += _limpiar_numero(fila[2])
            total_superficie += _limpiar_numero(fila[3])
            total_paises += 1 #Contador para el calculo de promedio
            continue
    promedio_pob = total_poblacion / total_paises #Calculo del promedio
    promedio_sup = total_superficie / total_paises
        
    return (f"Promedio de Población: {promedio_pob:,.0f} hab.\n"
            f"Promedio de Superficie: {promedio_sup:,.2f} km²")

#Función para contar cuantos paises hay en cada continente
def conteo_continentes():
    conteo = {}
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None) # Saltar encabezado
            
        for fila in lector:
            continente = fila[1]
            conteo[continente] = conteo.get(continente, 0) + 1
                    
    string_salida = "Países por Continente:"
    for continente, cantidad in conteo.items():
        string_salida += f"\n   - {continente}: {cantidad} países"
        
    return string_salida
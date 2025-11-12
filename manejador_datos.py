import csv

DATABASE = "DataBase.csv"
HEADERS = ['Nombre', 'Continente', 'Poblacion', 'Superficie']

def _limpiar_y_convertir_numero(texto_num):
    if not isinstance(texto_num, str):
        return int(texto_num) # Si ya es un número, lo devuelve
    try:
        # Quita puntos (separadores de miles) y luego convierte a entero
        return int(texto_num.replace(".", "").strip())
    except (ValueError, TypeError):
        return 0 # Devuelve 0 si el dato está vacío o corrupto

def cargar_datos():
    """
    Carga el archivo CSV una sola vez usando DictReader.
    Limpia y convierte los datos numéricos al cargarlos.
    Devuelve una lista de diccionarios.
    """
    datos_paises = []
    try:
        with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
            # Usa DictReader con el delimitador correcto
            lector = csv.DictReader(archivo, delimiter=";")
            
            for fila in lector:
                try:
                    # Limpia y convierte los datos numéricos en el momento
                    fila['Poblacion'] = _limpiar_y_convertir_numero(fila.get('Poblacion', 0))
                    fila['Superficie'] = float(_limpiar_y_convertir_numero(fila.get('Superficie', 0))) # Superficie como float
                    
                    # Asegura que las otras claves existan
                    fila['Nombre'] = fila.get('Nombre', 'Desconocido')
                    fila['Continente'] = fila.get('Continente', 'Desconocido')
                    
                    datos_paises.append(fila)
                except Exception as e:
                    print(f"Error procesando fila: {fila}. Error: {e}")
                    
        print(f"Datos cargados: {len(datos_paises)} países leídos.")
        return datos_paises

    except FileNotFoundError:
        print(f"ERROR: No se pudo encontrar el archivo '{DATABASE}'.")
        print("Asegúrate de que el archivo existe o actualízalo desde la API.")
        return None # Devuelve None para que Main.py pueda manejarlo
    except Exception as e:
        print(f"ERROR inesperado al cargar el archivo: {e}")
        return None
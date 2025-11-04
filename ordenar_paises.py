import csv


DATABASE = "DataBase.csv" 

# Fuunción q lee el CSV y prepara los datos para ordenar

def _cargar_y_preparar_datos():
    # Creo una lista para guardar los datos leídos
    datos = []
    
    # Abro archivo y compruebo excepciones.
    try:
        with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
            # Defino el lector de CSV con delimitador ;
            lector = csv.reader(archivo, delimiter=";")
            
            # Intento saltar el encabezado
            try:
                next(lector, None) 
            except StopIteration:
                pass # El archivo está vacío
                
            # Itero sobre cada fila del lector
            for fila in lector:
                if not fila:
                    continue # Omite líneas vacías

                try:
                    fila_limpia = fila[:] 
                    try:
                        # (fila[2] or 0) maneja celdas vacías
                        fila_limpia[2] = int(fila[2] or 0) 
                    except (ValueError, TypeError):
                        fila_limpia[2] = 0 # Asigno 0 si falla
                    
                    # Intento convertir Superficie a número (float)
                    try:
                        fila_limpia[3] = float(fila[3] or 0)
                    except (ValueError, TypeError):
                        fila_limpia[3] = 0.0 # Asigno 0 si falla

                    # Agrego la fila limpia a la lista de datos
                    datos.append(fila_limpia)
                
                except IndexError:
                    continue # Omite la fila malformada (no tiene suficientes columnas)

    # Manejo de errores de archivo
    except FileNotFoundError:
        return (None, f"ERROR: No se pudo encontrar el archivo '{DATABASE}'.")
    except PermissionError:
        return (None, f"ERROR: No hay permisos para leer el archivo '{DATABASE}'.")
    except Exception as e:
        return (None, f"ERROR inesperado al procesar el archivo: {e}")
    
    # Devuelvo los datos y 'None' (sin error)
    return (datos, None)


def _formatear_y_devolver(lista_ordenada):
    
    ##Funciónpara convertir la lista de listas en un string final
    # Si hay resultados en la lista ordenada
    if lista_ordenada:
        # Convierte cada lista (fila) en un string.
        lista_string = [str(fila) for fila in lista_ordenada]
        # Une las lineas de string con un salto de línea.
        string_final = "\n".join(lista_string)
        return string_final
    
    # Si no encuentra nada...
    else:
        return "No se encontraron datos para ordenar."



def ordenar_por_nombre(descendente=False):
    """
    Ordena la lista de países por nombre (índice 0).
    """
    # Llamo a la función interna para cargar los datos CADA VEZ
    datos_paises, error_carga = _cargar_y_preparar_datos()
    
    # Primero, compruebo si hubo un error al cargar el archivo
    if error_carga:
        return error_carga
    
    # Ordeno la lista de países usando el índice 0 (Nombre)
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila[0], 
        reverse=descendente
    )
    
    # Devuelvo la lista formateada como string
    return _formatear_y_devolver(lista_ordenada)


def ordenar_por_poblacion(descendente=False):
    # Llamo a la función interna para cargar los datos CADA VEZ
    datos_paises, error_carga = _cargar_y_preparar_datos()

    # Compruebo si hubo un error al cargar el archivo
    if error_carga:
        return error_carga
    
    # Ordeno usando el índice 2 (Población), que ya convertimos a 'int'
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila[2], 
        reverse=descendente
    )
    
    # Devuelvo la lista formateada como string
    return _formatear_y_devolver(lista_ordenada)


def ordenar_por_superficie(descendente=False):
    # Llamo a la función interna para cargar los datos CADA VEZ
    datos_paises, error_carga = _cargar_y_preparar_datos()

    # Compruebo si hubo un error al cargar el archivo
    if error_carga:
        return error_carga
        
    # Ordeno usando el índice 3 que estaba en float
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila[3], 
        reverse=descendente
    )
    
    # Devuelvo la lista ya formateada
    return _formatear_y_devolver(lista_ordenada)
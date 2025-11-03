import csv

#Defino el nombre de la base de datos
DATABASE = "DataBase.csv" 

#Función que busca y retorna el nombre del pais en el csv
def busqueda_pais(nombre_a_buscar):
    
    #Creo una lista para guardar los resultados que encuentre, sea parcial o no
    resultados_encontrados = []
    
    #Abro archivo y compruebo excepciones.
    try:
        with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            try:
                next(lector, None) #Salto el encabezado
            except StopIteration:
                pass 
                
            for fila in lector:
                if not fila:
                    continue

                try:
                    nombre_pais = fila[0]
                    
                    # Comprobacion si el nombre_a_buscar está en el nombre pais
                    if nombre_a_buscar.lower() in nombre_pais.lower():
                        # Si esta lo agrega a la lista de resultados
                        resultados_encontrados.append(fila)
                
                except IndexError:
                    continue # Omite la fila malformada

    except FileNotFoundError:
        return f"ERROR: No se pudo encontrar el archivo '{DATABASE}'."
    except PermissionError:
        return f"ERROR: No hay permisos para leer el archivo '{DATABASE}'."
    except Exception as e:
        return f"ERROR inesperado al procesar el archivo: {e}"
    
    #Si hay resultados entra en la condicion 
    if resultados_encontrados:
        
        # Convierte cada lista en string
        lista_string = [str(fila) for fila in resultados_encontrados]
        
        # Une las lineas de string
        string_final = "\n".join(lista_string)
        
        return string_final
        
    # Si no encuentra nada devuelve mensaje de error
    else:
        return f"No se encontraron países que contengan '{nombre_a_buscar}'."
import csv
import requests

DATABASE = "DataBase.csv"
# Define las cabeceras que el resto de tu aplicación espera
HEADERS = ['Nombre', 'Continente', 'Poblacion', 'Superficie']

def actualizar_csv_desde_api():
    url = "https://restcountries.com/v3.1/all"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza excepción si hay error HTTP

        paises = respuesta.json()

        with open(DATABASE, "w", newline="", encoding="utf-8") as archivo:
            # --- CAMBIOS IMPORTANTES ---
            # 1. Usa DictWriter para escribir diccionarios
            # 2. Especifica el delimitador ';'
            # 3. Especifica los fieldnames (cabeceras)
            escritor = csv.DictWriter(archivo, fieldnames=HEADERS, delimiter=';')
            
            # Escribe la fila de cabeceras (ej. Nombre;Continente;...)
            escritor.writeheader()
            # ---------------------------

            for p in paises:
                try:
                    # Extrae los datos de la API
                    nombre = p.get("name", {}).get("common", "Desconocido")
                    poblacion = p.get("population", 0)
                    superficie = p.get("area", 0)
                    continente = p.get("region", "Desconocido")
                    
                    # Crea un diccionario que coincida con tus HEADERS
                    fila_dict = {
                        'Nombre': nombre,
                        'Continente': continente,
                        'Poblacion': poblacion,
                        'Superficie': superficie
                    }
                    
                    # Escribe la fila usando el diccionario
                    escritor.writerow(fila_dict)
                    
                except Exception as e:
                    print(f"Error al procesar país: {e}")

        print("Archivo CSV actualizado con datos desde la API (formato correcto ';').")

    except requests.exceptions.RequestException as e:
        print("Error al conectar con la API:", e)
    except Exception as e:
        print("Error inesperado:", e)
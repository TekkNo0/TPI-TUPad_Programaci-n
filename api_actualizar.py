import csv
import requests

DATABASE = "DataBase.csv"

def actualizar_csv_desde_api():
    url = "https://restcountries.com/v3.1/all"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  #Lanza excepción si hay error HTTP

        paises = respuesta.json()

        with open(DATABASE, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

            for p in paises:
                try:
                    nombre = p.get("name", {}).get("common", "Desconocido")
                    poblacion = p.get("population", 0)
                    superficie = p.get("area", 0)
                    continente = p.get("region", "Desconocido")

                    escritor.writerow([nombre, poblacion, superficie, continente])
                except Exception as e:
                    print(f"Error al procesar país: {e}")

        print("Archivo CSV actualizado con datos desde la API.")

    except requests.exceptions.RequestException as e:
        print("Error al conectar con la API:", e)

    except Exception as e:
        print("Error inesperado:", e)
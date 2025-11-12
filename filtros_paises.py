import csv
import os

DATABASE = "DataBase.csv"


#Funciones de validación

def validar_archivo():
    #Verifica si el archivo CSV existe y no está vacío.
    if not os.path.exists(DATABASE):
        raise FileNotFoundError(f"El archivo '{DATABASE}' no existe.")
    if os.path.getsize(DATABASE) == 0:
        raise ValueError(f"El archivo '{DATABASE}' está vacío.")


def validar_continente(nombre: str) -> str:
    #Valida que el nombre del continente sea una cadena no vacía.
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del continente no puede estar vacío.")
    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre del continente no puede contener números.")
    return nombre.strip()


def validar_rango_numerico(rango) -> tuple:
    #Valida que el rango sea una tupla/lista de dos números válidos y positivos.
    if not isinstance(rango, (list, tuple)) or len(rango) != 2:
        raise TypeError("El rango debe ser una tupla o lista con dos valores (mínimo y máximo).")
    try:
        minimo, maximo = map(int, rango)
    except ValueError:
        raise ValueError("El rango debe contener solo números enteros.")

    if minimo < 0 or maximo < 0:
        raise ValueError("Los valores del rango deben ser positivos.")
    if minimo > maximo:
        raise ValueError("El rango mínimo no puede ser mayor que el máximo.")
    return minimo, maximo


def convertir_a_entero(valor: str) -> int:
    #Convierte una cadena con separadores o decimales a un número entero seguro.
    try:
        limpio = valor.strip().replace(".", "").replace(",", "")
        return int(limpio)
    except (ValueError, AttributeError):
        raise ValueError(f"Valor numérico inválido: '{valor}'.")


#Funciones de filtro para el codigo principal

def paises_en_continente(nombre_continente: str):
    #Devuelve una lista de países pertenecientes a un continente.
    validar_archivo()
    nombre_continente = validar_continente(nombre_continente)

    paises = []
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None)  # omitir encabezado

        for fila in lector:
            if len(fila) < 2:
                continue  # salta filas incompletas
            if fila[1].strip().lower() == nombre_continente.lower():
                paises.append(fila)

    if paises:
        return paises
    return f"No se encontraron países en el continente '{nombre_continente}'."


def paises_por_poblacion(rango_poblacion):
    #Filtra países por rango de población.
    validar_archivo()
    minimo, maximo = validar_rango_numerico(rango_poblacion)

    paises = []
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None)

        for fila in lector:
            if len(fila) < 3:
                continue
            try:
                poblacion = convertir_a_entero(fila[2])
            except ValueError:
                continue
            if minimo <= poblacion <= maximo:
                paises.append(fila)

    if paises:
        return paises
    return f"No se encontraron países con población entre {minimo} y {maximo}."


def paises_por_superficie(rango_superficie):
    #Filtra países por rango de superficie.
    validar_archivo()
    minimo, maximo = validar_rango_numerico(rango_superficie)

    paises = []
    with open(DATABASE, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None)

        for fila in lector:
            if len(fila) < 4:
                continue
            try:
                superficie = convertir_a_entero(fila[3])
            except ValueError:
                continue
            if minimo <= superficie <= maximo:
                paises.append(fila)

    if paises:
        return paises
    return f"No se encontraron países con superficie entre {minimo} y {maximo}."
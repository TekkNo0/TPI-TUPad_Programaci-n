# No se necesita csv, os, nin DATABASE

# --- Funciones de validación (se mantienen si aún son necesarias) ---
# Se elimina validar_archivo()
# Se elimina convertir_a_entero()

def validar_continente(nombre: str) -> str:
    # (Esta función se mantiene sin cambios si la necesitas)
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del continente no puede estar vacío.")
    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre del continente no puede contener números.")
    return nombre.strip()

def validar_rango_numerico(rango) -> tuple:
    # (Esta función se mantiene sin cambios)
    if not isinstance(rango, (list, tuple)) or len(rango) != 2:
        raise TypeError("El rango debe ser una tupla o lista con dos valores (mínimo y máximo).")
    try:
        minimo, maximo = map(int, rango)
    except ValueError:
        raise ValueError("El rango debe contener solo números enteros.")
    if minimo < 0 or maximo < 0:
        raise ValueError("Los valores del rango deben ser positivos.")
    if minimo > maximo:
        return maximo, minimo # Corrige el rango si está invertido
    return minimo, maximo

# --- Funciones de filtrado (modificadas) ---

# Acepta la lista 'datos_paises'
def paises_en_continente(nombre_continente, datos_paises):
    try:
        nombre_validado = validar_continente(nombre_continente)
    except ValueError as e:
        return f"Error: {e}"

    paises = []
    # Itera sobre la lista de diccionarios
    for fila in datos_paises:
        # Compara usando la clave 'Continente'
        if fila['Continente'].lower() == nombre_validado.lower():
            paises.append(fila) # Guarda el diccionario completo

    if paises:
        return paises # Devuelve una lista de diccionarios
    return f"No se encontraron países en el continente '{nombre_validado}'."

# Acepta la lista 'datos_paises'
def paises_por_poblacion(rango_poblacion, datos_paises):
    try:
        minimo, maximo = validar_rango_numerico(rango_poblacion)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    paises = []
    # Itera sobre la lista de diccionarios
    for fila in datos_paises:
        # Los datos en fila['Poblacion'] YA SON enteros
        if minimo <= fila['Poblacion'] <= maximo:
            paises.append(fila)

    if paises:
        return paises
    return f"No se encontraron países con población entre {minimo} y {maximo}."

# Acepta la lista 'datos_paises'
def paises_por_superficie(rango_superficie, datos_paises):
    try:
        minimo, maximo = validar_rango_numerico(rango_superficie)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    paises = []
    # Itera sobre la lista de diccionarios
    for fila in datos_paises:
        # Los datos en fila['Superficie'] YA SON floats/int
        if minimo <= fila['Superficie'] <= maximo:
            paises.append(fila)

            # Comprobar si la población está dentro del rango dado
            if rango_superficie[0] <= poblacion <= rango_superficie[1]:
                # Se agregan los paises que cumplan con las condiciones a la lista
                paises.append(fila)
        if paises:
            return paises
# No se necesita csv, os, nin DATABASE

# --- Nueva Función de Formato (copiada de ordenar_paises.py) ---

def _formatear_y_devolver(lista_paises):
    """
    Función auxiliar para convertir la lista de diccionarios
    en un string legible.
    """
    if not lista_paises:
        # Esta función de formato asume que la lista no está vacía,
        # las funciones de filtro ya manejan el caso de "no encontrado".
        return "No hay países para mostrar."
    
    lineas = []
    # Itera sobre la lista de diccionarios
    for fila in lista_paises:
        # Formatea usando las claves del diccionario
        linea = (f"- {fila['Nombre']} "
                f"(Pob: {fila['Poblacion']:,.0f}, "
                f"Sup: {fila['Superficie']:,.2f} km², "
                f"Cont: {fila['Continente']})")
        lineas.append(linea)
        
    return "\n".join(lineas)

# --- Funciones de validación (sin cambios) ---

def validar_continente(nombre: str) -> str:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del continente no puede estar vacío.")
    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre del continente no puede contener números.")
    return nombre.strip()

def validar_rango_numerico(rango) -> tuple:
    if not isinstance(rango, (list, tuple)) or len(rango) != 2:
        raise TypeError("El rango debe ser una tupla o lista con dos valores (mínimo y máximo).")
    try:
        minimo, maximo = map(int, rango)
    except ValueError:
        raise ValueError("El rango debe contener solo números enteros.")
    if minimo < 0 or maximo < 0:
        raise ValueError("Los valores del rango deben ser positivos.")
    if minimo > maximo:
        return maximo, minimo
    return minimo, maximo

# --- Funciones de filtrado (modificadas para usar el formato) ---

def paises_en_continente(nombre_continente, datos_paises):
    try:
        nombre_validado = validar_continente(nombre_continente)
    except ValueError as e:
        return f"Error: {e}"

    paises = []
    for fila in datos_paises:
        if fila['Continente'].lower() == nombre_validado.lower():
            paises.append(fila)

    if paises:
        # ¡CAMBIO AQUÍ! Llama a la función de formato
        return _formatear_y_devolver(paises)
    
    return f"No se encontraron países en el continente '{nombre_validado}'."

def paises_por_poblacion(rango_poblacion, datos_paises):
    try:
        minimo, maximo = validar_rango_numerico(rango_poblacion)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    paises = []
    for fila in datos_paises:
        if minimo <= fila['Poblacion'] <= maximo:
            paises.append(fila)

    if paises:
        # ¡CAMBIO AQUÍ! Llama a la función de formato
        return _formatear_y_devolver(paises)
        
    return f"No se encontraron países con población entre {minimo} y {maximo}."

def paises_por_superficie(rango_superficie, datos_paises):
    try:
        minimo, maximo = validar_rango_numerico(rango_superficie)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    paises = []
    for fila in datos_paises:
        if minimo <= fila['Superficie'] <= maximo:
            paises.append(fila)

    if paises:
        # ¡CAMBIO AQUÍ! Llama a la función de formato
        return _formatear_y_devolver(paises)
        
    return f"No se encontraron países con superficie entre {minimo} y {maximo}."
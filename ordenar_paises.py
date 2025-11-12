# No se necesita csv ni DATABASE
# Se elimina la función _cargar_y_preparar_datos()

def _formatear_y_devolver(lista_paises):
    """
    Función auxiliar para convertir la lista de diccionarios ordenados
    en un string legible.
    """
    if not lista_paises:
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

# Acepta 'datos_paises' y 'descendente'
def ordenar_por_nombre(datos_paises, descendente=False):
    if not datos_paises:
        return "No hay datos para ordenar."
    
    # Ordena la lista usando la clave 'Nombre'
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila['Nombre'], 
        reverse=descendente
    )
    
    return _formatear_y_devolver(lista_ordenada)

# Acepta 'datos_paises' y 'descendente'
def ordenar_por_poblacion(datos_paises, descendente=False):
    if not datos_paises:
        return "No hay datos para ordenar."
    
    # Ordena la lista usando la clave 'Poblacion' (ya es un int)
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila['Poblacion'], 
        reverse=descendente
    )
    
    return _formatear_y_devolver(lista_ordenada)

# Acepta 'datos_paises' y 'descendente'
def ordenar_por_superficie(datos_paises, descendente=False):
    if not datos_paises:
        return "No hay datos para ordenar."
    
    # Ordena la lista usando la clave 'Superficie' (ya es un float)
    lista_ordenada = sorted(
        datos_paises, 
        key=lambda fila: fila['Superficie'], 
        reverse=descendente
    )
    
    return _formatear_y_devolver(lista_ordenada)
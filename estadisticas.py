# No se necesita csv ni DATABASE
# Se elimina la función _limpiar_numero()

# Acepta la lista 'datos_paises'
def pais_maxpoblacion(datos_paises):
    if not datos_paises:
        return "No hay datos para calcular."
    
    # Usa max() con una lambda, accediendo a la clave 'Poblacion'
    # Los datos ya son números
    pais_max = max(datos_paises, key=lambda p: p['Poblacion'])
    
    return f"País con Mayor Población: {pais_max['Nombre']} ({pais_max['Poblacion']:,.0f})"

# Acepta la lista 'datos_paises'
def pais_minpoblacion(datos_paises):
    if not datos_paises:
        return "No hay datos para calcular."
        
    # Usa min() con una lambda
    pais_min = min(datos_paises, key=lambda p: p['Poblacion'])
    
    return f"País con Menor Población: {pais_min['Nombre']} ({pais_min['Poblacion']:,.0f})"

# Acepta la lista 'datos_paises'
def promedio(datos_paises):
    if not datos_paises:
        return "No hay datos para calcular."
        
    total_paises = len(datos_paises)
    
    # Usa sum() con un generador para sumar los valores de la clave
    total_poblacion = sum(p['Poblacion'] for p in datos_paises)
    total_superficie = sum(p['Superficie'] for p in datos_paises)
    
    promedio_pob = total_poblacion / total_paises
    promedio_sup = total_superficie / total_paises
        
    return (f"Promedio de Población: {promedio_pob:,.0f} hab.\n"
            f"Promedio de Superficie: {promedio_sup:,.2f} km²")

# Acepta la lista 'datos_paises'
def conteo_continentes(datos_paises):
    if not datos_paises:
        return "No hay datos para calcular."

    conteo = {}
    # Itera sobre la lista de diccionarios
    for fila in datos_paises:
        # Accede por clave 'Continente'
        continente = fila['Continente']
        conteo[continente] = conteo.get(continente, 0) + 1
            
    # Formatea el resultado
    resultado = "Conteo por Continente:\n"
    for continente, cantidad in conteo.items():
        resultado += f"  - {continente}: {cantidad} países\n"
    return resultado.strip()
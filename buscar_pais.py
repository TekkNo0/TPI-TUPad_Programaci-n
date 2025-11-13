

# La función ahora acepta 'datos_paises' como argumento
def busqueda_pais(nombre_a_buscar, datos_paises):
    
    # Lista para guardar los diccionarios que coincidan
    resultados_encontrados = []
    
    # Itera sobre la lista de diccionarios ya cargada
    for fila in datos_paises:
        try:
            # Accede a los datos por clave ('Nombre')
            if nombre_a_buscar.lower() in fila['Nombre'].lower():
                resultados_encontrados.append(fila)
        
        except KeyError:
            # En caso de que una fila no tenga la clave 'Nombre'
            print(f"Advertencia: Fila malformada omitida: {fila}")
            continue
    
    # Si hay resultados, los formatea
    if resultados_encontrados:
        
        # Formatea la lista de diccionarios para una mejor lectura
        lineas_string = []
        for pais in resultados_encontrados:
            linea = (f"País: {pais['Nombre']}, " 
                    f"Continente: {pais['Continente']}, "
                    f"Población: {pais['Poblacion']:,.0f}, "
                    f"Superficie: {pais['Superficie']:,.2f} km²")
            lineas_string.append(linea)

        return "\n".join(lineas_string)

    else:
        return f"No se encontraron países que contengan '{nombre_a_buscar}'."
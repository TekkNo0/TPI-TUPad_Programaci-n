import csv #Importo libreria csv
from buscar_pais import busqueda_pais #Importo las diferentes funciones de cada archivo
from filtros_paises import paises_en_continente
from filtros_paises import paises_por_poblacion
from filtros_paises import paises_por_superficie
from estadisticas import (pais_maxpoblacion,pais_minpoblacion,promedio,conteo_continentes)
from ordenar_paises import (ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie)

menu = True
while menu:
    print("\n(1)-> Buscar País (nombre)")
    print("(2)-> Filtrar países (por continente, rango de población o rango de superficie)")
    print("(3)-> Ordenar países")
    print("(4)-> Estadísticas globales")
    print("(4)-> Salir del programa")
    # Pido al usuario que ingrese una opción
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción inválida. Ingrese un número.")
        continue # Vuelve al bucle     
    if opcion == 1:
        # Pido el nombre del país al usuario
        nombre_pais = input("Ingrese el nombre del país a buscar: ")

        # LLamo a la función, y doy el nombre como argumento
        resultado = busqueda_pais(nombre_pais)
        print("\n--- Resultado de la Búsqueda ---")
        print(resultado)
        print("----------------------------------")

    elif opcion == 2:
        try:
            filtro = int(input("\nSi desea filtrar por continente ingrese '1', por rango de población '2' o por rango de superficie '3': "))
        except ValueError:
            print("Opción inválida. Ingrese un número.")
            continue # Vuelve al bucle
        if filtro == 1:
            continente = input("Ingrese el nombre del continente:")
            resultado = paises_en_continente(continente)
            print("\n--- Resultado del Filtro por Continente ---")
            print(resultado)
        elif filtro == 2:
            try:
                min_poblacion = int(input("Ingrese la población mínima: "))
                max_poblacion = int(input("Ingrese la población máxima: "))
            except ValueError:
                print("Entrada inválida. Ingrese números enteros para la población.")
                continue # Vuelve al bucle
            rango_poblacion = (min_poblacion, max_poblacion)
            resultado = paises_por_poblacion(rango_poblacion)
            print("\n--- Resultado del Filtro por Rango de Población ---")
            print(resultado)
        elif filtro == 3:
            try:
                min_poblacion = int(input("Ingrese el valor de la superficie mínima: "))
                max_poblacion = int(input("Ingrese el valor de la superficie máxima: "))
            except ValueError:
                print("Entrada inválida. Ingrese números enteros para la superficie.")
                continue # Vuelve al bucle
            rango_superficie = (min_poblacion, max_poblacion)
            resultado = paises_por_superficie(rango_superficie)
            print("\n--- Resultado del Filtro por Rango de Superficie ---")
            print(resultado)
        else:
            print("Opción inválida. Inténtelo nuevamente.")
            continue # Vuelve al bucle
    elif opcion == 3:
        print("\n--- Opciones de Ordenamiento ---")
        print("(1) Por Nombre (A-Z)")
        print("(2) Por Población")
        print("(3) Por Superficie")
        
        # Pido al usuario el criterio
        try:
            opcion_orden = int(input("Seleccione el criterio de ordenamiento: "))
        except ValueError:
            print("Opción inválida. Ingrese un número.")
            continue # Vuelve al bucle principal

        # Por defecto, el orden es Ascendente (False)
        descendente = False
        
        # Pregunto por la dirección solo si es población o superficie
        if opcion_orden == 2 or opcion_orden == 3:
            try:
                direccion = int(input("Ingrese '1' para Ascendente o '2' para Descendente: "))
                if direccion == 2:
                    descendente = True # True significa descendente
                elif direccion != 1:
                    print("Dirección inválida. Se usará Ascendente por defecto.")
            except ValueError:
                print("Entrada inválida. Se usará Ascendente por defecto.")

        # Llamo a la función correspondiente
        if opcion_orden == 1:
            # Por nombre, solo llamamos ascendente (descendente=False)
            resultado = ordenar_por_nombre(False) 
            print("\n--- Países Ordenados por Nombre (A-Z) ---")
            print(resultado)
        
        elif opcion_orden == 2:
            # Por población, paso la variable 'descendente' (True o False)
            resultado = ordenar_por_poblacion(descendente)
            tipo_orden = "Descendente" if descendente else "Ascendente"
            print(f"\n--- Países Ordenados por Población ({tipo_orden}) ---")
            print(resultado)
            
        elif opcion_orden == 3:
            # Por superficie, paso la variable 'descendente' (True o False)
            resultado = ordenar_por_superficie(descendente)
            tipo_orden = "Descendente" if descendente else "Ascendente"
            print(f"\n--- Países Ordenados por Superficie ({tipo_orden}) ---")
            print(resultado)
            
        else:
            print("Criterio de ordenamiento no reconocido.")
    elif opcion == 4:
        print("\n--- Estadísticas Globales ---")
        print(pais_maxpoblacion())
        print(pais_minpoblacion())
        print(promedio())
        print(conteo_continentes())
    elif opcion == 5:
        print("Saliendo del programa. ¡Adiós!") #Salgo del programa
        break 
    else:
        print("Opción no reconocida. Intente de nuevo.")
import csv
from buscar_pais import busqueda_pais
from filtros_paises import paises_en_continente
from filtros_paises import paises_por_poblacion

menu = True
while menu:
    print("\n(1)-> Buscar País (nombre)")
    print("(2)-> Filtrar países (continente, rango de población o rango de superficie)")
    print("(3)-> Salir")
    #Pido al usuario que ingrese una opción
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
            print("----------------------------------")
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
            print("----------------------------------")
    elif opcion == 3:
        print("Saliendo del programa. ¡Adiós!")
        #Salgo del programa
        break
        
    else:
        print("Opción no reconocida. Intente de nuevo.")
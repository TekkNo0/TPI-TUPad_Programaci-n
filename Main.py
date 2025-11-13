# Importa la función de carga del nuevo módulo
from manejador_datos import cargar_datos

# Importa las demás funciones
from buscar_pais import busqueda_pais
from filtros_paises import paises_en_continente, paises_por_poblacion, paises_por_superficie
from estadisticas import (pais_maxpoblacion, pais_minpoblacion, promedio, conteo_continentes)
from ordenar_paises import (ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie)
from api_actualizar import actualizar_csv_desde_api
import sys # Para salir si el archivo no se carga

# --- Carga de datos UNA SOLA VEZ ---
# Llama a la función para cargar los datos al inicio
lista_paises = cargar_datos() 

# Si los datos no se pudieron cargar (ej. archivo no existe), ofrece actualizar o salir.
if lista_paises is None:
    print("\nNo se pudieron cargar los datos iniciales.")
    resp = input("¿Desea intentar actualizar los datos desde la API? (s/n): ")
    if resp.lower() == 's':
        actualizar_csv_desde_api()
        lista_paises = cargar_datos() # Intenta cargar de nuevo
        if lista_paises is None:
            print("Error: Sigue sin poderse cargar los datos. Saliendo.")
            sys.exit(1) # Termina el programa
    else:
        print("Saliendo del programa.")
        sys.exit(1) # Termina el programa
# ------------------------------------


menu = True
while menu:
    print("\n(1)-> Buscar País (nombre)")
    print("(2)-> Filtrar países (por continente, rango de población o rango de superficie)")
    print("(3)-> Ordenar países")
    print("(4)-> Estadísticas globales")
    print("(5)-> Actualizar datos desde API") # Opción añadida para recargar
    print("(6)-> Salir del programa")
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción inválida. Ingrese un número.")
        continue

    if opcion == 1:
        nombre_pais = input("Ingrese el nombre del país a buscar: ")
        # Pasa la lista de países a la función
        resultado = busqueda_pais(nombre_pais, lista_paises)
        print(resultado)

    elif opcion == 2:
        # --- BLOQUE CORREGIDO ---
        print("\n--- Filtrar Países ---")
        sub_opcion = input("Filtrar por (C)ontinente, (P)oblación, (S)uperficie: ").upper()
        
        if sub_opcion == 'C':
            continente = input("Ingrese el nombre del continente: ")
            # Pasa la lista de países
            resultado = paises_en_continente(continente, lista_paises)
            print(resultado)
        
        elif sub_opcion == 'P':
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                # Pasa la lista de países
                resultado = paises_por_poblacion((min_pob, max_pob), lista_paises)
                print(resultado)
            except ValueError:
                print("Error: Ingrese solo números para la población.")

        elif sub_opcion == 'S': # --- ESTA PARTE FALTABA ---
            try:
                min_sup = int(input("Superficie mínima (km²): "))
                max_sup = int(input("Superficie máxima (km²): "))
                # Pasa la lista de países
                resultado = paises_por_superficie((min_sup, max_sup), lista_paises)
                print(resultado)
            except ValueError:
                print("Error: Ingrese solo números para la superficie.")
        
        else:
            print("Opción de filtro no válida.")

    elif opcion == 3:
        # ... (lógica de submenú de orden sin cambios) ...
        criterio = int(input("Ordenar por (1) Nombre, (2) Población, (3) Superficie: "))
        orden = input("Orden (A)scendente o (D)escendente: ").upper()
        descendente = (orden == 'D')
        
        if criterio == 1:
            # Pasa la lista de países
            resultado = ordenar_por_nombre(lista_paises, descendente)
        elif criterio == 2:
            # Pasa la lista de países
            resultado = ordenar_por_poblacion(lista_paises, descendente)
        elif criterio == 3:
            # Pasa la lista de países
            resultado = ordenar_por_superficie(lista_paises, descendente)
        else:
            resultado = "Criterio no válido."
        print(resultado)

    elif opcion == 4:
        print("\n--- Estadísticas Globales ---")
        # Pasa la lista de países a todas las funciones de estadísticas
        print(pais_maxpoblacion(lista_paises))
        print(pais_minpoblacion(lista_paises))
        print(promedio(lista_paises))
        print(conteo_continentes(lista_paises))

    elif opcion == 5:
        print("Actualizando datos desde la API...")
        actualizar_csv_desde_api()
        # Vuelve a cargar los datos en la variable principal
        lista_paises = cargar_datos()
        print("Datos actualizados y recargados.")

    elif opcion == 6:
        print("Saliendo del programa.")
        menu = False

    else:
        print("Opción no válida. Intente de nuevo.")
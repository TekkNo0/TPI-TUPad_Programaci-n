import csv
from buscar_pais import busqueda_pais 

menu = True
while menu:
    print("\n(1)-> Buscar País (nombre)")
    print("(2)-> (Opción vacía)")
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
        print("Opción 2 seleccionada, pero está vacía.")
        
    elif opcion == 3:
        print("Saliendo del programa. ¡Adiós!")
        #Salgo del programa
        break
        
    else:
        print("Opción no reconocida. Intente de nuevo.")
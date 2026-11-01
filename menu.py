def mostrar_menu():
    """
    Muestra en pantalla las opciones del sistema.
    """
    print("\n========== BIBLIOTECA - LIBROS Y PRÉSTAMOS ==========")
    print("1. Listado de libros")
    print("2. Consulta de libro por código")
    print("3. Alta de libro")
    print("4. Modificación de libro")
    print("5. Baja de libro (en cascada)")
    print("6. Listado cruzado de préstamos")
    print("7. Consulta de préstamos por código de libro")
    print("8. Estadísticas")
    print("9. Generar reporte_prestamos.txt")
    print("0. Salir")


def pedir_opcion():
    """
    Muestra el menú y pide una opción entre 0 y 9.
    Reintenta mientras la opción no sea numérica o esté fuera de rango.
    """
    valido = False
    opcion = -1

    while not valido:
        mostrar_menu()
        try:
            entrada = input("Ingrese una opción: ").strip()

            if not entrada.isdigit():
                raise ValueError("Debe ingresar un número.")

            opcion = int(entrada)

            if opcion < 0 or opcion > 9:
                raise ValueError("La opción debe estar entre 0 y 9.")

            valido = True

        except ValueError as error:
            print(f"Error: {error}")

    return opcion

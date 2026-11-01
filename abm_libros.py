from archivos import leer_libros, leer_prestamos, guardar_libros, guardar_prestamos
from validaciones import ( validar_entero_positivo, validar_entero_no_negativo, validar_texto, validar_confirmacion )


def buscar_libro(libros, codigo_buscado):
    # Busca un libro por código y devuelve su posición o -1 si no existe.
    posicion = -1
    i = 0

    while i < len(libros) and posicion == -1:
        if libros[i][0] == codigo_buscado:
            posicion = i
        else:
            i += 1

    return posicion


def pedir_texto_modificado(mensaje, valor_actual):
    # Permite mantener el texto actual al presionar Enter o valida el nuevo.
    valido = False
    resultado = valor_actual

    while not valido:
        entrada = input(mensaje).strip()

        if entrada == "":
            resultado = valor_actual
            valido = True
        elif ";" in entrada:
            print("Error: el texto no puede contener punto y coma.")
        else:
            resultado = entrada
            valido = True

    return resultado


def pedir_ejemplares_modificados(mensaje, valor_actual):
    # Permite mantener la cantidad actual con Enter o valida un entero no negativo.
    valido = False
    resultado = valor_actual

    while not valido:
        entrada = input(mensaje).strip()

        if entrada == "":
            resultado = valor_actual
            valido = True
        else:
            try:
                numero = int(entrada)

                if numero < 0:
                    raise ValueError("El número no puede ser negativo.")

                resultado = numero
                valido = True

            except ValueError as error:
                print(f"Error: {error}")

    return resultado


def alta_libro():
    # Da de alta un nuevo libro validando que el código no esté repetido.
    libros = leer_libros()

    print("\n--- ALTA DE LIBRO ---")
    codigo = validar_entero_positivo("Ingrese el código del libro: ")

    posicion = buscar_libro(libros, codigo)

    if posicion != -1:
        print("Error: ya existe un libro registrado con ese código.")
    else:
        titulo = validar_texto("Ingrese el título: ")
        categoria = validar_texto("Ingrese la categoría: ")
        autor = validar_texto("Ingrese el autor: ")
        ejemplares = validar_entero_no_negativo("Ingrese la cantidad de ejemplares: ")

        nuevo_libro = [codigo, titulo, categoria, autor, ejemplares]
        libros.append(nuevo_libro)
        guardar_libros(libros)

        print("Libro agregado correctamente.")


def modificar_libro():
    # Modifica los datos de un libro existente conservando campos al presionar Enter.
    libros = leer_libros()

    if len(libros) > 0:
        print("\n--- MODIFICACIÓN DE LIBRO ---")
        codigo = validar_entero_positivo("Ingrese el código del libro a modificar: ")

        posicion = buscar_libro(libros, codigo)

        if posicion == -1:
            print("No se encontró un libro con ese código.")
        else:
            libro = libros[posicion]

            print(f"Libro actual: {libro[0]} - {libro[1]} | Categoría: {libro[2]} | Autor: {libro[3]} | Ejemplares: {libro[4]}")
            print("Presione Enter sin escribir nada para mantener el valor actual.")

            nuevo_titulo = pedir_texto_modificado(f"Nuevo título ({libro[1]}): ", libro[1])
            nueva_categoria = pedir_texto_modificado(f"Nueva categoría ({libro[2]}): ", libro[2])
            nuevo_autor = pedir_texto_modificado(f"Nuevo autor ({libro[3]}): ", libro[3])
            nuevos_ejemplares = pedir_ejemplares_modificados(f"Nuevos ejemplares ({libro[4]}): ", libro[4])

            libros[posicion] = [codigo, nuevo_titulo, nueva_categoria, nuevo_autor, nuevos_ejemplares]
            guardar_libros(libros)

            print("Libro modificado correctamente.")


def baja_libro():
    # Elimina un libro y todos sus préstamos asociados previa confirmación.
    libros = leer_libros()
    prestamos = leer_prestamos()

    if len(libros) > 0:
        print("\n--- BAJA DE LIBRO ---")
        codigo = validar_entero_positivo("Ingrese el código del libro a eliminar: ")

        posicion = buscar_libro(libros, codigo)

        if posicion == -1:
            print("No se encontró un libro con ese código.")
        else:
            libro = libros[posicion]

            cantidad_prestamos = 0
            for prestamo in prestamos:
                if prestamo[1] == codigo:
                    cantidad_prestamos += 1

            print(f"Libro seleccionado: {libro[0]} - {libro[1]} ({libro[3]})")
            print(f"Categoría: {libro[2]} | Ejemplares: {libro[4]}")
            print(f"Préstamos asociados a este libro: {cantidad_prestamos}")

            confirmacion = validar_confirmacion("¿Confirma la baja del libro y sus préstamos asociados? (S/N): ")

            if confirmacion == "S":
                nuevos_libros = []
                for item in libros:
                    if item[0] != codigo:
                        nuevos_libros.append(item)

                nuevos_prestamos = []
                for prestamo in prestamos:
                    if prestamo[1] != codigo:
                        nuevos_prestamos.append(prestamo)

                guardar_libros(nuevos_libros)
                guardar_prestamos(nuevos_prestamos)

                print("Baja realizada correctamente.")
            else:
                print("Baja cancelada. No se modificaron los archivos.")

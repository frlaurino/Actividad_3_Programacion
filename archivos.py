
def leer_libros():
    
    # Lee los registros de libros.txt. Devuelve una matriz con los datos de los libros.
    
    libros = []
    archivo = None

    try:
        archivo = open("libros.txt", "r", encoding="UTF-8")

    except FileNotFoundError:
        print("No se encontró el archivo libros.txt.")

    except OSError as error:
        print(f"Error al abrir libros.txt: {error}")

    else:
        for linea in archivo:
            campos = linea.strip().split(";")

            libro = [
                int(campos[0]),
                campos[1],
                campos[2],
                campos[3],
                int(campos[4])
            ]

            libros.append(libro)

    finally:
        if archivo != None:
            archivo.close()

    return libros


def leer_prestamos():
    
    # Lee los registros de prestamos.txt. Devuelve una matriz con los datos de los préstamos.
    
    prestamos = []
    archivo = None

    try:
        archivo = open("prestamos.txt", "r", encoding="UTF-8")

    except FileNotFoundError:
        print("No se encontró el archivo prestamos.txt.")

    except OSError as error:
        print(f"Error al abrir prestamos.txt: {error}")

    else:
        for linea in archivo:
            campos = linea.strip().split(";")

            prestamo = [
                int(campos[0]),
                int(campos[1]),
                int(campos[2])
            ]

            prestamos.append(prestamo)

    finally:
        if archivo != None:
            archivo.close()

    return prestamos


def guardar_libros(libros):
    
    # Recibe una matriz de libros y sobrescribe libros.txt.

    archivo = None

    try:
        archivo = open("libros.txt", "w", encoding="UTF-8")

    except OSError as error:
        print(f"Error al guardar libros.txt: {error}")

    else:
        for libro in libros:
            linea = f"{libro[0]};{libro[1]};{libro[2]};{libro[3]};{libro[4]}\n"
            archivo.write(linea)

    finally:
        if archivo != None:
            archivo.close()


def guardar_prestamos(prestamos):
   
    # Recibe una matriz de préstamos y sobrescribe prestamos.txt.
   
    archivo = None

    try:
        archivo = open("prestamos.txt", "w", encoding="UTF-8")

    except OSError as error:
        print(f"Error al guardar prestamos.txt: {error}")

    else:
        for prestamo in prestamos:
            linea = f"{prestamo[0]};{prestamo[1]};{prestamo[2]}\n"
            archivo.write(linea)

    finally:
        if archivo != None:
            archivo.close()

from abm_libros import buscar_libro
from validaciones import validar_entero_positivo


def mostrar_ficha_libro(libro):
    """
    Muestra en pantalla la ficha de un libro.
    Recibe una fila de la matriz de libros: [codigo, titulo, categoria, autor, ejemplares].
    """
    print(f"Libro: {libro[1]} | Categoria: {libro[2]} | Autor: {libro[3]}")
    print(f"Ejemplares registrados: {libro[4]}")


def listar_libros(libros):
    """
    Opción 1: muestra todos los libros en una tabla alineada.
    Recibe la matriz de libros. Si está vacía, informa y no muestra la tabla.
    """
    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        print(f"{'CODIGO':<8}{'TITULO':<36}{'CATEGORIA':<17}{'AUTOR':<15}{'EJEMPL.':>7}")
        print("-" * 83)

        for libro in libros:
            print(f"{libro[0]:<8}{libro[1][:35]:<36}{libro[2][:16]:<17}{libro[3][:14]:<15}{libro[4]:>7}")


def buscar_libro_en_archivo(codigo_buscado):
    """
    Busca un libro por código leyendo libros.txt línea por línea con readline().
    Devuelve la fila [codigo, titulo, categoria, autor, ejemplares] o [] si no existe.
    """
    libro = []
    archivo = None

    try:
        archivo = open("libros.txt", "r", encoding="UTF-8")

    except FileNotFoundError:
        print("No se encontró el archivo libros.txt.")

    except OSError as error:
        print(f"Error al abrir libros.txt: {error}")

    else:
        encontrado = False
        linea = archivo.readline()

        while linea != "" and not encontrado:
            campos = linea.strip().split(";")

            if int(campos[0]) == codigo_buscado:
                libro = [int(campos[0]), campos[1], campos[2], campos[3], int(campos[4])]
                encontrado = True
            else:
                linea = archivo.readline()

    finally:
        if archivo != None:
            archivo.close()

    return libro


def consultar_libro():
    """
    Opción 2: pide un código de libro, lo busca en libros.txt y muestra sus datos.
    Si el código no existe, lo informa.
    """
    codigo = validar_entero_positivo("Ingrese el codigo del libro: ")
    libro = buscar_libro_en_archivo(codigo)

    if len(libro) == 0:
        print(f"No existe un libro con el codigo {codigo}.")
    else:
        print(f"Codigo: {libro[0]}")
        mostrar_ficha_libro(libro)


def listado_cruzado(prestamos, libros):
    """
    Opción 6: muestra todos los préstamos cruzados con libros.txt por código.
    Por cada préstamo busca el libro para recuperar su título y autor.
    """
    if len(prestamos) == 0:
        print("No hay prestamos registrados.")
    else:
        print(f"{'NRO':<6}{'CODIGO':<8}{'LIBRO':<36}{'AUTOR':<15}{'DIAS':>5}")
        print("-" * 70)

        for prestamo in prestamos:
            posicion = buscar_libro(libros, prestamo[1])

            if posicion == -1:
                titulo = "(libro inexistente)"
                autor = "-"
            else:
                titulo = libros[posicion][1]
                autor = libros[posicion][3]

            print(f"{prestamo[0]:<6}{prestamo[1]:<8}{titulo[:35]:<36}{autor[:14]:<15}{prestamo[2]:>5}")


def obtener_prestamos_libro(prestamos, codigo):
    """
    Devuelve una matriz auxiliar con los préstamos de un libro (puede quedar vacía).
    Recibe la matriz de préstamos y el código del libro.
    """
    prestamos_libro = []

    for prestamo in prestamos:
        if prestamo[1] == codigo:
            prestamos_libro.append(prestamo)

    return prestamos_libro


def consultar_prestamos(libros, prestamos):
    """
    Opción 7: pide un código de libro, muestra su ficha y el detalle de sus préstamos,
    con la cantidad de operaciones y los días acumulados.
    Informa si el libro no existe o si no registra operaciones.
    """
    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        codigo = validar_entero_positivo("Ingrese el codigo del libro: ")
        posicion = buscar_libro(libros, codigo)

        if posicion == -1:
            print(f"No existe un libro con el codigo {codigo}.")
        else:
            print(f"Codigo consultado: {codigo}")
            mostrar_ficha_libro(libros[posicion])

            prestamos_libro = obtener_prestamos_libro(prestamos, codigo)

            if len(prestamos_libro) == 0:
                print("El libro no registra operaciones.")
            else:
                print(f"{'NRO. PRESTAMO':<20}{'DIAS':>6}")

                dias_acumulados = 0
                for prestamo in prestamos_libro:
                    print(f"{prestamo[0]:<20}{prestamo[2]:>6}")
                    dias_acumulados += prestamo[2]

                print(f"Operaciones: {len(prestamos_libro)} | Dias acumulados: {dias_acumulados}")

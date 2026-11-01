from abm_libros import buscar_libro
from validaciones import validar_entero_positivo


def contar_prestamos_libro(prestamos, codigo):
    """
    Devuelve cuántos préstamos tiene un libro (0 si no tiene ninguno).
    """
    cantidad = 0

    for prestamo in prestamos:
        if prestamo[1] == codigo:
            cantidad += 1

    return cantidad


def dias_acumulados_libro(prestamos, codigo):
    """
    Devuelve la suma de días de todos los préstamos de un libro (0 si no tiene).
    """
    dias = 0

    for prestamo in prestamos:
        if prestamo[1] == codigo:
            dias += prestamo[2]

    return dias


def total_prestamos(prestamos):
    """
    Estadística 1: devuelve la cantidad total de préstamos registrados.
    """
    return len(prestamos)


def prestamos_por_libro(libros, prestamos):
    """
    Estadística 2: devuelve una matriz [codigo, titulo, cantidad] con una fila por libro.
    Recorre libros (no préstamos) para que aparezcan también los que tienen 0.
    """
    cantidades = []

    for libro in libros:
        cantidad = contar_prestamos_libro(prestamos, libro[0])
        cantidades.append([libro[0], libro[1], cantidad])

    return cantidades


def libros_mas_prestados(libros, prestamos):
    """
    Estadística 3: devuelve una matriz [codigo, titulo, cantidad] con TODOS los libros
    empatados en la mayor cantidad de préstamos. Devuelve [] si no hay libros.
    """
    cantidades = prestamos_por_libro(libros, prestamos)
    mas_prestados = []

    if len(cantidades) > 0:
        maximo = cantidades[0][2]
        for fila in cantidades:
            if fila[2] > maximo:
                maximo = fila[2]

        for fila in cantidades:
            if fila[2] == maximo:
                mas_prestados.append(fila)

    return mas_prestados


def unir_codigos(filas):
    """
    Devuelve los códigos de una matriz como texto: "301", "301 y 302" o "301, 302 y 303".
    """
    texto = ""
    i = 0

    while i < len(filas):
        if i == 0:
            texto = f"{filas[i][0]}"
        elif i == len(filas) - 1:
            texto = texto + f" y {filas[i][0]}"
        else:
            texto = texto + f", {filas[i][0]}"
        i += 1

    return texto


def unir_prestamos_por_libro(cantidades):
    """
    Devuelve la cantidad de préstamos por libro como texto: "301 El Aleph: 2 | 302 Rayuela: 2".
    Recibe la matriz [codigo, titulo, cantidad] de prestamos_por_libro.
    """
    texto = ""
    i = 0

    while i < len(cantidades):
        if i > 0:
            texto = texto + " | "
        texto = texto + f"{cantidades[i][0]} {cantidades[i][1]}: {cantidades[i][2]}"
        i += 1

    return texto


def calcular_promedio(dias, cantidad):
    """
    Devuelve dias / cantidad. Si cantidad es 0, Python lanza ZeroDivisionError
    y lo atrapa quien llama a esta función.
    """
    return dias / cantidad


def promedio_dias_libro(libros, prestamos):
    """
    Estadística 4: pide un código de libro y muestra su promedio de días de préstamo.
    Si el libro tiene 0 préstamos, atrapa ZeroDivisionError e informa sin cortar el programa.
    """
    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        codigo = validar_entero_positivo("Ingrese el codigo del libro para calcular el promedio: ")
        posicion = buscar_libro(libros, codigo)

        if posicion == -1:
            print(f"No existe un libro con el codigo {codigo}.")
        else:
            dias = dias_acumulados_libro(prestamos, codigo)
            cantidad = contar_prestamos_libro(prestamos, codigo)

            try:
                promedio = calcular_promedio(dias, cantidad)
            except ZeroDivisionError:
                print(f"El libro {codigo} no registra prestamos: no se puede calcular el promedio (division por cero).")
            else:
                print(f"Promedio para {codigo}: {dias} / {cantidad} = {promedio:.2f} dias")


def mostrar_estadisticas(libros, prestamos):
    """
    Opción 8: muestra las 4 estadísticas. Cada cálculo vive en su propia función;
    esta solo se encarga de mostrarlos.
    """
    print("\n--- ESTADISTICAS ---")

    print(f"1) Cantidad total de prestamos: {total_prestamos(prestamos)}")

    cantidades = prestamos_por_libro(libros, prestamos)
    if len(cantidades) == 0:
        print("2) No hay libros registrados.")
    else:
        print(f"2) Prestamos por libro: {unir_prestamos_por_libro(cantidades)}")

    mas_prestados = libros_mas_prestados(libros, prestamos)
    if len(mas_prestados) == 0 or mas_prestados[0][2] == 0:
        print("3) No hay prestamos registrados para determinar el mas prestado.")
    elif len(mas_prestados) == 1:
        print(f"3) Mayor cantidad: {mas_prestados[0][0]} {mas_prestados[0][1]}, con {mas_prestados[0][2]}")
    else:
        print(f"3) Mayor cantidad: empate ({unir_codigos(mas_prestados)}), con {mas_prestados[0][2]}")

    print("4) Promedio de dias de prestamo de un libro:")
    promedio_dias_libro(libros, prestamos)

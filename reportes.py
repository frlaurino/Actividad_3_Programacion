from consultas import obtener_prestamos_libro
from estadisticas import dias_acumulados_libro, libros_mas_prestados, unir_codigos


def armar_bloque_libro(libro, prestamos):
    """
    Devuelve el texto del bloque de un libro para el reporte: datos, detalle de
    préstamos, cantidad de operaciones y días acumulados.
    """
    prestamos_libro = obtener_prestamos_libro(prestamos, libro[0])
    dias = dias_acumulados_libro(prestamos, libro[0])

    texto = f"LIBRO: {libro[0]} - {libro[1]}\n"
    texto = texto + f"CATEGORIA: {libro[2]} | AUTOR: {libro[3]} | EJEMPLARES: {libro[4]}\n"

    if len(prestamos_libro) == 0:
        texto = texto + "Sin prestamos registrados.\n"
    else:
        texto = texto + f"{'PRESTAMO':<11}{'DIAS':>4}\n"
        for prestamo in prestamos_libro:
            texto = texto + f"{prestamo[0]:<11}{prestamo[2]:>4}\n"

    texto = texto + f"OPERACIONES: {len(prestamos_libro)} | DIAS ACUMULADOS: {dias}\n\n"

    return texto


def texto_mas_prestados(libros, prestamos):
    """
    Devuelve el texto de la línea MAS PRESTADOS del resumen, contemplando empates.
    """
    mas_prestados = libros_mas_prestados(libros, prestamos)

    if len(mas_prestados) == 0 or mas_prestados[0][2] == 0:
        texto = "Sin prestamos registrados"
    elif len(mas_prestados) == 1:
        texto = f"{mas_prestados[0][0]} - {mas_prestados[0][1]} ({mas_prestados[0][2]} prestamos)"
    else:
        texto = f"{unir_codigos(mas_prestados)} ({mas_prestados[0][2]} cada uno)"

    return texto


def armar_resumen(libros, prestamos):
    """
    Devuelve el texto del bloque RESUMEN GENERAL del reporte.
    """
    separador = "=" * 63

    dias_totales = 0
    for prestamo in prestamos:
        dias_totales += prestamo[2]

    texto = f"{separador}\n"
    texto = texto + "RESUMEN GENERAL\n"
    texto = texto + f"{separador}\n"
    texto = texto + f"LIBROS: {len(libros)}\n"
    texto = texto + f"PRESTAMOS: {len(prestamos)}\n"
    texto = texto + f"DIAS ACUMULADOS: {dias_totales}\n"
    texto = texto + f"MAS PRESTADOS: {texto_mas_prestados(libros, prestamos)}\n"
    texto = texto + f"{separador}\n"

    return texto


def generar_reporte(libros, prestamos):
    """
    Opción 9: genera reporte_prestamos.txt sobrescribiendo la versión anterior.
    Escribe un bloque por cada libro (incluso sin préstamos) y el resumen general.
    """
    if len(libros) == 0:
        print("No hay libros registrados. No se generó el reporte.")
    else:
        archivo = None
        separador = "=" * 63

        try:
            archivo = open("reporte_prestamos.txt", "w", encoding="UTF-8")

        except OSError as error:
            print(f"Error al generar reporte_prestamos.txt: {error}")

        else:
            archivo.write(f"{separador}\n")
            archivo.write("INFORME CONSOLIDADO - LIBROS Y PRÉSTAMOS\n")
            archivo.write(f"{separador}\n")

            for libro in libros:
                archivo.write(armar_bloque_libro(libro, prestamos))

            archivo.write(armar_resumen(libros, prestamos))

            print("Reporte generado correctamente en reporte_prestamos.txt.")

        finally:
            if archivo != None:
                archivo.close()

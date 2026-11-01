from archivos import leer_libros, leer_prestamos
from abm_libros import alta_libro, modificar_libro, baja_libro
from consultas import listar_libros, consultar_libro, listado_cruzado, consultar_prestamos
from estadisticas import mostrar_estadisticas
from reportes import generar_reporte
from menu import pedir_opcion


def ejecutar_opcion(opcion):
    """
    Ejecuta la funcionalidad elegida. Los archivos se leen en cada opción
    para trabajar siempre con los datos actualizados.
    """
    if opcion == 1:
        listar_libros(leer_libros())
    elif opcion == 2:
        consultar_libro()
    elif opcion == 3:
        alta_libro()
    elif opcion == 4:
        modificar_libro()
    elif opcion == 5:
        baja_libro()
    elif opcion == 6:
        listado_cruzado(leer_prestamos(), leer_libros())
    elif opcion == 7:
        consultar_prestamos(leer_libros(), leer_prestamos())
    elif opcion == 8:
        mostrar_estadisticas(leer_libros(), leer_prestamos())
    elif opcion == 9:
        generar_reporte(leer_libros(), leer_prestamos())


def main():
    """
    Programa principal: repite el menú hasta que el usuario elija salir.
    """
    opcion = -1

    while opcion != 0:
        opcion = pedir_opcion()

        if opcion == 0:
            print("Fin del programa.")
        else:
            ejecutar_opcion(opcion)


main()

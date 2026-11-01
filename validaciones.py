
def validar_entero_positivo(mensaje):
    valido = False

    while not valido:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                raise ValueError("El número debe ser mayor que cero.")

            valido = True

        except ValueError as error:
            print(f"Error: {error}")

    return numero


def validar_entero_no_negativo(mensaje):
    valido = False

    while not valido:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                raise ValueError("El número no puede ser negativo.")

            valido = True

        except ValueError as error:
            print(f"Error: {error}")

    return numero


def validar_texto(mensaje):
    valido = False

    while not valido:
        texto = input(mensaje).strip()

        if texto == "" or ";" in texto:
            print("Error: el texto no puede estar vacío ni contener punto y coma.")
        else:
            valido = True

    return texto


def validar_confirmacion(mensaje):
    valido = False

    while not valido:
        respuesta = input(mensaje).strip().upper()

        if respuesta == "S" or respuesta == "N":
            valido = True
        else:
            print("Ingrese S para confirmar o N para cancelar.")

    return respuesta

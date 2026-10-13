
# funciones.py

# -----------------------------------------
# FUNCIONES DE VALIDACION E INGRESO DE DATOS
# -----------------------------------------

def ingresar_legajo():
    """Solicita un legajo y valida que sea un entero positivo."""

    legajo = input("Ingrese el legajo: ")
    valido = False

    while not valido:
        valido = True

        if len(legajo) == 0:
            valido = False
        else:
            for i in range(len(legajo)):
                if ord(legajo[i]) < 48 or ord(legajo[i]) > 57:
                    valido = False

        if valido and int(legajo) > 0:
            break

        print("Error. El legajo debe ser un entero positivo.")
        legajo = input("Ingrese el legajo: ")

    return int(legajo)

def ingresar_nombre():
    """Solicita apellido y nombre y valida que sean alfabeticos."""
    nombre = input("Ingrese apellido y nombre: ").strip()

    while nombre == "" or not nombre.replace(" ", "").isalpha():
        print("Error. Ingrese solamente letras y espacios.")
        nombre = input("Ingrese apellido y nombre: ").strip()

    return nombre

6
def ingresar_genero():
    """Solicita el genero y valida que sea F, M o X."""
    genero = input("Ingrese genero (F/M/X): ").upper()

    while genero != "F" and genero != "M" and genero != "X":
        print("Error. El genero debe ser F, M o X.")
        genero = input("Ingrese genero (F/M/X): ").upper()

    return genero


def ingresar_nota():
    """Solicita una nota entera entre 1 y 10."""
    nota = input("Ingrese la nota (1 a 10): ")

    while not nota.isdigit() or int(nota) < 1 or int(nota) > 10:
        print("Error. La nota debe ser un entero entre 1 y 10.")
        nota = input("Ingrese la nota (1 a 10): ")

    return int(nota)


# -----------------------------------------
# CARGA DE LAS LISTAS PARALELAS
# -----------------------------------------

def cargar_datos(legajos, nombres, generos, notas1, notas2):
    """Carga los datos de los 30 estudiantes."""

    for i in range(len(legajos)):
        print("\nESTUDIANTE", i + 1)

        legajos[i] = ingresar_legajo()
        nombres[i] = ingresar_nombre()
        generos[i] = ingresar_genero()

        print("Primer parcial")
        notas1[i] = ingresar_nota()

        print("Segundo parcial")
        notas2[i] = ingresar_nota()

    print("\nCarga finalizada correctamente.")


# -----------------------------------------
# FUNCIONES PARA MOSTRAR ESTUDIANTES
# -----------------------------------------

def mostrar_un_estudiante(legajos, nombres, generos,
                          notas1, notas2, promedios, i):
    """Muestra todos los datos de un estudiante."""

    print(
        legajos[i], "|",
        nombres[i], "|",
        generos[i], "|",
        notas1[i], "|",
        notas2[i],
        end=""
    )

    if len(promedios) == len(legajos):
        print("|", format(promedios[i], ".2f"))
    else:
        print()


def recorrer_estudiantes(legajos, nombres, generos,
                         notas1, notas2, promedios,
                         criterio="todos", valor=None):
    """Recorre las listas y muestra todos o algunos estudiantes."""

    print("\nINFORME DE ESTUDIANTES")
    print("-" * 85)

    if len(promedios) == len(legajos):
        print("LEGAJO | APELLIDO Y NOMBRE | GENERO | PARCIAL 1 | PARCIAL 2 | PROMEDIO")
    else:
        print("LEGAJO | APELLIDO Y NOMBRE | GENERO | PARCIAL 1 | PARCIAL 2")

    print("-" * 85)

    for i in range(len(legajos)):

        if criterio == "todos":
            mostrar_un_estudiante(
                legajos, nombres, generos,
                notas1, notas2, promedios, i
            )

        elif criterio == "legajo" and legajos[i] == valor:
            mostrar_un_estudiante(
                legajos, nombres, generos,
                notas1, notas2, promedios, i
            )

        elif criterio == "promedio" and promedios[i] == valor:
            mostrar_un_estudiante(
                legajos, nombres, generos,
                notas1, notas2, promedios, i
            )

    print("-" * 85)


# -----------------------------------------
# CALCULO DE PROMEDIOS
# -----------------------------------------

def calcular_promedio(nota1, nota2):
    """Calcula el promedio de dos notas y lo devuelve como real."""
    promedio = (nota1 + nota2) / 2
    return round(promedio, 2)


def calcular_promedios(notas1, notas2):
    """Crea y devuelve la lista de promedios de los estudiantes."""

    promedios = []

    for i in range(len(notas1)):
        promedio = calcular_promedio(notas1[i], notas2[i])
        promedios.append(promedio)

    return promedios


# -----------------------------------------
# ORDENAMIENTO DE LISTAS PARALELAS
# -----------------------------------------

def ordenar_estudiantes(legajos, nombres, generos,
                        notas1, notas2, promedios, orden):
    """Ordena todas las listas paralelas por promedio ASC o DESC."""

    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):

            intercambiar = False

            if orden == "ASC" and promedios[i] > promedios[j]:
                intercambiar = True

            elif orden == "DESC" and promedios[i] < promedios[j]:
                intercambiar = True

            if intercambiar:
                # Intercambia los promedios
                auxiliar = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = auxiliar

                # Intercambia los legajos
                auxiliar = legajos[i]
                legajos[i] = legajos[j]
                legajos[j] = auxiliar

                # Intercambia los nombres
                auxiliar = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = auxiliar

                # Intercambia los generos
                auxiliar = generos[i]
                generos[i] = generos[j]
                generos[j] = auxiliar

                # Intercambia las notas del primer parcial
                auxiliar = notas1[i]
                notas1[i] = notas1[j]
                notas1[j] = auxiliar

                # Intercambia las notas del segundo parcial
                auxiliar = notas2[i]
                notas2[i] = notas2[j]
                notas2[j] = auxiliar


# -----------------------------------------
# BUSQUEDA DEL MAYOR PROMEDIO
# -----------------------------------------

def mostrar_mayor_promedio(legajos, nombres, generos,
                           notas1, notas2, promedios):
    """Busca el promedio mayor y muestra a todos sus estudiantes."""

    mayor = promedios[0]

    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    print("\nMAYOR PROMEDIO:", format(mayor, ".2f"))

    recorrer_estudiantes(
        legajos, nombres, generos,
        notas1, notas2, promedios,
        "promedio", mayor
    )


# -----------------------------------------
# BUSQUEDA POR LEGAJO
# -----------------------------------------

def buscar_por_legajo(legajos, nombres, generos,
                      notas1, notas2, promedios):
    """Solicita un legajo y muestra el estudiante encontrado."""

    legajo_buscado = ingresar_legajo()
    encontrado = False

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            encontrado = True

    if encontrado:
        recorrer_estudiantes(
            legajos, nombres, generos,
            notas1, notas2, promedios,
            "legajo", legajo_buscado
        )
    else:
        print("No existe un estudiante con ese legajo.")


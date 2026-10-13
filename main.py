
# main.py

import funciones


def main():
    """Ejecuta el menu principal del sistema de estudiantes."""

    # Crear las listas paralelas para 30 estudiantes
    legajos = [0] * 30
    nombres = [""] * 30
    generos = [""] * 30
    notas1 = [0] * 30
    notas2 = [0] * 30

    # Lista de promedios inicialmente vacia
    promedios = []

    # Controla si se realizo la carga de datos
    cargado = False

    opcion = ""

    while opcion != "7":

        print("\n===== MENU DE ESTUDIANTES =====")
        print("1 - Cargar datos")
        print("2 - Mostrar todos los estudiantes")
        print("3 - Calcular promedios")
        print("4 - Mostrar estudiantes ordenados por promedio DESC")
        print("5 - Mostrar estudiante/s con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:

            case "1":
                funciones.cargar_datos(
                    legajos, nombres, generos,
                    notas1, notas2
                )

                cargado = True
                promedios = []

            case "2":
                if cargado:
                    funciones.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios
                    )
                else:
                    print("Primero debe cargar los datos.")

            case "3":
                if cargado:
                    promedios = funciones.calcular_promedios(
                        notas1, notas2
                    )

                    print("Promedios calculados correctamente.")

                    for i in range(len(promedios)):
                        print(
                            nombres[i],
                            "- Promedio:",
                            format(promedios[i], ".2f")
                        )
                else:
                    print("Primero debe cargar los datos.")

            case "4":
                if cargado:
                    if len(promedios) == 0:
                        promedios = funciones.calcular_promedios(
                            notas1, notas2
                        )

                    funciones.ordenar_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios, "DESC"
                    )

                    funciones.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios
                    )
                else:
                    print("Primero debe cargar los datos.")

            case "5":
                if cargado:
                    if len(promedios) == 0:
                        promedios = funciones.calcular_promedios(
                            notas1, notas2
                        )

                    funciones.mostrar_mayor_promedio(
                        legajos, nombres, generos,
                        notas1, notas2, promedios
                    )
                else:
                    print("Primero debe cargar los datos.")

            case "6":
                if cargado:
                    funciones.buscar_por_legajo(
                        legajos, nombres, generos,
                        notas1, notas2, promedios
                    )
                else:
                    print("Primero debe cargar los datos.")

            case "7":
                print("Fin del programa.")

            case _:
                print("Opcion incorrecta. Ingrese del 1 al 7.")


if __name__ == "__main__":
    main()


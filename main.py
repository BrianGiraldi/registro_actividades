# Programa principal - Evaluacion Final Integradora

from actividad import registrar_actividad, mostrar_actividades
import utilidades


def menu():
    actividades = utilidades.cargar_datos()
    sigue_ejecutando = True

    while sigue_ejecutando:
        print("\n==========================================")
        print("   REGISTRO SEMANAL DE ACTIVIDAD FISICA   ")
        print("==========================================")
        print("1. Registrar nueva actividad")
        print("2. Mostrar todas las actividades")
        print("3. Ver estadisticas (Promedio y Calorias)")
        print("4. Buscar actividades por fecha o tipo")
        print("5. Ver grafico de duracion (Matplotlib)")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opcion (1-6): ").strip()

        if opcion == "1":
            nombre = input("Nombre de la actividad (ej. Caminar, Ciclismo, Gimnasio): ").strip()
            while nombre == "":
                print("El nombre no puede estar vacio.")
                nombre = input("Nombre de la actividad: ").strip()

            fecha = input("Fecha de realizacion (DD/MM/AAAA): ").strip()
            while fecha == "":
                print("La fecha no puede estar vacia.")
                fecha = input("Fecha de realizacion (DD/MM/AAAA): ").strip()

            duracion = utilidades.pedir_duracion()
            calorias = utilidades.pedir_calorias()

            registrar_actividad(actividades, nombre, fecha, duracion, calorias)
            utilidades.guardar_datos(actividades)

        elif opcion == "2":
            mostrar_actividades(actividades)

        elif opcion == "3":
            if len(actividades) == 0:
                print("No hay actividades registradas para calcular estadisticas.")
            else:
                promedio = utilidades.calcular_promedio_duracion(actividades)
                total_cal = utilidades.calcular_total_calorias(actividades)
                print("\n--- Analisis de la Semana ---")
                print(f"Promedio de duracion semanal: {promedio:.2f} minutos")
                print(f"Total de calorias quemadas: {total_cal:.2f} kcal")

        elif opcion == "4":
            if len(actividades) == 0:
                print("No hay actividades cargadas para buscar.")
            else:
                print("\n1. Buscar por tipo de actividad")
                print("2. Buscar por fecha")
                sub = input("Elija una opcion (1 o 2): ").strip()

                if sub == "1":
                    valor = input("Ingrese el nombre de la actividad a buscar: ").strip()
                    encontradas = utilidades.buscar_actividades(actividades, "tipo", valor)
                elif sub == "2":
                    valor = input("Ingrese la fecha a buscar (DD/MM/AAAA): ").strip()
                    encontradas = utilidades.buscar_actividades(actividades, "fecha", valor)
                else:
                    print("Opcion no valida.")
                    continue

                if len(encontradas) > 0:
                    print(f"\nSe encontraron {len(encontradas)} coincidencias:")
                    for act in encontradas:
                        print(act)
                else:
                    print("No se encontraron actividades con ese filtro.")

        elif opcion == "5":
            utilidades.mostrar_grafico(actividades)

        elif opcion == "6":
            utilidades.guardar_datos(actividades)
            print("Saliendo del programa... ¡Hasta luego!")
            sigue_ejecutando = False

        else:
            print("Opcion incorrecta, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()

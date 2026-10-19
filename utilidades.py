# Modulo de utilidades: validaciones, archivo json, analisis y grafico

import json
import matplotlib.pyplot as plt
from actividad import Actividad

ARCHIVO = "actividades.json"


# Funciones de validacion con try / except
def pedir_duracion():
    while True:
        try:
            minutos = int(input("Ingrese la duracion en minutos: "))
            if minutos > 0:
                return minutos
            else:
                print("Error: La duracion tiene que ser un numero mayor a cero.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")


def pedir_calorias():
    while True:
        try:
            calorias = float(input("Ingrese las calorias quemadas estimadas: "))
            if calorias > 0:
                return calorias
            else:
                print("Error: Las calorias deben ser mayores a cero.")
        except ValueError:
            print("Error: Debe ingresar un numero valido (puede tener decimales con punto).")


# Funciones de analisis
def calcular_promedio_duracion(lista_actividades):
    if len(lista_actividades) == 0:
        return 0
    suma = 0
    for act in lista_actividades:
        suma += act.duracion
    promedio = suma / len(lista_actividades)
    return promedio


def calcular_total_calorias(lista_actividades):
    total = 0.0
    for act in lista_actividades:
        total += act.calorias
    return total


# Funcion de busqueda usando filter y lambda como pide la consigna
def buscar_actividades(lista_actividades, criterio, valor):
    if criterio == "tipo":
        resultados = list(filter(lambda act: act.nombre.lower() == valor.lower(), lista_actividades))
    elif criterio == "fecha":
        resultados = list(filter(lambda act: act.fecha == valor, lista_actividades))
    else:
        resultados = []
    return resultados


# Funciones de persistencia con JSON
def guardar_datos(lista_actividades):
    lista_dicts = []
    for act in lista_actividades:
        lista_dicts.append(act.a_diccionario())
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)
        print("Datos guardados en el archivo correctamente.")
    except Exception as e:
        print(f"Ocurrio un error al guardar el archivo: {e}")


def cargar_datos():
    lista_actividades = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for item in datos:
                nueva = Actividad(item["nombre"], item["fecha"], item["duracion"], item["calorias"])
                lista_actividades.append(nueva)
    except FileNotFoundError:
        print("No se encontro archivo de datos previo, se creara uno nuevo.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return lista_actividades


# Funcion de visualizacion con Matplotlib
def mostrar_grafico(lista_actividades):
    if len(lista_actividades) == 0:
        print("No hay datos cargados para armar el grafico.")
        return

    # Agrupamos la duracion por tipo de actividad usando un diccionario
    acumulado = {}
    for act in lista_actividades:
        nombre = act.nombre.capitalize()
        if nombre in acumulado:
            acumulado[nombre] += act.duracion
        else:
            acumulado[nombre] = act.duracion

    categorias = list(acumulado.keys())
    valores = list(acumulado.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, valores, color=["skyblue", "orange", "green", "salmon"])
    plt.title("Duracion total por tipo de actividad")
    plt.xlabel("Actividad")
    plt.ylabel("Duracion (minutos)")
    plt.grid(True)
    plt.savefig("grafico_actividades.png")
    print("Se guardo una copia del grafico como 'grafico_actividades.png'.")
    plt.show()

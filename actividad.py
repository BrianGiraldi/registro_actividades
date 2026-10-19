# Modulo de la clase Actividad

class Actividad:
    def __init__(self, nombre, fecha, duracion, calorias):
        self.nombre = nombre
        self.fecha = fecha
        self.duracion = duracion
        self.calorias = calorias

    def __str__(self):
        return f"Actividad: {self.nombre} | Fecha: {self.fecha} | Duracion: {self.duracion} min | Calorias: {self.calorias} kcal"

    def a_diccionario(self):
        # Metodo para pasar el objeto a diccionario y poder guardarlo en el json
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "duracion": self.duracion,
            "calorias": self.calorias
        }


def registrar_actividad(lista_actividades, nombre, fecha, duracion, calorias):
    nueva_act = Actividad(nombre, fecha, duracion, calorias)
    lista_actividades.append(nueva_act)
    print("Actividad registrada correctamente!")


def mostrar_actividades(lista_actividades):
    if len(lista_actividades) == 0:
        print("Todavia no hay actividades cargadas.")
    else:
        print("\n--- Listado de Actividades ---")
        for i in range(len(lista_actividades)):
            print(f"{i + 1}. {lista_actividades[i]}")

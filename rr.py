# Definición de la clase Proceso
class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad

    def ejecutar(self, quantum):
        if self.tiempo_ejecucion > quantum:
            print(f"Ejecutando {self.nombre} por {quantum} unidades de tiempo.")
            self.tiempo_ejecucion -= quantum
        else:
            print(f"Ejecutando {self.nombre} por {self.tiempo_ejecucion} unidades de tiempo.")
            self.tiempo_ejecucion = 0

# Función para cargar procesos desde el archivo "procesos.txt"
def cargar_procesos():
    procesos = []
    with open("procesos.txt", "r") as archivo:
        for linea in archivo:
            nombre, tiempo_ejecucion, prioridad = linea.strip().split(", ")
            proceso = Proceso(nombre, int(tiempo_ejecucion), int(prioridad))
            procesos.append(proceso)
    return procesos

# Función principal de planificación Round Robin
def round_robin(procesos, quantum):
    tiempo_total = sum(proceso.tiempo_ejecucion for proceso in procesos)
    tiempo_actual = 0

    while tiempo_total > 0:
        for proceso in procesos:
            if proceso.tiempo_ejecucion > 0:
                proceso.ejecutar(quantum)
                tiempo_total -= min(quantum, proceso.tiempo_ejecucion)
                tiempo_actual += min(quantum, proceso.tiempo_ejecucion)
                print(f"Tiempo total restante: {tiempo_total}\n")

# Cargar procesos desde el archivo
procesos = cargar_procesos()

# Configurar el quantum
quantum = 3

# Ejecutar el algoritmo Round Robin
round_robin(procesos, quantum)

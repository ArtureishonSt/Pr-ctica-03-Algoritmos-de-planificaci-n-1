# Definición de la clase Proceso
class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad

    def ejecutar(self, tiempo):
        if self.tiempo_ejecucion > tiempo:
            print(f"Ejecutando {self.nombre} por {tiempo} unidades de tiempo.")
            self.tiempo_ejecucion -= tiempo
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

    print("Ejecución Round Robin completada. Presione Enter para regresar al menú...")
    input()

# Función principal de planificación SJF (Shortest Job First)
def sjf(procesos):
    procesos.sort(key=lambda x: x.tiempo_ejecucion)  # Ordenar procesos por tiempo de ejecución
    tiempo_total = sum(proceso.tiempo_ejecucion for proceso in procesos)
    tiempo_actual = 0

    while tiempo_total > 0:
        for proceso in procesos:
            if proceso.tiempo_ejecucion > 0:
                proceso.ejecutar(proceso.tiempo_ejecucion)  # Ejecutar el proceso completo
                tiempo_total -= proceso.tiempo_ejecucion
                tiempo_actual += proceso.tiempo_ejecucion
                print(f"Tiempo total restante: {tiempo_total}\n")

    print("Ejecución SJF completada. Presione Enter para regresar al menú...")
    input()

# Función principal de planificación FIFO (First-In-First-Out)
def fifo(procesos):
    tiempo_total = sum(proceso.tiempo_ejecucion for proceso in procesos)
    tiempo_actual = 0

    while tiempo_total > 0:
        for proceso in procesos:
            if proceso.tiempo_ejecucion > 0:
                proceso.ejecutar(proceso.tiempo_ejecucion)  # Ejecutar el proceso completo
                tiempo_total -= proceso.tiempo_ejecucion
                tiempo_actual += proceso.tiempo_ejecucion
                print(f"Tiempo total restante: {tiempo_total}\n")

    print("Ejecución FIFO completada. Presione Enter para regresar al menú...")
    input()

# Función principal de planificación por prioridades
def prioridades(procesos):
    procesos.sort(key=lambda x: x.prioridad)  # Ordenar procesos por prioridad
    tiempo_total = sum(proceso.tiempo_ejecucion for proceso in procesos)
    tiempo_actual = 0

    while tiempo_total > 0:
        for proceso in procesos:
            if proceso.tiempo_ejecucion > 0:
                proceso.ejecutar(proceso.tiempo_ejecucion)  # Ejecutar el proceso completo
                tiempo_total -= proceso.tiempo_ejecucion
                tiempo_actual += proceso.tiempo_ejecucion
                print(f"Tiempo total restante: {tiempo_total}\n")

    print("Ejecución de Prioridades completada. Presione Enter para regresar al menú...")
    input()

# Función para implementar el menú de selección (modificada)
def menu():
    while True:
        print("Menú de selección:")
        print("1. Round Robin")
        print("2. SJF")
        print("3. FIFO")
        print("4. Prioridades")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            quantum = 3  # Quantum predeterminado para Round Robin
            print("\nEjecutando Round Robin...\n")
            round_robin(procesos, quantum)
        elif opcion == "2":
            print("\nEjecutando SJF (Shortest Job First)...\n")
            sjf(procesos)
        elif opcion == "3":
            print("\nEjecutando FIFO (First-In-First-Out)...\n")
            fifo(procesos)


        elif opcion == "4":
            print("\nEjecutando Prioridades...\n")
            prioridades(procesos)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Seleccione una opción entre 1 al 5.")

if __name__ == "__main__":
    # Cargar procesos desde el archivo
    procesos = cargar_procesos()

    # Ejecutar el menú
    menu()

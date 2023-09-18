import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import threading

# Función para cargar los procesos desde el archivo 'procesos.txt'
def cargar_procesos():
    procesos = []
    try:
        with open('procesos.txt', 'r') as file:
            for line in file:
                nombre, tiempo_ejecucion, prioridad = line.strip().split(', ')
                procesos.append((nombre, int(tiempo_ejecucion), int(prioridad)))
    except FileNotFoundError:
        print("El archivo 'procesos.txt' no se encuentra en la raíz.")
    return procesos

# Algoritmo Round Robin
def round_robin(procesos, quantum):
    ejecucion = []
    cola = procesos.copy()
    tiempo = 0

    while cola:
        proceso = cola.pop(0)
        nombre, tiempo_ejecucion, prioridad = proceso
        ejecucion.append((nombre, min(quantum, tiempo_ejecucion)))

        if tiempo_ejecucion > quantum:
            time.sleep(quantum)
            tiempo += quantum
            cola.append((nombre, tiempo_ejecucion - quantum))
        else:
            time.sleep(tiempo_ejecucion)
            tiempo += tiempo_ejecucion

    return ejecucion

# Algoritmo SJF (Shortest Job First)
def sjf(procesos):
    ejecucion = []
    procesos.sort(key=lambda x: x[1])  # Ordenar por tiempo de ejecución
    tiempo = 0

    for proceso in procesos:
        nombre, tiempo_ejecucion, prioridad = proceso
        ejecucion.append((nombre, tiempo_ejecucion))
        time.sleep(tiempo_ejecucion)
        tiempo += tiempo_ejecucion

    return ejecucion

# Algoritmo FIFO (First-In, First-Out)
def fifo(procesos):
    ejecucion = []
    tiempo = 0

    for proceso in procesos:
        nombre, tiempo_ejecucion, prioridad = proceso
        ejecucion.append((nombre, tiempo_ejecucion))
        time.sleep(tiempo_ejecucion)
        tiempo += tiempo_ejecucion

    return ejecucion

# Algoritmo de Prioridades
def prioridades(procesos):
    ejecucion = []
    procesos.sort(key=lambda x: x[2])  # Ordenar por prioridad (menor número es mayor prioridad)
    tiempo = 0

    for proceso in procesos:
        nombre, tiempo_ejecucion, prioridad = proceso
        ejecucion.append((nombre, tiempo_ejecucion))
        time.sleep(tiempo_ejecucion)
        tiempo += tiempo_ejecucion

    return ejecucion

# Función para mostrar la simulación gráfica
def mostrar_simulacion(algoritmo, quantum=None):
    procesos = cargar_procesos()
    if not procesos:
        return

    if algoritmo == "Round Robin":
        if quantum is None or quantum <= 0:
            return
        ejecucion = round_robin(procesos, quantum)
    elif algoritmo == "SJF":
        ejecucion = sjf(procesos)
    elif algoritmo == "FIFO":
        ejecucion = fifo(procesos)
    elif algoritmo == "Prioridades":
        ejecucion = prioridades(procesos)
    else:
        return

    # Crear y mostrar la representación gráfica
    fig, ax = plt.subplots(figsize=(8, 4))
    tiempo = 0
    for proceso in ejecucion:
        nombre, tiempo_ejecucion = proceso
        ax.barh(nombre, tiempo_ejecucion, left=tiempo)
        tiempo += tiempo_ejecucion
    ax.set_xlabel('Tiempo de Ejecución')
    ax.set_ylabel('Proceso')
    ax.set_title(f'Simulación de {algoritmo}')
    plt.tight_layout()

    root = tk.Tk()
    root.title('Simulación de Planificación de Procesos')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    root.mainloop()

# Función para limpiar la ventana
def clear():
    plt.close('all')

# Interfaz gráfica
root = tk.Tk()
root.title('Planificación de Procesos')

algoritmo_label = ttk.Label(root, text="Selecciona el algoritmo:")
algoritmo_label.pack()

algoritmo_combo = ttk.Combobox(root, values=["Round Robin", "SJF", "FIFO", "Prioridades"])
algoritmo_combo.pack()

quantum_label = ttk.Label(root, text="Quantum (para Round Robin):")
quantum_label.pack()

quantum_entry = ttk.Entry(root)
quantum_entry.pack()

simular_button = ttk.Button(root, text="Simular", command=lambda: mostrar_simulacion(algoritmo_combo.get(), int(quantum_entry.get()) if algoritmo_combo.get() == "Round Robin" else None))
simular_button.pack()

clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.pack()

root.mainloop()

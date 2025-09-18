import os
import time
import sys
import matplotlib.pyplot as plt
import numpy as np

ENCABEZADO = "T_i,B_i"

def merge_sort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    medio = len(arreglo)//2
    izq = merge_sort(arreglo[:medio])
    der = merge_sort(arreglo[medio:])
    return merge(izq, der)

def merge(izq, der):
    i = j = 0
    res = []
    while i < len(izq) and j < len(der):
        tiempo_izq, peso_izq = izq[i]
        tiempo_der, peso_der = der[j]
        if tiempo_izq/peso_izq <= tiempo_der/peso_der:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            j += 1
    
    while i < len(izq):
        res.append(izq[i])
        i += 1
    
    while j < len(der):
        res.append(der[j])
        j += 1

    return res

def organizar_batallas(batallas):
    tiempo_fin_actual = 0
    suma_ponderada = 0
    batallas_ord = merge_sort(batallas)
    for batalla in batallas_ord:
        tiempo, peso = batalla
        tiempo_fin_actual += tiempo
        suma_ponderada += peso * tiempo_fin_actual
    return batallas_ord, suma_ponderada

def procesar_archivo_batallas(ruta_archivo):
    batallas = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea == ENCABEZADO:
                    continue
                ti, bi = map(int, linea.split(","))
                batallas.append((ti, bi))
    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe.")
        return None
    except ValueError:
        print("Error: el archivo no tiene el formato esperado. Ejemplo: (<ti>,<bi>).")
        return None
    return batallas

def main_mediciones():
    """
    Ejecuta el análisis de complejidad empírica.
    """
    ruta_carpeta = "sets"
    archivos_txt = [f for f in os.listdir(ruta_carpeta) if f.endswith('.txt')]
    
    tamanios_n = []
    tiempos_promedio = []

    for f in archivos_txt:
        nombre_sin_extension = os.path.splitext(f)[0]
        
        # Este es el cambio clave que evita el error
        if nombre_sin_extension.isdigit():
            n = int(nombre_sin_extension)
            tamanios_n.append(n)
            
            archivo_path = os.path.join(ruta_carpeta, f)
            tiempos_ejecucion = []
            num_pruebas = 5

            for _ in range(num_pruebas):
                batallas = procesar_archivo_batallas(archivo_path)
                if batallas is None: continue
                
                inicio_tiempo = time.time()
                organizar_batallas(batallas)
                fin_tiempo = time.time()
                tiempos_ejecucion.append(fin_tiempo - inicio_tiempo)
                
            if tiempos_ejecucion:
                tiempo_promedio = sum(tiempos_ejecucion) / len(tiempos_ejecucion)
                tiempos_promedio.append(tiempo_promedio)
            else:
                tiempos_promedio.append(0)

    tamanios_n, tiempos_promedio = zip(*sorted(zip(tamanios_n, tiempos_promedio)))
    
    n_array = np.array(tamanios_n)
    tiempos_array = np.array(tiempos_promedio)
    
    indices_validos = n_array > 1
    if np.any(indices_validos):
        n_validos = n_array[indices_validos]
        tiempos_validos = tiempos_array[indices_validos]
        C = tiempos_validos[-1] / (n_validos[-1] * np.log(n_validos[-1]))
    else:
        C = 0

    plt.figure(figsize=(10, 6))
    plt.scatter(n_array, tiempos_array, label='Mediciones Empíricas', color='red')
    x_teorica = np.linspace(n_array.min(), n_array.max(), 100)
    y_teorica = C * x_teorica * np.log(x_teorica)
    plt.plot(x_teorica, y_teorica, label=f'Complejidad Teórica O(n log n) con C={C:.2e}', linestyle='--', color='blue')
    plt.title('Análisis de Tiempos de Ejecución')
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "mediciones":
        main_mediciones()
    elif len(sys.argv) != 2:
        print("Uso: python3 archivo_pruebas_alex.py <archivo_entrada.txt> | python3 archivo_pruebas_alex.py mediciones")
        return 1
    else:
        archivo_entrada = sys.argv[1]
        batallas = procesar_archivo_batallas(archivo_entrada)
        if not batallas:
            print("No se encontraron batallas válidas.")
            return 1
        orden, suma = organizar_batallas(batallas)
        print("Orden de batallas:", orden)
        print("Suma ponderada:", suma)
    return 0

if __name__ == "__main__":
    sys.exit(main())

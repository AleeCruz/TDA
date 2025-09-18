# Importaciones necesarias
import os
import time
import sys
import matplotlib.pyplot as plt
import numpy as np

# A continuación, incluye todas tus funciones
# procesar_archivo_batallas, merge_sort, merge, organizar_batallas

# Batallas es un array de (ti, bi)
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
    ENCABEZADO = "T_i,B_i"
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

# Funciones de merge_sort y merge (sin cambios)
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

def main_mediciones():
    """
    Ejecuta el análisis de complejidad empírica.
    """
    ruta_carpeta = "sets"
    
    # 1. Recopilar datos de los archivos en la carpeta 'sets'
    archivos_txt = [f for f in os.listdir(ruta_carpeta) if f.endswith('.txt')]
    tamanios_n = sorted([int(f.split('.')[0]) for f in archivos_txt])
    tiempos_promedio = []

    for n in tamanios_n:
        archivo_path = os.path.join(ruta_carpeta, f"{n}.txt")
        tiempos_ejecucion = []
        num_pruebas = 5  # Múltiples mediciones para un promedio confiable

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

    # 2. Preparar los datos para el ajuste O(n log n)
    # Convertimos a arrays de numpy para facilidad de cálculo
    n_array = np.array(tamanios_n)
    tiempos_array = np.array(tiempos_promedio)
    
    # Preparamos los datos para la regresión lineal
    # x_regresion = n_array * np.log(n_array)
    # coeficientes = np.polyfit(x_regresion, tiempos_array, 1)
    # constante_C = coeficientes[0]
    
    # Opcionalmente, para un ajuste más directo, podemos usar una técnica de escalado simple
    # para encontrar una constante C que ajuste bien la curva teórica.
    # Evitamos log(0)
    indices_validos = n_array > 1
    if np.any(indices_validos):
        n_validos = n_array[indices_validos]
        tiempos_validos = tiempos_array[indices_validos]
        # Calcular la constante C a partir del último punto
        C = tiempos_validos[-1] / (n_validos[-1] * np.log(n_validos[-1]))
    else:
        C = 0

    # 3. Generar el gráfico
    plt.figure(figsize=(10, 6))
    
    # Graficar los puntos de las mediciones empíricas
    plt.scatter(n_array, tiempos_array, label='Mediciones Empíricas', color='red')
    
    # Graficar la curva teórica O(n log n)
    x_teorica = np.linspace(n_array.min(), n_array.max(), 100)
    y_teorica = C * x_teorica * np.log(x_teorica)
    
    plt.plot(x_teorica, y_teorica, label=f'Complejidad Teórica O(n log n) con C={C:.2e}', linestyle='--', color='blue')

    plt.title('Análisis de Tiempos de Ejecución')
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mediciones":
        main_mediciones()
    else:
        sys.exit(main())

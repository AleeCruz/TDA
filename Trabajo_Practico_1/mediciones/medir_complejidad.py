from random import seed
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from util import time_algorithm
import sys, os

DIR_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_RAIZ)
from tp1 import organizar_batallas

RANDOM_SEED = 12345
RANDOM_MIN = 1
RANDOM_MAX = 1000
TAMANIO_MIN = 100
TAMANIO_MAX = 500_000
CANTIDAD_PUNTOS = 20

SALIDA_GRAFICOS = "mediciones/graficos/"

seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
sns.set_theme()

# Funciones para ajustar
f_nlogn = lambda x, c1, c2: c1 * x * np.log(x) + c2 
f_n2 = lambda x, c1, c2: c1 * x**2 + c2

def generar_batallas(n):
    return [(np.random.randint(RANDOM_MIN, RANDOM_MAX), np.random.randint(RANDOM_MIN, RANDOM_MAX)) for _ in range(n)]

def generar_graficos(x, results, c_nlogn, c_n2, r_nlogn, r_n2):
    # Gráfico funciones ajustadas
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], '--',label="Medición")
    ax.plot(x, f_nlogn(x, *c_nlogn), 'g',label="Ajuste $n log(n)$")
    ax.plot(x, f_n2(x, *c_n2), 'r', label="Ajuste $n^2$")
    ax.set_title('Ajuste de funciones')
    ax.set_xlabel('Tamaño de entrada')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    fig.savefig(SALIDA_GRAFICOS + "complejidad_funciones.png")

    # Gráfico error de ajuste
    fig, ax = plt.subplots()
    ax.plot(x, r_nlogn, 'g',label="Ajuste $n log(n)$")
    ax.plot(x, r_n2, 'r',label="Ajuste $n^2$")
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño de entrada')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()
    fig.savefig(SALIDA_GRAFICOS + "complejidad_error.png")

if __name__ == "__main__":
    x = np.linspace(TAMANIO_MIN, TAMANIO_MAX, CANTIDAD_PUNTOS).astype(int)

    results = time_algorithm(organizar_batallas, x, lambda s: [generar_batallas(s)])

    c_nlogn, _ = sp.optimize.curve_fit(f_nlogn, x, [results[n] for n in x])
    c_n2, _ = sp.optimize.curve_fit(f_n2, x, [results[n] for n in x])

    r_nlogn = [np.abs(c_nlogn[0] * n * np.log(n) + c_nlogn[1] - results[n]) for n in x]
    r_n2 = [np.abs(c_n2[0] * n**2 + c_n2[1] - results[n]) for n in x]

    print("Ajuste O(n log n): c1 =", c_nlogn[0], ", c2 =", c_nlogn[1])
    print("Ajuste O(n²): c1 =", c_n2[0], ", c2 =", c_n2[1])

    if np.mean(r_nlogn) < np.mean(r_n2):
        print("Mejor función que ajusta: O(n * log n)")
    else:
        print("Mejor función que ajusta: O(n²)")

    generar_graficos(x, results, c_nlogn, c_n2, r_nlogn, r_n2)

import os
import random

def generar_datos_prueba(n, ruta_carpeta):
    """
    Genera un archivo de datos con n batallas aleatorias.
    """
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    nombre_archivo = f"{n}.txt"
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

    with open(ruta_completa, 'w') as archivo:
        archivo.write("T_i,B_i\n")  # Encabezado
        for _ in range(n):
            # Genera valores aleatorios para T_i y B_i
            # Puedes ajustar los rangos si lo necesitas
            ti = random.randint(1, 1000)
            bi = random.randint(1, 1000)
            archivo.write(f"{ti},{bi}\n")
    print(f"Archivo generado: {ruta_completa}")

def main_generador():
    """
    Genera un conjunto de archivos para las pruebas de complejidad.
    """
    # Define los tamaños de entrada (n) que quieres probar.
    # Puedes añadir más valores si quieres un gráfico con más puntos.
    tamanios_n = [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
    ruta_destino = "sets"
    
    for n in tamanios_n:
        generar_datos_prueba(n, ruta_destino)
    
    print("Todos los archivos de prueba han sido generados.")

if __name__ == "__main__":
    main_generador()

import os
import random

def generar_datos_prueba(n, ruta_carpeta, nombre_archivo):
    """
    Genera un archivo de datos con n batallas aleatorias y un nombre específico.
    """
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

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

def main():
    # Especifica aquí el nombre del archivo y la cantidad de datos
    nombre_archivo = "5000000.txt"
    cantidad_datos = 500000
    ruta_destino = "sets"
    
    generar_datos_prueba(cantidad_datos, ruta_destino, nombre_archivo)

if __name__ == "__main__":
    main()

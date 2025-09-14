import sys

# Batallas es un array de (ti, bi) 
def organizar_batallas(batallas):
    felicidad_actual = 0
    suma_ponderada = 0

    batallas_ord = sorted(batallas, key=lambda x: x[0]/x[1])

    for batalla in batallas_ord:
        felicidad_actual += batalla[0]
        suma_ponderada += batalla[1] * felicidad_actual

    return batallas_ord, suma_ponderada

def procesar_archivo_batallas(ruta_archivo):
    batallas = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                ti, bi = map(int, linea.split())
                batallas.append((ti, bi))
    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe.")
        return None
    except ValueError:
        print("Error: el archivo no tiene el formato esperado. Ejemplo: (<ti> <bi>).")
        return None
    return batallas

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp1.py <archivo_entrada.txt>")
        return 1

    archivo_entrada = sys.argv[1]
    batallas = procesar_archivo_batallas(archivo_entrada)

    if not batallas:
        return 1
    
    orden, suma = organizar_batallas(batallas)

    print("Orden de batallas:", orden)
    print("Suma ponderada:", suma)
    return 0

if __name__ == "__main__":
    sys.exit(main())

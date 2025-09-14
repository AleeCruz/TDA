import sys

ENCABEZADO = "T_i,B_i"

def merge_sort(arreglo): 
    if len(arreglo)<=1:
        return arreglo

    medio = len(arreglo)//2

    izq = merge_sort(arreglo[:medio])
    der = merge_sort(arreglo[medio:])

    return merge(izq, der)

def merge(izq, der):
    i=j=0
    res= []

    while i < len(izq) and j < len(der):
        tiempo_izq, peso_izq = izq[i]
        tiempo_der, peso_der = der[j]
        if tiempo_izq/peso_izq <= tiempo_der/peso_der:
            res.append(izq[i])
            i+=1
        else:
            res.append(der[j])
            j+=1
    
    while i < len(izq):
        res.append(izq[i])
        i+=1
        
    while j < len(der):
        res.append(der[j])
        j+=1

    return res

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

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp1.py <archivo_entrada.txt>")
        return 1

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

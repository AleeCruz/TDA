import sys

def organizar_batallas(batallas):
    suma_ponderada = 0
    tiempo_fin_actual = 0

    # Ordenar por t_i / b_i en forma ascendente
    batallas_ordenadas = sorted(batallas, key=lambda x: x[0] / x[1])

    for tiempo, peso in batallas_ordenadas:
        tiempo_fin_actual += tiempo
        suma_ponderada += peso * tiempo_fin_actual

    return batallas_ordenadas, suma_ponderada


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 tp1.py ruta/al/archivo.txt")
        sys.exit(1)

    ruta = sys.argv[1]
    batallas = []
    with open(ruta, "r") as f:
        next(f)  # saltar encabezado "T_i,B_i"
        for linea in f:
            if linea.strip():  # evitar líneas vacías
                t, b = map(int, linea.strip().split(","))
                batallas.append((t, b))

    ordenadas, suma = organizar_batallas(batallas)

    print("Orden óptimo de batallas (t, b):")
    for t, b in ordenadas:
        print(f"{t} {b}")

    print("\nSuma ponderada mínima:", suma)


if __name__ == "__main__":
    main()


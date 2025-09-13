# Batallas es un array de (ti, bi) 
def organizar_batallas(batallas):
    felicidad_actual = 0
    suma_ponderada = 0

    batallas_ord = sorted(batallas, key=lambda x: x[0]/x[1])

    for batalla in batallas_ord:
        felicidad_actual += batalla[0]
        suma_ponderada += batalla[1] * felicidad_actual

    return batallas_ord, suma_ponderada
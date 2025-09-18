from tp1 import organizar_batallas

def prueba_1():
    batallas = []

    orden_esperado = []
    suma_esperada = 0

    orden, suma = organizar_batallas(batallas)

    assert orden == orden_esperado, f"\nOrden obtenido:{orden} \nOrden esperado: {orden_esperado}"
    assert suma == suma_esperada, f"\nSuma obtenida:{suma} \nSuma esperada: {suma_esperada}"

def prueba_2():
    batallas = [(3, 4)]

    orden_esperado = [(3, 4)]
    suma_esperada = 12

    orden, suma = organizar_batallas(batallas)

    assert orden == orden_esperado, f"\nOrden obtenido:{orden} \nOrden esperado: {orden_esperado}"
    assert suma == suma_esperada, f"\nSuma obtenida:{suma} \nSuma esperada: {suma_esperada}"

def prueba_3():
    batallas = [
        (3, 4),
        (2, 2),
        (1, 6),
    ]

    orden_esperado = [
        (1, 6),
        (3, 4),
        (2, 2),
    ]
    suma_esperada = 34

    orden, suma = organizar_batallas(batallas)

    assert orden == orden_esperado, f"\nOrden obtenido:{orden} \nOrden esperado: {orden_esperado}"
    assert suma == suma_esperada, f"\nSuma obtenida:{suma} \nSuma esperada: {suma_esperada}"

def prueba_4():
    batallas = [
        (2, 3),
        (2, 2),
        (2, 1),
    ]

    orden_esperado = [
        (2, 3),
        (2, 2),
        (2, 1),
    ]
    suma_esperada = 20

    orden, suma = organizar_batallas(batallas)

    assert orden == orden_esperado, f"\nOrden obtenido:{orden} \nOrden esperado: {orden_esperado}"
    assert suma == suma_esperada, f"\nSuma obtenida:{suma} \nSuma esperada: {suma_esperada}"    

if __name__ == "__main__":
    prueba_1()
    prueba_2()
    prueba_3()
    prueba_4()
    print("Todas las pruebas pasaron")
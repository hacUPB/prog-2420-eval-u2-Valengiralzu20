
def main():
        #Simulación desintegración orbital de un satélite 

    import math #Para poder utilizar operaciones matemáticas 

    def simulacion_desintegracion(altitud_satelite_inicial, cd_inicial, altitud_satelite_minima):

        altitud_satelite_actual = altitud_satelite_inicial
        cd = cd_inicial
        orbitas = 0

        print("\nA continuación se puede evidenciar una simulación de la desintegración orbital de un satélite:")

        while altitud_satelite_actual > altitud_satelite_minima:
            # Calcula la pérdida de altitud
            altitud_perdida = cd * altitud_satelite_actual

            # Actualiza la altitud
            altitud_satelite_actual=altitud_satelite_actual-altitud_perdida 

            # Aumenta el coeficiente de arrastre (simplificación)
            cd = cd + 0.0001

            # Incrementa el contador de órbitas
            orbitas = orbitas + 1

            print(f"Órbita {orbitas}: Altitud actual = {altitud_satelite_actual} km, Coeficiente de arrastre = {cd}")

        print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")

    # Obtener datos del usuario
    altitud_satelite_inicial = float(input("\nIngrese la altitud inicial del satélite (en kilómetros): "))
    cd_inicial = float(input("\nIngrese el coeficiente de arrastre inicial: "))
    altitud_minima = float(input("\nIngrese la altitud mínima segura (en kilómetros): "))

    # Iniciar la simulación
    simulacion_desintegracion(altitud_satelite_inicial, cd_inicial, altitud_minima)


if __name__ == "__main__":
    main()


def main():
        #Simulación desintegración orbital de un satélite 

    import math #Para poder utilizar operaciones matemáticas 

    def simulacion_desintegracion(altitud_inicial, coeficiente_arrastre_inicial, altitud_minima):

        altitud_actual = altitud_inicial
        coeficiente_arrastre = coeficiente_arrastre_inicial
        orbitas = 0

        print("\nA continuación se puede evidenciar una simulación de la desintegración orbital de un satélite:")

        while altitud_actual > altitud_minima:
            # Calcula la pérdida de altitud
            perdida_altitud = coeficiente_arrastre * altitud_actual

            # Actualiza la altitud
            altitud_actual=altitud_actual-perdida_altitud

            # Aumenta el coeficiente de arrastre (simplificación)
            coeficiente_arrastre = coeficiente_arrastre +0.0001

            # Incrementa el contador de órbitas
            orbitas = orbitas + 1

            print(f"Órbita {orbitas}: Altitud actual = {altitud_actual:.2f} km, Coeficiente de arrastre = {coeficiente_arrastre:.4f}")

        print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")

    # Obtener datos del usuario
    altitud_inicial = float(input("\nIngrese la altitud inicial del satélite (en kilómetros): "))
    coeficiente_arrastre_inicial = float(input("\nIngrese el coeficiente de arrastre inicial: "))
    altitud_minima = float(input("\nIngrese la altitud mínima segura (en kilómetros): "))

    # Iniciar la simulación
    simulacion_desintegracion(altitud_inicial, coeficiente_arrastre_inicial, altitud_minima)


if __name__ == "__main__":
    main()

#Simulación desintegración orbital de un satélite 

def main():
    
    #Se definió la función y los parámetro que se utilizarán 
    def simulacion_desintegracion(altitud_satelite_inicial, cd_inicial, altitud_satelite_minima):

        #Tareas que debe ejecutar 
        altitud_satelite_actual = altitud_satelite_inicial
        cd = cd_inicial
        orbitas = 0

        print("\nA continuación se puede evidenciar una simulación de la desintegración orbital de un satélite:")
        
        #Se utiliza un bucle para que solo se ejecute si cumple la condición 
        while altitud_satelite_actual > altitud_satelite_minima:
            # Operaciones que se realizan si la condición del bucle es verdadera 

            altitud_perdida = cd * altitud_satelite_actual #Calculo de perdida por altitud

            altitud_satelite_actual=altitud_satelite_actual-altitud_perdida #Para obtener altitud actual

            cd = cd + 0.0001 #Para aumentar el cd 

            orbitas = orbitas + 1 #Se utiliza un contador para incrementar el # de orbitas 

            print(f"Órbita {orbitas}: Altitud actual = {altitud_satelite_actual} km, Coeficiente de arrastre = {cd}")

        print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")

    # Datos que debe ingresar el usuario
    altitud_satelite_inicial = float(input("\nIngrese la altitud inicial del satélite (en kilómetros): "))
    cd_inicial = float(input("\nIngrese el coeficiente de arrastre inicial: "))
    altitud_minima = float(input("\nIngrese la altitud mínima segura (en kilómetros): "))

    simulacion_desintegracion(altitud_satelite_inicial, cd_inicial, altitud_minima)

if __name__ == "__main__":
    main()

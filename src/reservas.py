def main():
    
    import random

    # Distancias entre ciudades (en km)
    ciudades={}
    distancias = {
        (0, 1): 240,
        (0, 2): 461,
        (1, 2): 657,
        (1, 0): 240,
        (2, 0): 461,
        (2, 1): 657
    }


    #para calcular el precio del tiquete según el día de la semana

    def calcular_precio(origen, destino, dia_semana):

        distancia = distancias[(origen, destino)]
        
        if distancia < 400:
            if dia_semana in ["1", "2", "3", "4"]:
                precio = 79900
            else:
                precio = 119900
        else:
            if dia_semana in ["1", "2", "3", "4"]:
                precio = 156900
            else:
                precio = 213000
        return precio

    #para asinar asiento elegido por el usuario 
    def asignar_asiento(preferencia):
        if preferencia == "1.":
            return "C"
        elif preferencia == "2.":
            return "A"
        else:
            return "B"

    #funcion para reservar vuelo
    def reservar_vuelo():
        continuar=True
        while continuar:
            titulo = input("\nIngrese su título (Sr o Sra):").capitalize()
            nombre = input("Ingrese su nombre: ").capitalize()
            apellido = input("Ingrese su apellido: ").capitalize()

            print(f"\n{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")

            print("\nOpciones ciudad de origen:\n1.Medellín\n2.Bogotá\n3.Cartagena")
            origen = int(input("\nSeleccione su ciudad de origen: "))-1

            print("\nOpciones ciudad de destino:\n1.Medellín\n2.Bogotá\n3.Cartagena")
            destino = int(input("\nSeleccione su ciudad de destino: "))-1
            ciudades=["Medellín","Bogotá","Cartagena"]
            origen_ciudad=ciudades [origen]
            destino_ciudad=ciudades[destino]

            print ("\nOpciones día de la semana para viajar:\n1.Lunes\n2.Martes\n3.Miercóles\n4.Jueves\n5.Viernes\n6.Sábado\n7.Domingo")
            dia_semana_str = input ("\nIngrese el día de la semana que desea viajar:")
            dia_semana = int(dia_semana_str)
            dias_semana=["Lunes", "Martes", "Miercóles", "Jueves", "Viernes", "Sábado", "Domingo"]
            dia_semana_texto=dias_semana[dia_semana-1]

            dia_mes = int(input("\nIngrese el día del mes (1-30): "))
        
            print("\nOpciones mes del año:\n1.Enero\n2.Febrero\n3.Marzo\n4.Abril\n5.Mayo\n6.Junio\n7.Julio\n8.Agosto\n9.Septiembre\n10.Octubre\n11.Noviembre\n12.Diciembre")
            mes_año = int (input ("\nIngrese el mes del año que desea viajar:"))
        
            año=input("\nIngrese el año que desea viajar:")
        
            precio = calcular_precio(origen, destino, dia_semana) 

            print("\nOpciones de asiento:\n1.Pasillo\n2.Ventana\n3.No tiene preferencia")
            preferencia = input("\nSeleccione el asiento que desea:")
            fila = random.randint(1, 29)
            columna = asignar_asiento(preferencia)
            asiento= f"{columna}{fila}"

            fecha= f"{dia_mes}/{mes_año}/{año}"
            
            

            print(f"\nResumen de su reserva:")
            print(f"Nombre: {titulo} {nombre} {apellido}")
            print(f"Origen: {origen_ciudad}")
            print(f"Destino: {destino_ciudad}")
            print(f"Fecha de vuelo: {fecha}")
            print(f"Precio: ${precio}")
            print(f"Asiento asignado: {asiento}")

            print("\n¿Quiere realizar otra reserva?\n1.Sí\n2.No")
            otra_reserva=input ("\nIngrese su selección:")
            continuar=otra_reserva=="1" 
    
    reservar_vuelo() 

if __name__ == "__main__":
    main()
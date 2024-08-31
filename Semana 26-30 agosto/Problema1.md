# Avance 27 y 29 de agosto

## Análisis del problema 

### Constantes:
- Ciudades: Medellín, Bogotá, Cartagena (son fijas y no cambian durante la ejecución del programa).
- Distancias entre ciudades: Estos valores son fijos y se utilizan para calcular los precios.
- Precios base: Los precios para vuelos cortos y largos, así como los precios para días de semana y fines de semana, son constantes.
- Tipos de asientos: Pasillo, ventana, sin preferencia.

### Variables:
- Nombre del usuario: Cambia según el usuario.
- Origen y destino: Seleccionados por el usuario.
- Fecha de vuelo: Día de la semana y día del mes, ingresados por el usuario.
- Precio del vuelo: Calculado según la distancia y el día de la semana.
- Número de asiento: Asignado aleatoriamente.

### Para construir diagrama de bloques
1.	Inicio: Comienza el programa.
2.	Ingreso de datos del usuario: Solicita nombre, apellido y título.
3.	Selección de vuelos:
- Mostrar opciones de ciudades.
- Solicitar origen y destino.
- Solicitar fecha de vuelo.
4.	Cálculo del precio:
- Determinar la distancia entre ciudades.
- Calcular el precio basado en la distancia y el día de la semana.
5.	Asignación de asiento:
-Solicitar preferencia de asiento.
- Asignar un asiento aleatorio según la preferencia.
6.	Mostrar información de la reserva:
- Mostrar nombre del pasajero, origen, destino, fecha, precio y asiento asignado.
7.	Fin: Terminar el programa.

### Diagrama de bloques 
[Diagrama de bloques](https://miro.com/app/board/uXjVKkvjbIo=/?share_link_id=984604946339)

### Pseudocódigo

Inicio

  // Pedir al usuario que ingrese datos 

  Ingresar título (Sr, Sra), nombre, apellido 

  Mostrar saludo personalizado

  // Definir ciudades y distancias

  Definir ciudades = ["Medellín", "Bogotá", "Cartagena"] 

  Definir distancias = [[0, 240, 461], [240, 0, 657], [461, 657, 0]] 

  Definir precios_bajo = 79900  

  Definir precios_alto = 119900

  Definir precios_bajo_largo = 156900 

  Definir precios_alto_largo = 213000

  // Pedir usuario ingrese origen y destino 

  Ingresar origen 

  Ingresar destino
  
  // Pedir usuario ingrese fecha 

  Ingresar día_semana 

  Ingresar día_mes

  // Calcular precio 

  Si distancia(origen)(destino) < 400 entonces 

     Si día_semana es "lunes" O "martes" O "miércoles" O "jueves" entonces

            precio = precios_bajo 

     Si no 

            precio = precios_alto 

     Fin si

  Si no

     Si día_semana es "lunes" O "martes" O "miércoles" O "jueves" entonces 

         precio = precios_bajo_largo 

     Si no

         precio = precios_alto_largo 

     Fin si

  Fin si

   // Asignar silla

   Ingresar preferencia_silla 

   Generar número_silla aleatorio entre 1 y 29

   Si preferencia_silla es "pasillo" entonces 

      silla = número_silla + "C" 

  Si no si preferencia_silla es "ventana" entonces

      silla = número_silla + "A" 

  Si no

      silla = número_silla + "B"

  Fin si

   // Mostrar confirmación

   Mostrar nombre, origen, destino, fecha, precio, asiento

 Fin 
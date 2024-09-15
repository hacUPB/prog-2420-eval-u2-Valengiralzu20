# Avance 27 y 29 de agosto

## Variables y Constantes
### Variables:
- Altitud: Cambia a medida que el satélite pierde altura debido al arrastre.
- Coeficiente de arrastre: Aumenta a medida que el satélite se acerca a la Tierra.
- Número de órbitas: Cuenta el número de veces que el satélite ha orbitado la Tierra.

### Constantes:
- Altitud mínima de seguridad: Valor fijo que determina el punto en el que se considera que el satélite se ha desintegrado.
- Incremento del coeficiente de arrastre: Valor fijo que determina la rapidez con la que aumenta el coeficiente de arrastre.

### Para construir diagrama de bloques

1.	Inicio: Comienza el programa.
2.	Ingreso de datos: Solicita al usuario la altitud inicial, coeficiente de arrastre inicial y altitud mínima de seguridad.
3.	Inicialización: Inicializa las variables: altitud actual, número de órbitas, etc.
4.	Bucle principal:
- Cálculo de la pérdida de altitud: Calcula la pérdida de altitud basada en la altitud actual y el coeficiente de arrastre.
- Actualización de la altitud: Resta la pérdida de altitud a la altitud actual.
- Incremento del coeficiente de arrastre: Aumenta ligeramente el coeficiente de arrastre.
- Verificación de condiciones de parada: Si la altitud es menor que la altitud mínima de seguridad o si la pérdida de altitud es muy pequeña, se detiene el bucle.
- Incrementar el número de órbitas: Suma uno al contador de órbitas.
5.	Salida: Imprime el resultado final (si el satélite se desintegró o se estabilizó).
6.	Fin: Termina el programa.

### Diagrama de bloques 
[Diagrama de bloques](https://miro.com/app/board/uXjVKku5Pm4=/?share_link_id=746825607701)

### Pseudocódigo
Inicio

  // Pedir al usuario ingresar datos

  Ingresar altitud_inicial

  Ingresar coeficiente_arrastre_inicial 

  Ingresar  altitud_minima_seguridad 

  // Iniciar variables

  altitud_actual <=altitud_inicial

  coeficiente_arrastre <= coeficiente_arrastre_inicial 

  num_orbitas <=0

  // Definir bucle 

  Mientras altitud_actual > altitud_minima_seguridad calcular

    perdida_altitud = coeficiente_arrastre * altitud_actual

    altitud_actual = altitud_actual - perdida_altitud 

    coeficiente_arrastre += coeficiente_arrastre + 0.0001

    num_orbitas = num_orbitas + 1 

  Fin mientras

  // Mostrar resultado 

  Si altitud_actual <= altitud_minima_seguridad entonces
  
     Escribir "El satélite ha reingresado en la atmósfera." 

  Si no

     Escribir "El satélite se ha estabilizado en una órbita baja." 

  Fin si

  Escribir "Número de órbitas completadas:", num_orbitas 
  
Fin


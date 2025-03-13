# Inicialización de variables
reporte_participantes = "Listado de Participantes\n"  # Cadena para almacenar la lista de participantes
reporte_edades = "Listado de Edades\n"  # Cadena para almacenar las edades de los participantes
suma_edades = 0  # Acumulador para calcular el promedio de edades
contador = 0  # Contador para numeración de participantes
bandera = True  # Variable de control para el ciclo while

# Uso de listas para almacenar datos de los participantes
lista_nombres = []  # Lista para almacenar los nombres de los participantes
lista_lenguajes = []  # Lista para almacenar los lenguajes favoritos de los participantes
lista_edades = []  # Lista para almacenar solo las edades de los participantes
lista_nivel_experiencia = []  # Lista para almacenar el nivel de experiencia de cada participante

# Bucle para ingreso de datos
while bandera:
    print("\nIngrese la información del participante:")
    nombres = input("Nombres del participante: ")  # Se solicita el nombre del participante
    lenguaje = input("Lenguaje de programación favorito: ")  # Se solicita el lenguaje favorito
    edad = input("Edad del participante: ")  # Se solicita la edad del participante
    edad = int(edad)  # Conversión de la edad a entero
    nivel = input("Nivel de experiencia (Principiante, Intermedio, Avanzado): ")  # Se solicita el nivel de experiencia

    # Uso de listas para almacenar la información de cada participante
    contador = contador + 1  # Se incrementa el contador para numerar a los participantes
    lista_nombres.append(nombres)  # Se almacena la información de los nombres en una lista
    lista_edades.append(edad)  # Se almacena la edad en la lista de edades
    lista_lenguajes.append(lenguaje)  # Se almacena el lenguaje en la lista de lenguajes (corregido)
    lista_nivel_experiencia.append(nivel)  # Se almacena el nivel de experiencia en la lista correspondiente

    # Preguntar al usuario si desea continuar ingresando participantes
    continuar = input("¿Desea ingresar otro participante? (si/no): ")
    if continuar.lower() != "si":  # Si la respuesta no es "si", se termina el ciclo
        bandera = False

# Construcción del reporte de participantes a partir de las listas
for i in range(len(lista_nombres)):
    reporte_participantes = f"{reporte_participantes}{i+1}. {lista_nombres[i]} -{lista_lenguajes[i]}-, edad {lista_edades[i]}, nivel {lista_nivel_experiencia[i]}\n"

# Suma de edades
suma_edades = sum(lista_edades)
for i in lista_edades:
    reporte_edades = f"{reporte_edades}{i}\n"

# Cálculo de promedios de edad
if contador > 0:
    promedio_edades = suma_edades / contador  # Se calcula el promedio de edades
else:
    promedio_edades = 0

# Impresión del reporte final
print(reporte_participantes)  # Se imprime el listado de participantes
print(reporte_edades)  # Se imprime el listado de edades
print(f"Promedio de edades: {promedio_edades:.1f}")  # Se imprime el promedio de edades

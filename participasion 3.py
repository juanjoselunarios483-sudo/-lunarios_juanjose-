#pide nombres hasta que el usuario escriba la palabra "fin".al final muestra cuantos nombres ingreso y cual es el primero y el ultimo
# Programa que pide nombres hasta que el usuario escriba "Fin"
nombres = []

while True:
    nombre = input("Escribe un nombre (o 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)

# Mostrar resultados
if len(nombres) > 0:
    print(f"\nIngresaste {len(nombres)} nombres.")
    print(f"El primer nombre fue: {nombres[0]}")
    print(f"El último nombre fue: {nombres[-1]}")
else:
    print("\No ingresaste ningún nombre.")



# pide una frase y pide cuantas vocales usa (a, e, i, o ,u)
frase=input("ingresa una frase")
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in frase:
    if letra in vocales:
        contador_vocales += 1
        print(f"la frase tiene {contador_vocales}vocales")
        print("-------------------------")

# has un programa que pida un numero y crea una nueva lista sin duplicados
numero = int(input("ingresa un numero para crear una lista sin duplicados"))
lista_numeros = [] 
for i in range(numero):
    numero_lista = int(input( "ingresa el numero {i + 1}:"))
    if numero_lista not in lista_numeros:
        lista_numeros.append(numero_lista)
        print("la lista sin duplicados es:", lista_numeros)
        print("-------------------------")

#Haz un programa que pida "Nombre" y "Calificaciones". Posteriormente calcula el promedio general, calificación mayor, calificación menor y muestra el nombre del mejor alumno
alumnos = {}
while True:
    nombre = input("Escribe el nombre del alumno (o 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        calificacion = float(input(f"Escribe la calificación de {nombre}: "))
        alumnos[nombre] = calificacion
    except ValueError:
        print("Por favor, escribe una calificación válida.")

# Procesar resultados
if alumnos:
    calificaciones = list(alumnos.values())
    promedio = sum(calificaciones) / len(calificaciones)
    mayor = max(calificaciones)
    menor = min(calificaciones)

    # Encontrar el nombre del mejor alumno
    for nombre, calificacion in alumnos.items():
        if calificacion == mayor:
            mejor_alumno = nombre
            break

    # Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Calificación más alta: {mayor}")
    print(f"Calificación más baja: {menor}")
    print(f"Mejor alumno: {mejor_alumno}")

else:
    print("No se ingresaron datos.")



#pide numeroshasta que el usuario escriba 0 guarda los pares en una lista y los inpares en otra al final muestar cuantos numeros hay en cada lista. ordena la lista de forma asendente y recorre la listaspara mostrar cada numero uno por uno





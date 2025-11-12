# haz un programa que pida dos numeros y muestre su suma, resta, multiplicacion y divicion
#inputmath = "calculadora basica"
num1 = input("ingresa el primer numero")
num2 = input("ingresa el segundo numero")
suma =(f"{num1} + {num2}")
resta = (f"{num1} - {num2}")
multiplicacion = (f" {num1} * {num2}")
division = (f" {num1} / {num2}")
print("el resultado es:")
print(suma)
print(resta)
print(multiplicacion)
print(division)
# print("el resultado de la suma es:" + suma)
# print("el resultado de la resta es: + resta ")


# sintaxis condicionales

# if condicion:
#   intrucciones si la condicion es verdadera
# elif otra condicion:
#   instruciones si la otra condicion es verdadera
# else:
#   intrucciones si ninguna condicion es verdadera

# programa que pida un numero y muestr si es positivo negativo o cer

numero = float(input("ingrese un numero:"))
if numero >0:
    print("bloque if ejecutado")
    print("el numero es positivo")
elif numero < 0:
    print("bloque elif ejecutado")
    print("el numro es negativo")
else:
    print("bloque else ejecutado")
    print("el numero es cero")

print("-------------------------")

# ejercicio 2 : programa que pida dos numeros y muestre cual es el mayor o si son iguales

num1 = float(input("ingresa el primer numero:"))
num2 = float(input("ingresa el segundo numero"))

if num1 > num2: 
    print("el primer numero es mayor")
elif num1 < num2: # num2 > num1
    print("el segundo numero es mayor")
else:
    print("ambos numeros son iguales")    

print("-------------------------")

# ejercicio 3: haz un programa que pida una calificacion del 0 al 10 y muestre si esta aprobado o reprobado. toma en cuenta una calificacion mayor o igual a 6 como aprovatoria

nombreAlumno = input("ingresa el nombre del alumno:")
calificacion = float(input("ingresa la calificacion del alumno (0-10):"))
if calificacion >= 6:
    print(F"el alumno {nombreAlumno} esta aprobado")
else:
    print(F"el alumno {nombreAlumno}esta reprobado")
    
    print("-------------------------")

# haz un programa que pida la edad de una persona y muestre si pude votar (mayor o igual a 18 años) o no

nombre = input("ingresa el nombre de la persona:")
edadPersona = int(input("ingrese su edad"))

if edadPersona >=18:
    print(F"{nombre} tiene {edadPersona} años y puede votar")
else:
    print(F"{nombre}tiene {edadPersona} años y no puede votar")
    

# for variable in iterable:
#   bloque de codigo


# funcion range(inicio, fin, paso)
for i in range(0, 11, 2):
    print(i)

# ejercicio 1 Haz un programa que muestre los numeros del 1 al 20
print("numeros del 1 al 20")
for numero in range(1, 21):
    print(numero)

# ejercicio 2 haz un programa que muestre la tabla de multiplicar de un numero dad por el usuario (del 1 al 10)

numero_usuario = int(input("introduce un numero"))
print(f"tabla de mutiplicar del {numero_usuario}")
for i in range(1, 11,):
    resultado = numero_usuario * i
    print(("{numero_usuario} x {i} = {resultado}"))

# ejercicio 3 haz un programa en python que pida un numero y muestre cuantos numeros pares hay desde 1 hasta ese numero (incluyendolo si es par) 

conteo_pares =0
#solicitar al usuario


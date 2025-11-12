#Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando. Imprime en consola un coteo de números pares y de números impares
ingresa_numro = int(input("ingresa un numero)"))
contador_pares = 0
contador_impares = 0
for numero in range("1, ingresa un numero + 1"):
    if numero % 2== 0:
        contador_pares += 1
    print("numero par:")
else:
    contador_impares += 1
    print("numero impar:")
    print(f"desde 1 hasta {ingresa_numero} hay {contador_pares} numeros pares")
    print(f"desde 1 hasta {ingresa_numero} hay {contador_impares} numeros impares")
    print("-------------------------")
 #Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma.
suma_pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        suma_pares += numero
        print(f"la suma de todos los numeros pares del 1 al 100 es: {suma_pares}")
        print("-------------------------")

#Haz un programa en Python que pida al usuario ingresar un número, y muestre su tabla de multiplicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc).
numero_usuario = int(imput("ingresa un numero"))
print(f"tabla de multiplicar del {numero_usuario}para los multiplos pares ")
for i in range(2, 21, 2):
    resultado = numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado} ")
    print("-------------------------")

#Haz un programa que genera la tabla de multiplicar de un número ingresado. Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50, cuántos menores que 50 y cuántos iguales a 50.
numero_usuario = int(input("ingresa un numero"))
contador_mayores = 0
contador_menores = 0
contador_iguales = 0
print(f"tabla de multiplar del {numero_usuario}")
for i in range(1, 21):
    resultado = numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado}")
    if resultado > 50:
        contador_mayores += 1
    elif resultado < 50:
        contador_menores += 1
    else:
        contador_iguales += 1
        print(f"resultados mayores que 50: {contador_mayores}")
        print(f"resultados menores que 50: {contador_menores}")
        print(f"resultados iguales a 50: {contador_iguales}")
        print("-------------------------")

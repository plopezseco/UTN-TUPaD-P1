# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = str(input("Ingrese un número: "))

if numero[0] == "-":
    numero = numero[1:]

print(len(numero))

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
suma = 0

for i in range(num1, num2 + 1):
    suma += i

print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese un número y se sumará. Para salir ingrese 0 "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número y se sumará. Para salir ingrese 0 "))

print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_random = random.randint(0, 9)
numero_usuario = int(input("Adivine el número de 0 a 9 "))
intentos = 1

while numero_random != numero_usuario:
    intentos += 1
    numero_usuario = int(input("Incorrecto, intente de nuevo "))

print("Has adivinado el número en el intento N°",intentos)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo "))
suma = 0

if numero <= 0:
    numero = int(input("Número negativo, por favor ingrese un número entero positivo "))

for i in range(numero):
    suma += i

print(f"La suma de todos los numeros comprendidos entre 0 y {numero} es {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input("Ingrese un número "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"""Positivos: {positivos}
Negativos: {negativos}
Pares: {pares}
Impares: {impares}
""")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0

for i in range(100):
    numero = int(input("Ingrese un número "))
    suma += numero

promedio = suma / 100

print(f"El promedio es {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = str(input("Ingrese un número "))

if numero[0] == "-":
    inverso = '-' + numero[:0:-1]
else: 
    inverso = numero[::-1]

print(inverso)




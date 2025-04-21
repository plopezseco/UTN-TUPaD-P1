# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#funcion
def imprimir_hola_mundo(mensaje):
    return print(mensaje)

#programa principal
imprimir_hola_mundo("Hola Mundo!")


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#funcion
def saludar_usuario(mensaje):
    return f"Hola {mensaje}!"

#programa principal
nombre = input("Ingrese su nombre ")
print(saludar_usuario(nombre))


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#funcion
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#programa principal
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
residencia = input("Lugar de residencia ")

informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#funciones
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#programa principal
radio = float(input("Ingrese el radio "))

print(f"El área es {calcular_area_circulo(radio)}")
print(f"El perímetro es {calcular_perimetro_circulo(radio)}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#funcion
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese una cantidad de segundos para pasar a horas "))
print(f"{segundos} son {segundos_a_horas(segundos):.2f} horas") #Redondeo el resultado a dos decimales


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#funcion
def tabla_multiplicar(numero):
    n = 1
    while n <= 10:
        print(numero * n)
        n += 1
    return 

#programa principal
numero = int(input("Ingrese un número para visualizar su tabla de multiplicar "))
tabla_multiplicar(numero)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#funcion
def operaciones_basicas(a, b):
    tupla = (a+b, a-b, a*b, a/b)
    return print(f"""
Suma: {tupla[0]}
Resta: {tupla[1]}
Multiplicación: {tupla[2]}
División: {tupla[3]:.2f}
      """)

#programa principal
num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))

operaciones_basicas(num1, num2)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#funcion
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return print(f"Tu IMC es {round(imc, 1)}")

#programa principal
peso = int(input("Ingrese su peso "))
altura = float(input("Ingrese su altura en formato metros "))

calcular_imc(peso, altura)


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#funcion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")

#programa principal
celsius = int(input("Ingrese los grados en Celsius "))
celsius_a_fahrenheit(celsius)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))
num3 = int(input("Ingrese otro número "))

print(f"El promedio de los tres números ingresados es {calcular_promedio(num1, num2, num3):.2f}")


# Nombre: Guale Neira César David
# Fecha: 11-Septiembre-2026 16:49pm
# Instrucciones: Resuelve los siguientes problemas creando funciones para cada uno. Usa type hints y las bibliotecas necesarias.
"""
    Ejercicio 1: Función de Saludo Personalizado
    Crea una función saludo_personalizado(nombre: str) que imprima un saludo.
    Llama a la función dos veces con nombres diferentes.
"""
print(" - - - - - - - - - - -")
print("Ejercicio 1: Función de Saludo Personalizado")
#Definimos la funcion
def saludo_perso(nombre:str):
    print(f"Hola {nombre}, resoolviste el primer ejercicio :) ") 

#Ingresamos el primer nombre
nombre: str = input("Ingrese el primer nombre: ")
#Llamamos a la funcion por primera vez
saludo_perso(nombre)
#Ingresamos otro nombre
nombre2: str = input("Ingrese el segundo nombre: ")
#Llamamos a la funcion por segunda vez
saludo_perso(nombre2)

"""
    Ejercicio 2: Calculadora de Área de Círculo
    Importa la biblioteca math.
    Crea una función llamada calcular_area_circulo que acepte un parámetro radio (float).
    Dentro de la función, usa math.pi y la fórmula del área (π * r²) para calcular el área.
    La función debe retornar el área calculada.
    Llama a la función, guarda el resultado en una variable e imprímelo.
"""
print("\n - - - - - - - - - - -")
print("Ejercicio 2: Calculadora de Área de Círculo")
import math #Biblioteca para usar el valor de pi

def calcular_area_circulo(radio: float):
    area: float = math.pi * (radio ** 2)
    return area
#Llmamos a la funcion e ingresamos los datos
radio: float = float(input("Ingrese el radio del círculo: "))
area_circulo: float = calcular_area_circulo(radio)
print(f"El area del círculo es: {area_circulo}") #Imprimimos el resultado del area del circulo

"""
    Ejercicio 3: Refactorizando el Verificador de Calificaciones
    Crea una función obtener_feedback_calificacion(calificacion: float) que retorne un texto ("Sobresaliente", "Notable", etc.) basado en la nota.
    Llama a la función e imprime el feedback retornado.
"""
print("\n - - - - - - - - - - -")
print("Ejercicio 3: Refactorizando el Verificador de Calificaciones")
#Definimos la funcion para obtener el feedback de la calificacion y su retorno (comentario)
def obtener_feedback_calificacion(calificacion: float):
    if calificacion >=9:
        return "Sobresaliente"
    if calificacion >=7:
        return "Notable"
    if calificacion >=5:
        return "Aprobado"
    return "Reprobado pa, toca repetir de nuevo"

#Creamos las variables y llamamos a la funcion para obtener el feedback
calificacion: float = float(input("Digite su calificacion: ")) 
feedback: str = obtener_feedback_calificacion(calificacion)
print(f"Su calificación es: {calificacion} y su feedback es: {feedback}")

"""
    Ejercicio 4: Función para Encontrar Números Pares
    Crea una función encontrar_pares(lista_numeros: list[int]) que retorne una nueva lista solo con los números pares de la original.
    Llama a la función e imprime la nueva lista.
"""
print("\n - - - - - - - - - - -")
print("Ejercicio 4: Función para Encontrar Números Pares")
#Primero definimos la funcion
def encontrar_pares(lista_numeros: list[int]):
    #Definimos la lista de pares
    lista_pares: list[int] = [] #Creamos la lista vacia para almacenar los numeros pares
    #Recorremos la lista de numeros y verificamos si son pares
    for numero in lista_numeros:
        if numero % 2 == 0: #Si es divisible y su resultado es 0, entonces es par
            lista_pares.append(numero) #Se agrega el número par a la lista de pares.
    return lista_pares

#Creamos la lista de números y claro llamamos a la funcion
lista_numeros = [1,4,32,17,50,70,96,21,15,100]
lista_pares: list[int] = encontrar_pares(lista_numeros)
#Imprimimos en pantalla la lista de pares
print(f"La lista de números pares son: {lista_pares}")

"""
    Ejercicio 5: Calculadora de Estadísticas con NumPy
    1.- Importa la biblioteca numpy con el alias np.
    2.- Crea una función calcular_estadisticas_np que acepte una lista de números.
    3.- Dentro de la función, convierte la lista a un arreglo de NumPy: arreglo = np.array(lista_numeros).
    4.- La función debe retornar un diccionario con las siguientes estadísticas, calculadas con funciones de NumPy:
        + "media": np.mean(arreglo)
        + "mediana": np.median(arreglo)
        + "desviacion_estandar": np.std(arreglo)
    5.- Llama a la función e imprime el diccionario resultante.
"""
#Importamos la librería y lo nombramos como alias np
import numpy as np
#Creamos la funcion
def calcular_estadisticas_np(lista_numeros: list[float]):
    arreglo = np.array(lista_numeros)
    estadisticas = {
        "media": np.mean(arreglo),
        "mediana": np.median(arreglo),
        "desviacion_estandar": np.std(arreglo)  # Corregida la 's'
    }
    return estadisticas

#Imprimimos en pantalla el resultado de la funcion
print("\n - - - - - - - - - - -")
print("Ejercicio 5: Calculadora de Estadísticas con NumPy")

datos = [10.5, 20.0, 15.2, 35.8, 12.0]
resultado = calcular_estadisticas_np(datos)
print(resultado)
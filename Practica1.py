# ===============================
# PRACTICA DE PYTHON: VARIABLES Y TIPE HINTS
# ===============================
# Ejercicio 1: Informacion Personal
# Enunciado: Crear variables para almacenar nombre completo
# edad, estatura (decimal un float) y una variable booleana
# para comida favorita e imprimir con mensajes descriptivos
# ---------------------------------------------
nombre: str = "David Guale"
edad: int = 21
estatura: float = 1.70
le_gusta_manzana: bool = True

print(f"Su nombre es: {nombre}")
print(f"Su edad es: {edad}")
print(f"Su estatura es: {estatura} metros")
print(f"¿Le gusta la manzana? {le_gusta_manzana}")

# Ejercicio 2: Calculadora de Área de un Rectángulo
# Enunciado: Crear variables 'base' y 'altura'. Calcular el área
# con la formula: (base * altura) y almacenar el 'area'. Imprimir
# de forma clara
# ---------------------------------------------
base: float = 7.0
altura: float = 3.0
area: float = base * altura
print(" - - - - - - - - - - -")
print(f"El area de la figura es: {area}")

# Ejercicio 3: Conversor de Moneda Simple
# Enunciado: Crear variable 'dolares' y 'tasa_conversion_eur'
# Calcular el equivalente en euros e imprimir ambos valores
# ---------------------------------------------
dolar: float = 15
euro: float = 0.92
euros: float = dolar * euro
print(" - - - - - - - - - - -")
print(f"El equivalete de dolares a euros es: {euros}")
print(" - - - - - - - - - - -")
print(f"Dolares: {dolar}")
print(f"Cantidad convertida {euros}")
print(" - - - - - - - - - - -")

# Ejercicio 4: División y Resto
# Enunciado: Declarar 'total_estudiantes' (28) y 'tamanio_grupo' (5)
# Calcular grupos completos (división entera) y estudiantes sobrantes (módulo)
TEstudiantes: int = int(input("Ingrese el numero de estudiantes: "))
Tamgrupos: int = int(input("Digite el numero de grupos: "))
grupos:int = TEstudiantes // Tamgrupos
sobrantes:int = TEstudiantes % Tamgrupos

if sobrantes>0: 
    grupos = grupos+1

print(" - - - - - - - - - - -")
print(f"El numero de grupos completos es: {grupos}")
print(f"El numero de estudiantes sobrantes es: {sobrantes}")

# Ejercicio 5: Calculadora IMC
# Enunciado: Crear variables para peso (kg) y altura (m).
# Calcular el IMC usando la fórmula: peso / (altura ** 2) y almacenar en 'imc'.
peso: float = float(input("Ingrese el peso en kg: "))
altura: float = float(input("Digite su altura en metros: "))
imc: float = peso / (altura ** 2)
print(f"El IMC es: {imc}")

""""
# Otra solucion es crear una funcion que retorne los valores
def resultado(peso:float, altura:float):
    return (peso)/(altura**2)

# Mostramos los valores
print(resultado(peso, altura))
"""
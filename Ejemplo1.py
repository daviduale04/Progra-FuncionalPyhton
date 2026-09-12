#Dada una lista de calificaciones, obtener otra lista con las notas aprobadas
#ajustadas con un punto extra. 10-9-2026 13:50pm

notas = [5,8,9,6,10]

aprobadas = []

for notas in notas:
    if notas>=7:
        aprobadas.append(notas+1)

print(aprobadas)

#Tipos de datos en Python y el cambio de Java
#String en Java String nombre = "Juan"
nombre = "Juan"
print(type(nombre)) #str
#Int en Java int edad = 20
edad = 20
print(type(edad)) #int
#Float en Java float estatura = 1.75
estatura = 1.75
print(type(estatura)) #float
#Boolean en Java boolean esMayor = true
legustaElFutbol: bool = False
print(type(legustaElFutbol)) #bool

if legustaElFutbol:
    print("Es mayor de edad")
    print("Su nombre es: "+nombre)#Imprime esto si esta dentro del for
    #Importa el espacio de identacion, si no esta dentro del for no se imprime

print("Su nombre es: "+nombre)

##Ejercicio clasico base por altura
base: float = 5.0
altura: float = 3.0
area: float = base * altura
#pasamos de numero a string para poder concatenar con el str(area)
print("El área del rectángulo es: "+str(area))


#Otra solucion del ejercicio 1
notas = [5,8,9,6,10]
aprobadas = list(
    map(lambda nota: nota + 1, 
        filter(lambda nota: nota >= 7, notas))
)
print(aprobadas)


#Solucion del docente
def sumar1(nota: int)-> int:
    return nota + 1

r = map(sumar1,filter(lambda nota: nota >= 7, notas))
print(list(r))

#forma funcional
notas = [5,8,9,6,10]
aprobadas = list (
    map(lambda nota: nota + 1,
         filter(lambda nota : nota >=7, notas))
)

print (aprobadas)

#forma no funcional: 
notas = [5,8,9,6,10]
aprobadas = []
for nota in notas :
    if nota >= 7 :
        aprobadas.append(nota+1)

print(aprobadas)
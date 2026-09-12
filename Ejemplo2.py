#Ingreso de datos
#En java declaravamos Scanner en Python es un input

#numero = int(input("Ingrese un numero: "))

#print("El numero ingresado es: "+str(numero))
#print(type(numero))#str

#promedio = float(input("Ingrese el promedio: "))
#print("El promedio ingresado es: "+str(promedio))
#print(type(promedio))#float

#Funciones en Java
#public static void main(String[] args) {}
#[Visibilidad] [constante o no] [tipo de dato] [nombre de la funcion]([parametros]){}

def suma(a: int,b:int) ->int:
    #codigo de la funcion 
    return a+b

resultado: int = suma(5,10)
print("El resultado de la suma es: "+str(resultado))


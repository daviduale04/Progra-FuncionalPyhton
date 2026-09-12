# Dicionario en Python
# Map<String, String> persona = new HasMap<>();
# persona.put("nombre", "Juan");
# persona.put("edad", "20");
# persona.put("altura", "1.75");

# JSON
# { 
#  "nombre" : "Juan",
#  "edad" : "20",
#  "altura" : "1.75" 
# }

estudiante: dict[str,str] = { #[str,str] indica que es un diccionario con clave y valor de tipo string
    "clave ": "12345",
    "nombre": "Juan",
    "edad": "20",
    "altura": "1.75"
}
estudiante["nombre"] = "Juan Piguave"
estudiante["identificacion"] = "1234567890"

print("nombre: " + estudiante["nombre"])
print("identificacion: " + estudiante["identificacion"])

#########################
#########################
import nump as np #as np es un apodo de la libreria importada nump
nota: list[int] = [5,8,9,6,10]
nota_np =np.array(nota) #convertimos la lista a un array de numpy
print("Notas (lista): ",nota)
print("Notas numpy: ",nota_np)

media = np.mean(nota_np) #calculamos la media de las notas
print("La media de las notas es: ",media)

notaMaxima = np.max(nota_np) #calculamos la nota maxima
print("La nota maxima es: ",notaMaxima)



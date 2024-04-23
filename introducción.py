#Conjuntos: los conjuntos de datos desordenados y no indexados de elementos únicos. Se definen utilizando llaves {} o la función set ().

#conjunto de números 
numerosPrimos = {2,3,5,7,11}
# conjunto de letras 
lenguaje = set("Python3")
#agregar elementos a un conjunto 
numerosPrimos.add(13)
print(numerosPrimos)
#eliminar datos de un conjunto
lenguaje.remove("3")
print(lenguaje)
#Diccionarios : son colecciones de datos pares clave: valor {}

alumno = {
    "Nombre": "Juanito",
    "Edad": 30, 
    "Beca": True,
    "Ciudad": "Puerto Montt",
    "Provincia": "Llanquihue",

}
print(alumno)
#Imprimir dato especifico de un diccionario
print(alumno["Beca"])
#Modificar un dato especifico de un diccionario
alumno["Edad"] =50
print(alumno)
#Agregar un nuevo clave valor
alumno["Altura"]="1.20"
alumno["Nombre"] = "Miguelito"
print(alumno)

#Como saber de que tipo es una variable con typeof
print(type (numerosPrimos))
print(type (alumno))

#obtener un dato del usuario
datoUsuario= int (input("Ingrese un número"))
print(datoUsuario)
print (type(datoUsuario))

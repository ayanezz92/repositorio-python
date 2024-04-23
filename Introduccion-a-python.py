#Comentarios de una linea

"""
Comentarios de varias lineas

Que es una variable:
Es un espacio de memoria reservado para almacenar datos que pueden cambiar en el transcursodel programa.

Python es un lemguaje de programacion dinamico, no es necesario declarar explicitamente el tipo de variable antes de utilizarlo.

"""
#variables en Python:
#Deben contener letras, numeros o guiones bajos.
#deben comenzar con una letra.
#case sensitive
variable = 1
Variable = 1
#no se pueden utilizar palabras reservadas para definir variables
If = 1

"""
    False, as, None, True, and, assert, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, try, whille, with y yield.
    """
 #tipos de datos: 
entero = 2 
decimalFloat = 1.5
cadenaTexto = "Hola soy una cadena"

suma = 2+5
resta = 3-2
multiplicación = 3*3
división = 10/2
 #imprimir datos
print(suma)
print(resta)
print(multiplicación)
print(división)

mensaje = "Hola"
nombre = "Agustin"
 #concatenar variables + texto 
print(mensaje + "texto extra" + nombre)

#Booleanos
edad = 18
esEstudiante = True
estaTrabajando = False
#Operación lógica con booleanos
esMayorDeEdad = edad>=18
puedeVotar = esMayorDeEdad and estaTrabajando
print(esMayorDeEdad)
print (puedeVotar)

#Listas: son colecciones de datos ordenados y modificables. []
numeros = [1,2,3,4,5,6,7,8,9]
nombres = ["Raúl", "Pedro", "Cosme Fulanito"]

mixta = [1,"cosme", True, 1.4]

print(numeros)
print(numeros[6])
print(numeros[-3])


#Tuplas: Son colecciones de datos ordenados e inmutables.
()

coordenadas = (10,20)
meses = ("Enero", "Febrero", "Marzo")
print(meses)
print(meses[-2]) 
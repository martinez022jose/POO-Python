"""
Se desea crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

*Un constructor, donde los datos pueden estar vacíos.

*Los setters y getters para cada uno de los atributos.

*mostrar(): Muestra los datos de la persona.

*esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""
class Persona():
    def __init__(self,nombre,edad,dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    def nombre(self):
        return self._nombre
    
    def edad(self):
        return self._edad
    
    def dni(self):
        return self._dni

    def nombre(self,nombre):
        self._nombre = nombre

    def edad(self,edad):
        self._edad = edad

    def dni(self,dni):
        self._dni = dni

    def mostrar(self):
        return "Nombre: "+self._nombre+"\nEdad: "+str(self._edad)+"\nDni: "+str(self._dni)

    def esMayorDeEdad(self):
        return self._edad >= 18


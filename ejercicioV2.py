"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

*Un constructor, donde los datos pueden estar vacíos.
*Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
*mostrar(): Muestra los datos de la cuenta.
*ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
*retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""


class Cuenta():
    def __init__(self,persona,cantidad):
        self._persona = persona
        self._cantidad = cantidad
    
    def persona(self):
        return self._persona
    
    def cantidad(self):
        return self._cantidad

    def persona(self,persona):
        self._persona = persona 

    def cantidad(self,cantidad):
        self._cantidad = cantidad
    
    def mostrar(self):
        print("Persona:"+self._persona.mostrar() + "\nCantidad:" + str(self._cantidad))
    
    def ingresar(self,monto):
        if(monto <= 0):
            print("Debe ingresar saldo mayor a cero")
        else:
            self._cantidad += monto

    def retirar(self,monto):
        self._cantidad -= monto

persona = Persona("jose",22,1231)
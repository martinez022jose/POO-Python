"""
1. Crear una clase producto con los siguientes atributos:
 - codigo
 - nombre
 - precio
Creale un constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos unas unidades y
nos debe calcular el precio final.

2. Añadir una clase pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
   Añade las siguiente funcionalidad:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido

3. Siguiendo con la clase pedido, añade la siguiente funcionalidad:
    - aniadir_producto: le pasamos un producto y una cantidad,
    añadirá ese producto y esa cantidad a su respectiva lista.
    Debemos validar que el dato que nos pasen es correcto, es decir,
    que sea un producto y que la cantidad sea valida. En caso de que no,
    devolver una excepción.
    - eliminar_producto: le pasamos el producto a borrar, si existe, lo eliminamos.
    Sino existe devolver una excepcion, indicándolo.
    Comprobar también que es un producto lo que nos pasan.
"""

class Pedido:
    def __init__(self):
        self.__productos = []
        self.__cantidades = []
    
    @property
    def productos(self):
        return self.__productos

    @property
    def cantidades(self):
        return self.__cantidades

    @productos.setter
    def productos(self,productos):
        self.__productos = productos
    
    @cantidades.setter
    def cantidades(self,cantidades):
        self.__cantidades = cantidades

    def agregarAPedido(self,producto,cantidad):
        if not isinstance(producto,Producto):
            raise Exception("Debe ingresar algo de tipo Producto")

        if not isinstance(cantidad, int):
            raise Exception("Debe ingresa algo de tipo entero")

        if cantidad <= 0:
            raise Exception("Debe ingresar una cantidad > 0")

        if producto in self.__productos:
            index = self.__productos.index(producto)
            self.__cantidades[index]+=cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminarDePedido(self,producto):
        if not isinstance(producto,Producto):
            raise Exception("Debe ingresar algo de tipo entero")

        if producto in self.__productos:
            index = self.__productos.index(producto)
            self.__productos.pop(index)
        else:
            raise Exception("No se encontro el producto")
    
    def totalPedido(self):
        total = 0
        for (producto,cantidad) in zip(self.__productos,self.__cantidades):
            total+= producto.calcularTotal(cantidad)
        return total

    def mostrarPedido(self):
        for (producto,cantidad) in zip(self.__productos,self.__cantidades):
            print("Producto: "+producto.__str__()+"\nCantidad: "+str(cantidad))
    
    
class Producto:
    def __init__(self,codigo,nombre,precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @precio.setter
    def precio(self,precio):
        self.__precio = precio
    
    def __str__(self):
        return "\nCodigo:"+str(self.__codigo)+"\nNombre:"+self.__nombre+"\nPrecio:"+str(self.__precio)
    
    def calcularTotal(self,unidades):
        return self.__precio * unidades


import random

class Persona():
    def __init__(self,nombre,edad,carrera,monto,hijos,felicidadActual):
        self.__nombre = nombre
        self.__edad = edad
        self.__carrera = carrera 
        self.__monto = monto
        self.__hijos = hijos
        self.__felicidadActual = felicidadActual
        self.__sueniosPorCumplir = []
        self.__sueniosCumplidos = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self__edad

    @property
    def carrera(self):
        return self.__carrera
    
    @property
    def monto(self):
        return self.__monto

    @property
    def hijos(self):
        return self.__hijos
    
    @property
    def sueniosPorCumplir(self):
        return self.__sueniosPorCumplir

    @property
    def sueniosCumplidos(self):
        return self.__sueniosCumplidos

    @property
    def felicidadActual(self):
        return self.__felicidadActual

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @edad.setter
    def edad(self,edad):
        self.__edad = edad
    
    @carrera.setter
    def carrera(self,carrera):
        self.__carrera = carrera
    
    @monto.setter
    def monto(self,monto):
        self.__monto = monto

    def agregarSuenioPorCumplir(self,suenio):
        if suenio in self.__sueniosPorCumplir:
            raise Exception("Este suenio ya se encuentra en la lista de pendientes")
        else:
            self.__sueniosPorCumplir.append(suenio)
    
    def agregarSuenioCumplido(self,suenio):
        if suenio in self.__sueniosCumplidos:
            raise Exception("Este suenio ya se realizo")
        else:
            self.__sueniosCumplidos.append(suenio)
        
    def eliminarSuenioDeLista(self,lista,suenio):
        if suenio in lista:
            index = lista.index(suenio)
            lista.pop(index)
        else:
            print("Suenio a eliminar no pertenece a los sueñios pendientes")

    def cumplirSuenio(self,suenio):
        if suenio.validar(self):
            self.agregarSuenioCumplido(suenio)
            self.eliminarSuenioDeLista(self.__sueniosPorCumplir,suenio)
            self.__felicidadActual += suenio.nivelDeFelicidad
        else:
            if isinstance(suenio,Recibirse):
                raise Exception("Suenio no valido para carrera elegida")
            if isinstance(suenio,ConseguirTrabajo):
                raise Exception("Debe tener sueldo Mayor")
            if isinstance(suenio,Adoptar):
                raise Exception("Debe no poseer hijos")
    
    def cumplirSueniosMultiple(self,listaDeSuenios):
        for suenio in listaDeSuenios:
            self.cumplirSuenio(suenio)


    def listarSueniosPorCumplir(self):
        print("Lista de suenios por cumplir")
        for suenio in self.__sueniosPorCumplir:
            suenio.__str__()
    
    def listarSueniosCumplidos(self):
        print("Lista de suenios cumplidos")
        for suenio in self.__sueniosCumplidos:
            suenio.__str__()
    
    def posDeMayorFelicidad(self):
        mayorFelicidad = self.__sueniosPorCumplir[0].nivelDeFelicidad
        index = 0
        for suenio in self.__sueniosPorCumplir:
            if suenio.nivelDeFelicidad > mayorFelicidad:
                mayorFelicidad = suenio.nivelDeFelicidad
                index = self.__sueniosPorCumplir.index(suenio)
        return index
    
    def totalFelicidadSueniosPendientes(self):
        totalFelicidad = 0
        for suenio in self.__sueniosPorCumplir:
            totalFelicidad += suenio.nivelDeFelicidad
        return totalFelicidad

    def esFeliz(self):
        if self.totalFelicidadSueniosPendientes() < self.__felicidadActual:
            return True
        else:
            return False

    def cantidadDeSueniosSinImportarEstadoActual(self):
        cantidadDeSuenios = 0
        listaUnion = self.__sueniosCumplidos + self.__sueniosPorCumplir
        return len(listaUnion)
    
    def nivelDeAmbisioso(self):
         listaUnion = self.__sueniosCumplidos + self.__sueniosPorCumplir
         cantidadNivelAmbisioso = 0
         for suenio in listaUnion:
             if suenio.nivelDeFelicidad > 100:
                 cantidadNivelAmbisioso += 1
         return cantidadNivelAmbisioso
             
    def esAmbisiosa(self):
        if self.cantidadDeSueniosSinImportarEstadoActual() > 3 and self.nivelDeAmbisioso() > 3:
            return True
        else:
            return False
        
    def __str__(self):
        print( "{\nNombre "+ self.__nombre+"\nEdad:"+str(self.__edad)+"\nCarrera:"+self.__carrera+"\nMonto:"+str(self.__monto)+"\nHijos:"+str(self.__hijos)+"\nNivel De Felicidad:"+ str(self.__felicidadActual))

class Realista(Persona):
    def __init__(self,nombre,edad,carrera,monto,hijos,felicidadActual):
        super().__init__(nombre,edad,carrera,monto,hijos,felicidadActual)
    
    def cumplirSuenioPreciado(self):
        index = self.posDeMayorFelicidad()
        self.cumplirSuenio(self.sueniosPorCumplir[index])
            
class Obsesivo(Persona):
    def __init__(self,nombre,edad,carrera,monto,hijos,felicidadActual):
        super().__init__(nombre,edad,carrera,monto,hijos,felicidadActual)

    def cumplirSuenioPreciado(self):
        self.cumplirSuenio(self.sueniosPorCumplir[0])

class Alocado(Persona):
    def __init__(self, nombre,edad,carrera,monto,hijos,felicidadActual):
        super().__init__(nombre,edad,carrera,monto,hijos,felicidadActual)
    
    def cumplirSuenioPreciado(self):
        longitudLista = len(self.sueniosPorCumplir)
        numeroRandom = random.randint(0, longitudLista-1)
        self.cumplirSuenio(self.sueniosPorCumplir[numeroRandom])

class Suenio():
    def __init__(self,nombreDeSuenio,nivelDeFelicidad):
        self.__nombreDeSuenio = nombreDeSuenio
        self.__nivelDeFelicidad = nivelDeFelicidad

    @property
    def nombreDeSuenio(self):
         return self.__nombreDeSuenio
    @property
    def nivelDeFelicidad(self):
        return self.__nivelDeFelicidad
  

    def __str__(self):
        print ("{\nNombre Suenio:"+ self.__nombreDeSuenio+"\nNivel De Felicidad: "+ str(self.__nivelDeFelicidad))

class Recibirse(Suenio):
    def __init__(self,nombreDeSuenio,nivelDeFelicidad):
        super().__init__(nombreDeSuenio,nivelDeFelicidad)
    
    def validar(self,persona):
        if persona.carrera == super().nombreDeSuenio:
            return True
        else:
            return False

    def __str__(self):
        super().__str__()
        print("}")

class ConseguirTrabajo(Suenio):
    def __init__(self,nombreDeSuenio,nivelDeFelicidad,sueldo):
        super().__init__(nombreDeSuenio,nivelDeFelicidad)
        self.__sueldo = sueldo
    
    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self.__sueldo = sueldo

    def validar(self,persona):
        if self.__sueldo < persona.monto:
            return False
        else:
            return True

    def __str__(self):
        super().__str__()
        print("Sueldo: "+str(self.__sueldo)+"\n}")

class Adoptar(Suenio):
    def __init__(self,nombreDeSuenio,nivelDeFelicidad,cantidad):
        super().__init__(nombreDeSuenio,nivelDeFelicidad)
        self.__cantidad = cantidad
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def validar(self,persona):
        if persona.hijos > 0:
            return False
        else:
            return True
    def __str__(self):
        super().__str__()
        print("CantidadAAdoptar: "+str(self.__cantidad)+"\n}") 



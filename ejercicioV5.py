
class Pajaro():
    def __init__(self,ira,fuerza):
        self.__ira = ira
        self.__fuerza = fuerza
    
    @property
    def fuerza(self):
        return self.__fuerza

    @property
    def ira(self):
        return self.__ira    

    @fuerza.setter
    def fuerza(self,fuerza):
        self.__fuerza = fuerza

    @ira.setter
    def ira(self,ira):
        self.__ira = ira

    def enojarse(self):
        self.__ira = self.__ira * 2
    
    def listarPajaro(self):
        print("Fuerza:"+str(self.__fuerza)+"\nIra:"+str(self.__ira))

class Comun(Pajaro):
    def __init__(self,ira):
        self.ira = ira
        self.definirFuerza()
    
    def definirFuerza(self):
        self.fuerza =  self.ira * 2

    def enojarse(self):
        super().enojarse()
        self.definirFuerza()
    
class Red(Pajaro):
    def __init__(self,ira):
        self.ira = ira
        self.__cantidadDeEnojos = 0 
        self.definirFuerza()

    def definirFuerza(self):
        self.fuerza =  self.ira * 10 * self.__cantidadDeEnojos

    def enojarse(self):
        super().enojarse()
        self.__cantidadDeEnojos += 1
        self.definirFuerza()
        
class Bomb(Pajaro):
    def __init__(self,ira):
        self.__maxFuerza = 9000
        self.ira = ira
        self.fuerza = 0
        self.definirFuerza()

    def definirFuerza(self):
        if max(self.fuerza,self.ira*2) <=  self.__maxFuerza:
            self.fuerza = self.ira * 2
        else:
            raise Exception("Supero la maxima fuerza")

    def enojarse(self):
        super().enojarse()
        self.definirFuerza()

class Chuck(Pajaro):
    def __init__(self,ira,velocidad):
        self.ira = ira
        self.__velocidad = velocidad
        self.definirFuerza()
    
    def definirFuerza(self):
        if self.__velocidad < 80:
            self.fuerza = 150
        else:
            self.fuerza = 150 + 5* (self.__velocidad - 80)

    def enojarse(self):
        self.__velocidad *= 2
        self.definirFuerza()

class Terense(Pajaro):
    def __init__(self,ira):
        self.ira = ira
        self.__cantidadDeEnojos = 0
        self.__multiplicador = 0
        self.definirFuerza()

    @property
    def multiplicador(self):
        return self.multiplicador

    @multiplicador.setter
    def multiplicador(self,multiplicador):
        self.__multiplicador = multiplicador
    
    def definirFuerza(self):
        self.relacion(self.__multiplicador,self.__cantidadDeEnojos)
    
    def relacion(multiplicador,cantidadDeEnojos):
        pass 

    def enojarse(self):
        super().enojarse()
        self.__cantidadDeEnojos+= 1
        self.definirFuerza()

class Matilda(Pajaro):
    def __init__(self,ira):
        self.ira = ira
        self.__huevos = []
        self.definirFuerza()


    def definirFuerza(self):
        self.fuerza = (self.ira * 2) + self.totalPeso()

    def totalPeso(self):
        total = 0
        for huevo in self.__huevos:
            total += huevo.peso
        return total
    
    def agregarHuevo(self,huevo):
        self.__huevos.append(huevo)

    def enojarse(self):
        huevo = Huevo(2)
        self.agregarHuevo(huevo)
        self.definirFuerza()
        
class Huevo():
    def __init__(self,peso):
        self.__peso = peso
    
    @property
    def peso(self):
        return self.__peso

class Isla():
    def __init__(self):
        self.__pajaros = []
    
    def agregarPajaro(self,pajaro):
        self.__pajaros.append(pajaro)

    def esFuerte(self,pajaro):
        return pajaro.fuerza > 100
    
    def pajarosFuertes(self):
        fuertes = []
        for pajaro in self.__pajaros:
            if self.esFuerte(pajaro):
                fuertes.append(pajaro)
        return fuertes

    def fuerza(self):
        totalFuerza = 0
        for pajaro in self.pajarosFuertes():
            totalFuerza += pajaro.fuerza
        return totalFuerza

    def listarFuertes(self):
        for pajaro in self.__pajaros:
            if pajaro.fuerza > 100:
                pajaro.listarPajaro()
    
    def reducirIraEn(self,cantidad):
        for pajaro in self.__pajaros:
            pajaro.ira-=cantidad

    def evento(self,evento):
        if isinstance(evento,SesionManejoIra):
            self.reducirIraEn(5)


class SesionManejoIra():
    def __init__(self):
        pass





pajaro1 = Comun(400)
pajaro2 = Comun(300)
pajaro3 = Comun(200)
evento = SesionManejoIra()
isla = Isla()
isla.agregarPajaro(pajaro1)
isla.agregarPajaro(pajaro2)
isla.agregarPajaro(pajaro3)
isla.listarFuertes()

isla.evento(evento)

isla.listarFuertes()
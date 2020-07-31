import math

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

class IslaPajaro():
    def __init__(self):
        self.__pajaros = []
        self.__pajarosHomenajeados = []
        self.__eventos = []
    
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

    def enojarATodosLosPajaros(self):
        for pajaro in self.__pajaros:
            pajaro.enojarse()

    def enojarPajarosSegun(self,cantidad):
        _ , cantidadAEnojar = math.modf(cantidad/100)
        inicial = 0
        while inicial < cantidadAEnojar:
            self.enojarATodosLosPajaros()
            inicial+=1

    def enojarHomenajeados(self):
        for homenajeado in self.__pajarosHomenajeados:
            homenajeado.enojarse()

    def realizarEvento(self,evento):
        if isinstance(evento,SesionManejoIra):
            self.reducirIraEn(5)
        if isinstance(evento,InvasionDeCerditos):
            self.enojarPajarosSegun(evento.cantidad)
        if isinstance(evento,FiestaSorpresa):
            self.enojarHomenajeados()
        if isinstance(evento,EventosDesafortunados):
            self.__realizarEventos()

    def realizarEventos(self):
        for evento in self.__eventos:
            self.realizarEvento(evento)

class SesionManejoIra():
    def __init__(self):
        pass

class InvasionDeCerditos():
    def __init__(self,cantidad):
        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

class FiestaSorpresa():
    def __init__(self):
        pass

class EventosDesafortunados():
    def __init__(self):
        pass

class IslaCerdito():
    def __init__(self):
        self.__paredes = []
        self.__cerditos = []
    
    def agregarPared(self,pared):
        self.__paredes.append(pared)
    
    def agregarCerdito(self,cerdito):
        self.__cerditos.append(cerdito)

class Pared():
    def __init__(self,ancho):
        self.__ancho = ancho
        self.__resistencia = 0
    
    @property
    def ancho(self):
        return self.__ancho

    @property
    def resistencia(self):
        return self.__resistencia


class Vidrio(Pared):
    def __init__(self,ancho):
        super().__init__(ancho)
        self.definirResistencia()

    def definirResistencia(self):
        self.resistencia = 10 * self.ancho

class Madera(Pared):
    def __init__(self,ancho):
        super().__init__(ancho)
        self.definirResistencia()

    def definirResistencia(self):
        self.resistencia = 25 * self.ancho

class Piedra(Pared):
    def __init__(self,ancho):
        super().__init__(ancho)
        self.definirResistencia()

    def definirResistencia(self):
        self.resistencia= 50 * self.ancho

class Cerdito():
    def __init__(self):
        self.__resistencia = 0
    
    @property
    def resistencia(self):
        return self.__resistencia
    
    

class Obrero(Cerdito):
    def __init__(self):
        self.resistencia = 50

class Armado(Cerdito):
    def __init__(self):
        self.__armas = []
        self.definirResistencia()
    
    def agregarArma(self,arma):
        self.__armas.append(arma)

    def definirResistencia(self):
        self.resistencia = self.totalResistenciaCascos() +self.totalResistenciaEscudos
    
    def cascos(self):
        cascos = []
        for arma in self.__armas:
            if isinstance(arma,Casco):
                cascos.append(arma)
        return cascos
    
    def escudos(self):
        escudos = []
        for escudo in self.__armas:
            if isinstance(escudo,Escudo):
                escudos.append(escudo)
        return escudos
    
    def totalResistenciaEscudos(self):
        total = 0
        for escudo in self.escudos():
            total+=escudo.resistencia
        return total

    def totalResistenciaCascos(self):
        total = 0
        for casco in self.cascos():
            total+=casco.resistencia
        return total

class Arma():
    def __init__(self,resistencia):
        self.__resistencia = resistencia
    
    @property
    def resistencia(self):
        return self.__resistencia

class Casco(Arma):
    def __init__(self,resistencia):
        super().__init__(resistencia)

class Escudo(Arma):
    def __init__(self,resistencia):
        super().__init__(resistencia)



pajaro1 = Comun(400)
pajaro2 = Comun(300)
pajaro3 = Comun(200)
evento1 = InvasionDeCerditos(100)
isla = IslaPajaro()
isla.agregarPajaro(pajaro1)
isla.agregarPajaro(pajaro2)
isla.agregarPajaro(pajaro3)
isla.listarFuertes()

isla.realizarEvento(evento1)
print("---------------------------------")

isla.listarFuertes()
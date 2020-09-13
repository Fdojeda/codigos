from abc import ABC, abstractmethod 

class Delegaciones(ABC):
    def __init__ (self, moral, equipo, medallas, dinero):
        self.__moral = moral
        self.__equipo = equipo
        self.__medallas = medallas
        self.__dinero = dinero

    @abstractmethod
    def sanar_lesiones(self):
        pass

    def get_equipo(self):
        return self.__equipo

    def get_moral(self):
        return float(self.__moral)

    def set_moral(self, equipo):
        nueva_moral = 0
        equipo = self.get_equipo()
        for elem in equipo:
            nueva_moral += elem.moral
        if (nueva_moral/len(equipo)) > 100:
            nueva_moral = 100
            return nueva_moral
        elif (nueva_moral/len(equipo)) < 0:
            nueva_moral = 0
            return nueva_moral
        return float(nueva_moral/len(equipo))
        

class IEEEsparta(Delegaciones):
    def __init__ (self, moral, equipo, medallas, dinero):
        super().__init__(moral, equipo, medallas, dinero)
        
    def Entrenador(self, nombre):
        self.entrenador = nombre

    def sanar_lesiones(self):
        return "sanito uwu"
    
    def Equipo(self):
        pass
    

class DCCrotona(Delegaciones):
    def __init__ (self, moral, equipo, medallas, dinero):
        super().__init__(moral, equipo, medallas, dinero)
        
    def Entrenador(self, nombre):
        self.entrenador = nombre

    def sanar_lesiones(self):
        return "sanuto uwu"
    
    def Equipo(self):
        pass

class Deportistas:
    def __init__ (self, nombre, flex, moral, precio, velocidad, lesion, resist):
        self.nombre = nombre
        self.flexibilidad = flex
        self.moral = moral
        self.precio = precio
        self.velocidad = velocidad
        self.lesionado = lesion
        self.resistencia = resist

    def __str__(self):
        return "DEPORTISTA AÑADIDO: "+self.nombre

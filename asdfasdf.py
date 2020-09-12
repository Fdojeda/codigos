from abc import ABC, abstractmethod 

class Delegaciones:
    def __init__ (self):

     @abstractmethod
     def Entrenador(self):
        self.entrenador = "owo"

    @abstractmethod
    def Equipo(self):
            pass

    @abstractmethod
    def Medallas(self):
            pass

    @abstractmethod
    def Moral(self):
            pass

    @abstractmethod
    def Dinero(self):
            pass

    @abstractmethod
    def Excelencia_y_Respeto(self):
            pass

    @abstractmethod
    def implementos_deportivos(self):
            pass

    @abstractmethod
    def implementos_medicos(self):
            pass

    @abstractmethod
    def fichar_deportista(self):
            pass

    @abstractmethod
    def entrenar_deportista(self):
            pass

    @abstractmethod
    def sanar_lesiones(self):
            pass

    @abstractmethod
    def comprar_tecnologia(self):
            pass

    @abstractmethod
    def usar_habilidad_especial(self):
            pass

class IEEEsparta(Delegaciones):
    def __init__ (self):
        super().__init__() 
        
    def Entrenador(self):
        self.Entrenador = "uwu"

    def Equipo(self):
        


delegacion_1 = IEEEsparta()
delegacion_1.Entrenador()
print (delegacion_1.Entrenador) 
            

        

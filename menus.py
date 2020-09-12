from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self):
        self.atributo = "funciona :D"

class Menu_Inicio(Menu):
    def __init__(self):
        super().__init__()
        self.atrib = "esto funciona tambien"

    def nueva_partida(self):
        return "Partida nueva :D"

    def salir_del_programa(self):
        return "has salido :0"

class Menu_Principal(Menu):
    def __init__(self):
        super().__init__()
        self.at = "TAMBIEN FUNCIONAAAAAAA"

    def menu_entrenador(self):
        return "Este es el menu del entrenador"

    def simular_competencias(self):
        pass

    def mostrar_estado(self):
        pass

    def salir_del_programa(self):
        return "has salido :0"

class Menu_Entrenador(Menu_Principal):
    def __init__(self):
        super().__init__()
        self.entren = "soy un entrenador :0"

    def fichar(self):
        return "estas fichando D:"

    def entrenar(self):
        return "Estas entrenando D:"

    def sanar(self):
        return "c curo :v"

    def comprar_tecnología(self):
        return "c vende :v"

    def usar_habilidad_especial(self):
        return "c doble vende :Vvv"

    def simular_competencias(self):
        return "pium pium :V"

    def mostrar_estado(self):
        return "c muestra u//w//u"

men = Menu_Entrenador()
print(men.atributo)

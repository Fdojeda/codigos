from abc import ABC, abstractmethod
from cargar_datos import IEEES, DCC

### MENUS ###

class Menu(ABC):
    def __init__(self):
        self.atributo = "funciona :D"

    @abstractmethod
    def ejecutar(self):
        pass

class Menu_Inicio(Menu):
    def __init__(self):
        super().__init__()
        self.atrib = "esto funciona tambien"

    ###TAMBIEN SE ELIGE EQUIPO AAAAAAAAAAAAAAAA###
    def ejecutar(self):
        print("*****MENU INICIAL******")
        accion = input("Seleccione una Opción:\n[0] Comenzar una Nueva Partida.\n[1] Salir del Juego.\nOpcion Elegida: ")
        while True:
            if accion == "0":
                delegado = input("Elige tu nombre de Delegado: ")
                while True:
                    if delegado.isalnum():
                        IEEES.delegado = delegado
                        break
                    else:
                        delegado = input("NOMBRE INVALIDO!!\nElige tu nombre de Delegado (Hint: Sólo LETRAS y NUMEROS): ")
                print("NUEVO NOMBRE ARCHIVADO PARA IEEESPARTA!!")
                enemigo_delegado = input("Elige el nombre del delegado de DCCrotona: ")
                while True:
                    if enemigo_delegado.isalnum():
                        DCC.delegado = enemigo_delegado
                        
                        break
                    else:
                        enemigo_delegado = input("NOMBRE INVALIDO!!\nElige el nombre del delegado de DCCrotona (Hint: Sólo LETRAS y NUMEROS): ")
                print("NOMBRE ENEMIGO ARCHIVADO PARA DCCROTONA!!")
                menu_principal = Menu_Principal()
                return menu_principal.ejecutar()
            elif accion == "1":
                return "Has salido :v"
            else:
                accion = input("**********************\nSELECCION INVÁLIDA!\n\nSeleccione una Opción:\n[0] Comenzar una Nueva Partida.\n[1] Salir del Juego.\nOpcion Elegida: ")
            

class Menu_Principal(Menu):
    def __init__(self):
        super().__init__()
        self.at = "TAMBIEN FUNCIONAAAAAAA"

    def ejecutar(self):
        print("*-* HAZ INICIADO EL JUEGO *-*")
        print("*****MENU PRINCIPAL******")
        accion = input("Seleccione una Opción:\n[0] Menu Entrenador.\n[1] Simular Competencias.\n[2] Mostrar Estado.\n[3] Salir del Programa.\nOpcion Elegida: ")
        while True:
            if accion == "0":
                return "Has iniciado el juego :v"
            elif accion == "1":
                return "SIMULANDO UWU"
            elif accion == "2":
                return "Estado uieje"
            elif accion == "1":
                return "Has salido :vv"
            else:
                accion = input("**********************\nSELECCION INVÁLIDA!\n\nSeleccione una Opción:\n[0] Menu Entrenador.\n[1] Simular Competencias.\n[2] Mostrar Estado.\n[3] Salir del Programa.\nOpcion Elegida: ")

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

men = Menu_Inicio()
print(men.ejecutar())

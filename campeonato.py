from cargar_datos import IEEES, DCC

###CAMPEONATO###

class Campeonato:
    def __init__(self, dia):
        self.dia_actual = dia
        self.medallero = {"IEEES": 0 , "DCC": 0}

    def competencias_diarias(self):
        pass

    def premiar_deportistas(self):
        pass

    def calcular_moral(self):
        pass

    ###CODING DEEXCELENCIA, IMPLEMENTOS  MEDICOS Y WEASAAA
    def mostrar_estado(self):
        print("*****ESTADO DE LAS DELEGACIONES Y DEPORTISTAS*****\n-------------------------------------------------------------")
        print("IEEEsparta\nEntrenador: "+IEEES.delegado+"\nMoral del Equipo: "+str(IEEES.get_moral())+"\nMedallas: "+str(IEEES.get_medallas())+"\nDinero: "+str(IEEES.get_dinero())+"\n")
        print("Excelencia y respeto: "+str(0.8)+"\nImplementos deportivos: "+str(0.7)+"\nImplementos médicos: "+str(0.4)+"\n")
        print("Equipo Deportivo")
        print("Nombre Deportista    | Velocidad | Resistencia | Flexibilidad | Lesion")
        for deportista in IEEES.get_equipo():
            print((deportista.nombre)+(" "*(len("Nombre Deportista    | Velo")-len(deportista.nombre)))+str(deportista.velocidad)+(" "*(len("idad | Resist")-len(str(deportista.velocidad))))+str(deportista.resistencia)+(" "*(len("encia | Flexib")-len(str(deportista.resistencia))))+str(deportista.flexibilidad)+(" "*(len("lidad | Les")-len(str(deportista.flexibilidad))))+str(deportista.lesionado))
        print("*************************************************************")
        print("DCCrotona\nEntrenador: "+DCC.delegado+"\nMoral del Equipo: "+str(DCC.get_moral())+"\nMedallas: "+str(DCC.get_medallas())+"\nDinero: "+str(DCC.get_dinero())+"\n")
        print("Excelencia y respeto: "+str(1.0)+"\nImplementos deportivos: "+str(0.3)+"\nImplementos médicos: "+str(0.2)+"\n")
        print("Equipo Deportivo")
        print("Nombre Deportista    | Velocidad | Resistencia | Flexibilidad | Lesion")
        for deportista in DCC.get_equipo():
            print((deportista.nombre)+(" "*(len("Nombre Deportista    | Velo")-len(deportista.nombre)))+str(deportista.velocidad)+(" "*(len("idad | Resist")-len(str(deportista.velocidad))))+str(deportista.resistencia)+(" "*(len("encia | Flexib")-len(str(deportista.resistencia))))+str(deportista.flexibilidad)+(" "*(len("lidad | Les")-len(str(deportista.flexibilidad))))+str(deportista.lesionado))
        print("-------------------------------------------------------------")
        return "AQUI VA LO DE LAS COMPETENCIAS AAAAAAAAA"

camp = Campeonato(0)
print(camp.mostrar_estado())
print("c termino :0")



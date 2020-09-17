from abc import ABC, abstractmethod
from cargar_datos_y_deportes import IEEES, DCC, deportistas_totales, Ciclismo, Atletismo, Natacion, Gimnasia
from parametros import PUNTOS_ENTRENAMIENTO, IMPLEMENTOS_DEPORTIVOS_IEEESPARTA, IMPLEMENTOS_DEPORTIVOS_DCCROTONA, PONDERACION_ENTRENAMIENTO_IEEESPARTA, PRECIO_ENTRENAR_DEPORTISTA, IMPLEMENTOS_MEDICOS_IEEESPARTA, IMPLEMENTOS_MEDICOS_DCCROTONA, EXCELENCIA_Y_RESPETO_IEEESPARTA, EXCELENCIA_Y_RESPETO_DCCROTONA, PRECIO_SANAR_LESIONES, PRECIO_COMPRAR_TECNOLOGIA, BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES, BONUS_IMPLEMENTOS_DEPORTIVOS_DCC, BONUS_IMPEMENTOS_MEDICOS_IEEES, BONUS_IMPEMENTOS_MEDICOS_DCC
from parametros import PONDERACION_VELOCIDAD_ATLETISMO, PONDERACION_RESISTENCIA_ATLETISMO, PONDERACION_MORAL_ATLETISMO, PONDERACION_VELOCIDAD_NATACION, PONDERACION_RESISTENCIA_NATACION, PONDERACION_FLEXIBILIDAD_NATACION, PONDERACION_VELOCIDAD_CICLISMO, PONDERACION_RESISTENCIA_CICLISMO, PONDERACION_FLEXIBILIDAD_CICLISMO, PONDERACION_RESISTENCIA_GIMNASIA, PONDERACION_MORAL_GIMNASIA, PONDERACION_FLEXIBILIDAD_GIMNASIA
from parametros import PROBABILIDAD_ACCIDENTARSE_GIMNASIA, PROBABILIDAD_ACCIDENTARSE_CICLISMO, PROBABILIDAD_ACCIDENTARSE_NATACION, PROBABILIDAD_ACCIDENTARSE_ATLETISMO
import random

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

    def ejecutar(self):
        print("*****MENU INICIAL******")
        accion = input("Seleccione una Opción:\n[0] Comenzar una Nueva Partida.\n[1] Salir del Juego.\nOpcion Elegida: ")
        while True:
            if accion == "0":
                IEEES.delegado = ""
                DCC.delegado = ""
                delegado = input("Elige tu nombre de Delegado: ")
                while True:
                    if delegado.isalnum():
                        equipo = input("¿Qué equipo deseas apoyar?\n\n[0] IEEEsparta\n[1] DCCrotona\n\nElección: ")
                        while True:
                            if equipo == "0":
                                print("NUEVO NOMBRE ARCHIVADO PARA IEEESPARTA!!")
                                IEEES.propio = True
                                IEEES.delegado = delegado
                                break
                            elif equipo == "1":
                                print("NUEVO NOMBRE ARCHIVADO PARA DCCROTONA!!")
                                DCC.propio = True
                                DCC.delegado = delegado
                                break
                            else:
                                equipo = input("OPCIÓN INVÁLIDA!!\n¿Qué equipo deseas apoyar?\n\n[0] IEEEsparta\n[1] DCCrotona\n\nElección: ")
                        break
                    else:
                        delegado = input("NOMBRE INVALIDO!!\nElige tu nombre de Delegado (Hint: Sólo LETRAS y NUMEROS): ")
                enemigo_delegado = input("Elige el nombre del delegado de tu contrincante: ")
                while True:
                    if enemigo_delegado.isalnum():
                        if IEEES.delegado == delegado:
                            print("NOMBRE ENEMIGO ARCHIVADO PARA DCCROTONA!!")
                            DCC.delegado = enemigo_delegado
                        elif DCC.delegado == delegado:
                            print("NOMBRE ENEMIGO ARCHIVADO PARA IEEESPARTA!!")
                            IEEES.delegado = enemigo_delegado
                        break
                    else:
                        enemigo_delegado = input("NOMBRE INVALIDO!!\nElige el nombre del delegado de DCCrotona (Hint: Sólo LETRAS y NUMEROS): ")
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
                menu_propio = Menu_Entrenador()
                return menu_propio.ejecutar()
            elif accion == "1":
                return self.simular_competencias()
            elif accion == "2":
                return "Estado uieje"
            elif accion == "3":
                return "Has salido :vv"
            else:
                accion = input("**********************\nSELECCION INVÁLIDA!\n\nSeleccione una Opción:\n[0] Menu Entrenador.\n[1] Simular Competencias.\n[2] Mostrar Estado.\n[3] Salir del Programa.\nOpcion Elegida: ")

    def simular_competencias(self):
        eleccion = ""
        deporte = input("-----------------------------------\nDEPORTE A ELEGIR:\n\n[0] Ciclismo\n[1] Atletismo\n[2] Natacion\n[3] Gimnasia\n\nSU ELECCION: ")
        while True:
            if deporte == "0":
                eleccion = "0"
            elif deporte == "1":
                eleccion = "1"
            elif deporte == "2":
                eleccion = "2"
            elif deporte == "3":
                eleccion = "3"
            else:
                deporte = input("POR FAVOR, ELIJA UNA OPCION VÁLIDA\nSU ELECCION: ")        
        print("-----------------------------------\n SUS COMPETIDORES:\n")
        if IEEES.propio:
            i = 0
            for deportista in IEEES.get_equipo():
                print("["+str(i)+"] "+(deportista.nombre))
                i += 1
            comp_1 = input("ELIGA TU COMPETIDOR: ")
            while True:
                if comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(DCC.get_equipo()))
                    if deporte == "0":##########
                        DEPORT = Ciclismo(PROBABILIDAD_ACCIDENTARSE_CICLISMO, True, PONDERACION_VELOCIDAD_CICLISMO, PONDERACION_RESISTENCIA_CICLISMO, PONDERACION_FLEXIBILIDAD_CICLISMO)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(DCC.get_equipo()))
                    if deporte == "1":##########
                        DEPORT = Atletismo(PROBABILIDAD_ACCIDENTARSE_ATLETISMO, False, PONDERACION_VELOCIDAD_ATLETISMO, PONDERACION_RESISTENCIA_ATLETISMO, PONDERACION_MORAL_ATLETISMO)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(DCC.get_equipo()))
                    if deporte == "2":##########
                        DEPORT = Natacion(PROBABILIDAD_ACCIDENTARSE_NATACION, False, PONDERACION_VELOCIDAD_NATACION, PONDERACION_RESISTENCIA_NATACION, PONDERACION_FLEXIBILIDAD_NATACION)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                 elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(DCC.get_equipo()))
                    if deporte == "3":##########
                        DEPORT = Gimnasia(PROBABILIDAD_ACCIDENTARSE_GIMNASIA, True, PONDERACION_MORAL_GIMNASIA, PONDERACION_RESISTENCIA_GIMNASIA, PONDERACION_FLEXIBILIDAD_GIMNASIA)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"

        elif DCC.propio:
            i = 0
            for deportista in DCC.get_equipo():
                print("["+str(i)+"] "+(deportista.nombre))
                i += 1
            comp_1 = input("ELIGA TU COMPETIDOR: ")
            while True:
                if comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(IEEES.get_equipo()))
                    if deporte == "0":##########
                        DEPORT = Ciclismo(PROBABILIDAD_ACCIDENTARSE_CICLISMO, True, PONDERACION_VELOCIDAD_CICLISMO, PONDERACION_RESISTENCIA_CICLISMO, PONDERACION_FLEXIBILIDAD_CICLISMO)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(IEEES.get_equipo()))
                    if deporte == "1":##########
                        DEPORT = Atletismo(PROBABILIDAD_ACCIDENTARSE_ATLETISMO, False, PONDERACION_VELOCIDAD_ATLETISMO, PONDERACION_RESISTENCIA_ATLETISMO, PONDERACION_MORAL_ATLETISMO)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(IEEES.get_equipo()))
                    if deporte == "2":##########
                        DEPORT = Natacion(PROBABILIDAD_ACCIDENTARSE_NATACION, False, PONDERACION_VELOCIDAD_NATACION, PONDERACION_RESISTENCIA_NATACION, PONDERACION_FLEXIBILIDAD_NATACION)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                        
                 elif comp_1 < i:
                    COMPETIDOR_1 = IEEES.get_equipo()[comp_1]
                    COMPETIDOR_2 = random.randint(len(IEEES.get_equipo()))
                    if deporte == "3":##########
                        DEPORT = Gimnasia(PROBABILIDAD_ACCIDENTARSE_GIMNASIA, True, PONDERACION_MORAL_GIMNASIA, PONDERACION_RESISTENCIA_GIMNASIA, PONDERACION_FLEXIBILIDAD_GIMNASIA)
                        valido = DEPORT.validez_competencia(COMPETIDOR_1, COMPETIDOR_2)
                        if valido == "Ambos cumplen":
                            ganador = DEPORT.calcular_ganador(COMPETIDOR_1, COMPETIDOR_2)
                        elif valido == "IEEES no cumple":
                            return "GANA DCC WUU"
                        elif valido == "DCC no cumple":
                            return "GANA IEEES UWU"
                        elif valido == "Ninguno cumple":
                            return "EMPATE"
                else:
                    comp_1 = input("POR, FAVOR, ELIGA UN COMPETIDOR VÁLIDO: ")

    def mostrar_estado(self):
        return "c muestra u//w//u"##
    
class Menu_Entrenador(Menu_Principal):
    def __init__(self):
        super().__init__()
        self.entren = "soy un entrenador :0"

###VOLVER DE FICHAR Y DINERO NO NEGATIVO
    def ejecutar(self):
        print("------------------------------\n***** MENU ENTRENADOR *****")
        accion = input("Seleccione una Opción:\n[0] Fichar\n[1] Entrenar\n[2] Sanar Deportistas\n[3] Comprar Tecnología\n[4] Usar Habilidad Especial\n[5] Salir del Juego\n\nOpcion Elegida: ")
        while True:
            if accion == "0":
                print("*-* ELIGE DE LOS SIGUIENTES DEPORTISTAS *-*")
                i = 0
                deportistas_usables = []
                for deportista in deportistas_totales:
                    if deportista in IEEES.get_equipo() or  deportista in DCC.get_equipo():
                        continue
                    else:
                        print("["+str(i)+"] "+(deportista.nombre)+" [ $"+str(deportista.precio)+" ]")
                        i += 1
                        deportistas_usables.append(deportista)
                nuevo_deportista = input("\nSu Elección: ")
                while True:
                    if nuevo_deportista.isnumeric():
                        if int(nuevo_deportista) < i:
                            print("AÑADIDO "+str(deportistas_usables[int(nuevo_deportista)].nombre)+" AL EQUIPO!!")
                            if IEEES.propio:
                                IEEES.get_equipo().append(deportistas_usables[int(nuevo_deportista)])
                                print(IEEES.set_dinero(deportistas_usables[int(nuevo_deportista)].precio))
                            else:
                                DCC.get_equipo().append(deportistas_usables[int(nuevo_deportista)])
                                print(DCC.set_dinero(deportistas_usables[int(nuevo_deportista)].precio))
                            break
                        else:
                            nuevo_deportista = input("ELECCIÓN INVÁLIDA(Por favor, coloque el número)\nSu Elección: ")
                    else:
                        nuevo_deportista = input("ELECCIÓN INVÁLIDA(Por favor, coloque el número)\nSu Elección: ")
                return self.ejecutar()
            
            elif accion == "1":
                print("----------------------------------------------------------\nN° | Nombre Deportista            | Velocidad | Resistencia | Flexibilidad | Lesion")
                if IEEES.propio:
                    i = 0
                    for deportista in IEEES.get_equipo():
                        print(str(i)+".   "+(deportista.nombre)+(" "*(len("N° | Nombre Deportista       | Velo")-len(deportista.nombre)))+str(deportista.velocidad)+(" "*(len("idad | Resist")-len(str(deportista.velocidad))))+str(deportista.resistencia)+(" "*(len("encia | Flexib")-len(str(deportista.resistencia))))+str(deportista.flexibilidad)+(" "*(len("lidad | Les")-len(str(deportista.flexibilidad))))+str(deportista.lesionado))
                        i += 1
                    nombre_dep = input("Seleccione deportista a entrenar: ")
                    while True:
                        if nombre_dep.isnumeric() and int(nombre_dep)<i and  not IEEES.get_equipo()[int(nombre_dep)].lesionado:
                            atributo = input("Seleccione el atributo a Entrenar:\n\n[0] Velocidad\n[1] Resistencia\n[2] Flexibilidad\nSU ELECCIÓN: ")
                            while True:
                                if atributo == "0":
                                    IEEES.get_equipo()[int(nombre_dep)].velocidad += (PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus))* PONDERACION_ENTRENAMIENTO_IEEESPARTA)
                                    print(IEEES.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    IEEES.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(IEEES.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) * PONDERACION_ENTRENAMIENTO_IEEESPARTA)+" puntos de Velocidad!")
                                    return self.ejecutar()
                                elif atributo == "1":
                                    IEEES.get_equipo()[int(nombre_dep)].resistencia += (PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) * PONDERACION_ENTRENAMIENTO_IEEESPARTA)
                                    print(IEEES.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    IEEES.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(IEEES.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) * PONDERACION_ENTRENAMIENTO_IEEESPARTA)+" puntos de Resistencia!")
                                    return self.ejecutar()
                                elif atributo == "2":
                                    IEEES.get_equipo()[int(nombre_dep)].flexibilidad += (PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) * PONDERACION_ENTRENAMIENTO_IEEESPARTA)
                                    print(IEEES.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    IEEES.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(IEEES.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) * PONDERACION_ENTRENAMIENTO_IEEESPARTA)+" puntos de Flexibilidad !")
                                    return self.ejecutar()
                                else:
                                    atributo = input("OPCIÓN INVÁLIDA!!\nSU ELECCIÓN: ")
                        else:
                            nombre_dep = input("Por favor, seleccione una opción válida (Hint: N° del Jugador; Hint: Que no este lesionade!): ")
                elif DCC.propio:
                    i = 0
                    for deportista in DCC.get_equipo():
                        print(str(i)+".   "+(deportista.nombre)+(" "*(len("N° | Nombre Deportista       | Velo")-len(deportista.nombre)))+str(deportista.velocidad)+(" "*(len("idad | Resist")-len(str(deportista.velocidad))))+str(deportista.resistencia)+(" "*(len("encia | Flexib")-len(str(deportista.resistencia))))+str(deportista.flexibilidad)+(" "*(len("lidad | Les")-len(str(deportista.flexibilidad))))+str(deportista.lesionado))
                        i += 1
                    nombre_dep = input("Seleccione deportista a entrenar: ")
                    while True:
                        if nombre_dep.isnumeric() and int(nombre_dep)<i and not DCC.get_equipo()[int(nombre_dep)].lesionado:
                            atributo = input("Seleccione el atributo a Entrenar:\n\n[0] Velocidad\n[1] Resistencia\n[2] Flexibilidad\nSU ELECCIÓN: ")
                            while True:
                                if atributo == "0":
                                    DCC.get_equipo()[int(nombre_dep)].velocidad += (PUNTOS_ENTRENAMIENTO * IMPLEMENTOS_DEPORTIVOS_DCCROTONA)
                                    print(DCC.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    DCC.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(DCC.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(IMPLEMENTOS_DEPORTIVOS_DCCROTONA*DCC.cantidad_bonus)))+" puntos de Velocidad!")
                                    return self.ejecutar()
                                elif atributo == "1":
                                    DCC.get_equipo()[int(nombre_dep)].resistencia += (PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(IMPLEMENTOS_DEPORTIVOS_DCCROTONA*DCC.cantidad_bonus)))
                                    print(DCC.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    DCC.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(DCC.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(IMPLEMENTOS_DEPORTIVOS_DCCROTONA*DCC.cantidad_bonus)))+" puntos de Resistencia!")
                                    return self.ejecutar()
                                elif atributo == "2":
                                    DCC.get_equipo()[int(nombre_dep)].flexibilidad += (PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(IMPLEMENTOS_DEPORTIVOS_DCCROTONA*DCC.cantidad_bonus)))
                                    print(DCC.set_dinero(int(PRECIO_ENTRENAR_DEPORTISTA)))
                                    DCC.get_equipo()[int(nombre_dep)].moral += 1
                                    print("FELICIDADES!! "+str(DCC.get_equipo()[int(nombre_dep)].nombre)+" a ganado "+str(PUNTOS_ENTRENAMIENTO * (IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(IMPLEMENTOS_DEPORTIVOS_DCCROTONA*DCC.cantidad_bonus)))+" puntos de Flexibilidad !")
                                    return self.ejecutar()
                                else:
                                    atributo = input("OPCIÓN INVÁLIDA!!\nSU ELECCIÓN: ")
                        else:
                            nombre_dep = input("Por favor, seleccione una opción válida (Hint: N° del Jugador; Hint: Que no este lesionade!): ")
                else:
                    return "error :0"
            
            elif accion == "2":
                if IEEES.propio:
                    hay = False
                    for deportista in IEEES.get_equipo():
                        if deportista.lesionado:
                            hay = True
                            break
                        else:
                            continue
                    if not hay:
                        print("No tiene ningun deportista lesionado en el momento :)")
                        return self.ejecutar()
                    else:
                        print("----------------------------------------------------------\nDeportistas Lesionados:")
                        i = 0
                        dep_lesionados = []
                        for deportista in IEEES.get_equipo():
                            if deportista.lesionado:
                                dep_lesionados.append(deportista)
                                print(str(i)+".   "+(deportista.nombre))
                                i += 1
                            else:
                                continue
                        nombre_dep = input("Seleccione deportista a sanar: ")
                        while True:
                            if nombre_dep.isnumeric() and int(nombre_dep)<i:
                                porcentaje = round(min(1, max(0, ((float(dep_lesionados[int(nombre_dep)].moral)*((IMPLEMENTOS_MEDICOS_IEEESPARTA+(BONUS_IMPEMENTOS_MEDICOS_IEEES*IEEES.bonus_medico)) + EXCELENCIA_Y_RESPETO_IEEESPARTA))/200))),1)
                                valor = round(random.uniform(0.0,1.0),1)
                                if valor >= porcentaje:
                                    dep_lesionados[int(nombre_dep)].lesionado = False
                                    print(IEEES.set_dinero(int(PRECIO_SANAR_LESIONES)))
                                    print("FELICIDADES!! "+dep_lesionados[int(nombre_dep)].nombre+" se ha curade :D")
                                else:
                                    print("No logró curarse :c")
                                return self.ejecutar()
                            else:
                                nombre_dep = input("Seleccione a un deportista VÁLIDO para sanar: ")
                elif DCC.propio:
                    hay = False
                    for deportista in DCC.get_equipo():
                        if deportista.lesionado:
                            hay = True
                            break
                        else:
                            continue
                    if not hay:
                        print("No tiene ningun deportista lesionado en el momento :)")
                        return self.ejecutar()
                    else:
                        print("----------------------------------------------------------\nDeportistas Lesionados:")
                        i = 0
                        dep_lesionados = []
                        for deportista in DCC.get_equipo():
                            if deportista.lesionado:
                                dep_lesionados.append(deportista)
                                print(str(i)+".   "+(deportista.nombre))
                                i += 1
                            else:
                                continue
                        nombre_dep = input("Seleccione deportista a sanar: ")
                        while True:
                            if nombre_dep.isnumeric() and int(nombre_dep)<i:
                                porcentaje = round(min(1, max(0, ((float(dep_lesionados[int(nombre_dep)].moral)*((IMPLEMENTOS_MEDICOS_DCCROTONA+ (BONUS_IMPEMENTOS_MEDICOS_DCC*DCC.bonus_medico)) + EXCELENCIA_Y_RESPETO_DCCROTONA))/200))),1)
                                valor = round(random.uniform(0.0,1.0),1)
                                if valor >= porcentaje:
                                    dep_lesionados[int(nombre_dep)].lesionado = False
                                    print(DCC.set_dinero((int(PRECIO_SANAR_LESIONES)*2)))
                                    print("FELICIDADES!! "+dep_lesionados[int(nombre_dep)].nombre+" se ha curade :D")
                                else:
                                    print(dep_lesionados[int(nombre_dep)].nombre+" no logró curarse :c")
                                return self.ejecutar()
                            else:
                                nombre_dep = input("Seleccione a un deportista VÁLIDO para sanar: ")

            elif accion == "3":
                print("***** TIENDE IMPLEMEN3 DEPORTIVES Y MEDIQUES *****")
                opcion = input("Bienvenide! Desea comprar implementes deportives y mediques? Son inclusives!!!\nSu costo es de $"+str(PRECIO_COMPRAR_TECNOLOGIA)+"!! [SI/NO]\nSu Elección: ")##CAMBIAR LOL
                while True:
                    if IEEES.propio:
                        if opcion.lower() == "si" or opcion.lower() == "sí":
                            print(IEEES.set_dinero(PRECIO_COMPRAR_TECNOLOGIA))
                            IEEES.bonus_medico += 1
                            IEEES.cantidad_bonus += 1
                            print("Gracias uwu!! Sus Implementos Deportivos y Médicos han aumentado en 10%!")
                            return self.ejecutar()
                        elif opcion.lower() == "no" or opcion.lower() == "nó":
                            print("Ni modo, ni queria venderte >:V")
                            return self.ejecutar()
                        else:
                            opcion = input("Por favor, seleccione una opción válida!! [SI/NO]\n Su eleccion: ")
                    elif DCC.propio:
                        if opcion.lower() == "si" or opcion.lower() == "sí":
                            print(DCC.set_dinero(PRECIO_COMPRAR_TECNOLOGIA))
                            DCC.bonus_medico += 1
                            DCC.cantidad_bonus += 1
                            print("Gracias uwu!! Sus Implementos Deportivos y Médicos han aumentado en 10%!")
                            return self.ejecutar()
                        elif opcion.lower() == "no" or opcion.lower() == "nó":
                            print("Ni modo, ni queria venderte >:V")
                            return self.ejecutar()
                        else:
                            opcion = input("Por favor, seleccione una opción válida!! [SI/NO]\n Su eleccion: ")
                    
            elif accion == "4":
                return "pium muajaja >:V"
            elif accion == "5":
                return "Has salido :V"
            else:
                accion = input("SELECCION INVÁLIDA!!\nSeleccione una Opción:\n[0] Fichar\n[1] Entrenar\n[2] Sanar Deportistas\n[3] Comprar Tecnología\n[4] Usar Habilidad Especial\n[5] Salir del Juego\n\nOpcion Elegida: ")


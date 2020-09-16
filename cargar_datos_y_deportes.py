from entidades import IEEEsparta, DCCrotona, Deportistas
from parametros import NIVEL_IMPLEMENTOS, PUNTOS_ENTRENAMIENTO, IMPLEMENTOS_DEPORTIVOS_IEEESPARTA, IMPLEMENTOS_DEPORTIVOS_DCCROTONA, PONDERACION_ENTRENAMIENTO_IEEESPARTA, PRECIO_ENTRENAR_DEPORTISTA, IMPLEMENTOS_MEDICOS_IEEESPARTA, IMPLEMENTOS_MEDICOS_DCCROTONA, EXCELENCIA_Y_RESPETO_IEEESPARTA, EXCELENCIA_Y_RESPETO_DCCROTONA, PRECIO_SANAR_LESIONES, PRECIO_COMPRAR_TECNOLOGIA, BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES, BONUS_IMPLEMENTOS_DEPORTIVOS_DCC, BONUS_IMPEMENTOS_MEDICOS_IEEES, BONUS_IMPEMENTOS_MEDICOS_DCC, PONDERACION_VELOCIDAD_ATLETISMO, PONDERACION_RESISTENCIA_ATLETISMO, PONDERACION_MORAL_ATLETISMO, PUNTAJE_MINIMO, PONDERACION_VELOCIDAD_NATACION, PONDERACION_RESISTENCIA_NATACION, PONDERACION_FLEXIBILIDAD_NATACION, PONDERACION_VELOCIDAD_CICLISMO, PONDERACION_RESISTENCIA_CICLISMO, PONDERACION_FLEXIBILIDAD_CICLISMO, PONDERACION_RESISTENCIA_GIMNASIA, PONDERACION_MORAL_GIMNASIA, PONDERACION_FLEXIBILIDAD_GIMNASIA
from abc import ABC, abstractmethod

###ANADIR DEPORTISTAS A LISTA_DEPORTISTAS
deportistas_totales= []
with open("deportistas.csv", "r") as p:
    for line in p:
        if "nombre" in line:
            continue
        else:
            lin = line.split(",")
            true_lin = []
            lin[len(lin)-1] = lin[len(lin)-1].strip()
            for el in lin:
                if el.isnumeric():
                    el = int(el)
                elif el == "True":
                    el = True
                elif el == "False":
                    el = False
                elif el.isalpha():
                    el = str(el)
                true_lin.append(el)
            deportista = Deportistas(true_lin[0], true_lin[1], true_lin[2], true_lin[3], true_lin[4], true_lin[5], true_lin[6])
            deportistas_totales.append(deportista)

### AÑADIR DELEGADOS A LISTAS
delegacion_IE = []
delegacion_DC = []
with open("delegaciones.csv", "r") as d:
    for line in d:
        if "Moral" in line:
            continue
        else:
            lin = line.split(",")
            lin[len(lin)-1] = lin[len(lin)-1].strip()
            if len(delegacion_IE) == 0:
                ###BUSCAR DEPORTISTAS EN DEPORTISTAS TOTALES
                for elem in lin:
                    if ";" in elem:
                        obj_deports =[]
                        lin_temp = elem.split(";")
                        lin_temp[len(lin_temp)-1] = lin_temp[len(lin_temp)-1].strip()
                        for dep in lin_temp:
                            for deportista in deportistas_totales:
                                if dep == deportista.nombre:
                                    obj_deports.append(deportista)
                        delegacion_IE.append(obj_deports)
                    else:
                        delegacion_IE.append(elem)
            else:
                for elem in lin:
                    if ";" in elem:
                        obj_deports =[]
                        lin_temp = elem.split(";")
                        lin_temp[len(lin_temp)-1] = lin_temp[len(lin_temp)-1].strip()
                        for dep in lin_temp:
                            for deportista in deportistas_totales:
                                if dep == deportista.nombre:
                                    obj_deports.append(deportista)
                        delegacion_DC.append(obj_deports)
                    else:
                        delegacion_DC.append(elem)
            
###EQUIPOS EN CLASES
IEEES = IEEEsparta(delegacion_IE[0], delegacion_IE[2], delegacion_IE[3], delegacion_IE[4])
DCC = DCCrotona(delegacion_DC[0], delegacion_DC[2], delegacion_DC[3], delegacion_DC[4])

###DEPORTES####

class Deporte(ABC):
    def __init__(self, riesgo, implemento):
        self.riesgo = riesgo
        self.implemento = implemento

    @abstractmethod
    def validez_competencia(self, deportista_1, deportista_2):
        pass

    @abstractmethod
    def calcular_ganador(self, deportista_1, deportista_2):
        pass

### DEP_1 == IEEES ; DEP_2 == DCC
class Ciclismo(Deporte):
    def __init__(self, riesgo, implemento, vel, res, flex):
        super().__init__(riesgo, implemento)
        self.velocidad = vel
        self.resistencia = res
        self.flexibilidad = flex

    def validez_competencia(self, deportista_1, deportista_2):
        if (deportista_1 in IEEES.get_equipo() and deportista_2 in DCC.get_equipo()):
            if (not deportista_1.lesionado) and (not deportista_2.lesionado):
                if IEEES.propio:
                    if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) > NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) > NIVEL_IMPLEMENTOS):
                        return "Ambos cumplen"
                    else:
                        if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "Ninguno cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "IEEES no cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "DCC no cumple"
                elif DCC.propio:
                    if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) > NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) > NIVEL_IMPLEMENTOS):
                        return "Ambos cumplen"
                    else:
                        if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "Ninguno cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "IEEES no cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "DCC no cumple"
            else:
                if deportista_1.lesionado and deportista_2.lesionado:
                    return "Ninguno cumple"
                elif deportista_1.lesionado:
                    return "IEEES no cumple"
                elif deportista_2.lesionado:
                    return "DCC no cumple"
        else:
            if IEEES.propio:
                if (deportista_1 not in IEEES.get_equipo() and deportista_2  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_1 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_2 not in DCC.get_equipo()):
                    return "DCC no cumple"
            elif DCC.propio:
                if (deportista_2 not in IEEES.get_equipo() and deportista_1  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_2 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_1 not in DCC.get_equipo()):
                    return "DCC no cumple"

    def calcular_ganador(self, deportista_1, deportista_2):########
        puntaje_dep_1 = max(PUNTAJE_MINIMO, ((self.velocidad*deportista_1.velocidad) + (PONDERACION_RESISTENCIA_CICLISMO*deportista_1.resistencia) + (PONDERACION_FLEXIBILIDAD_CICLISMO*deportista_1.flexibilidad)))
        puntaje_dep_2 = max(PUNTAJE_MINIMO, ((self.velocidad*deportista_2.velocidad) + (PONDERACION_RESISTENCIA_CICLISMO*deportista_2.resistencia) + (PONDERACION_FLEXIBILIDAD_CICLISMO*deportista_2.flexibilidad)))
        if puntaje_dep_1 > puntaje_dep_2:
            return "ganó IEEES"
        elif puntaje_dep_1 < puntaje_dep_2:
            return "ganó DCC"
        else:
            return "Empate"

class Natacion(Deporte):
    def __init__(self, riesgo, implemento, vel, res, flex):
        super().__init__(riesgo, implemento)
        self.velocidad = vel
        self.resistencia = res
        self.flexibilidad = flex

    def validez_competencia(self, deportista_1, deportista_2):
        if (deportista_1 in IEEES.get_equipo() and deportista_2 in DCC.get_equipo()):
            if (not deportista_1.lesionado) and (not deportista_2.lesionado):
                return "Ambos cumplen"
            else:
                if deportista_1.lesionado and deportista_2.lesionado:
                    return "Ninguno cumple"
                elif deportista_1.lesionado:
                    return "IEEES no cumple"
                elif deportista_2.lesionado:
                    return "DCC no cumple"
        else:
            if IEEES.propio:
                if (deportista_1 not in IEEES.get_equipo() and deportista_2  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_1 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_2 not in DCC.get_equipo()):
                    return "DCC no cumple"
            elif DCC.propio:
                if (deportista_2 not in IEEES.get_equipo() and deportista_1  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_2 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_1 not in DCC.get_equipo()):
                    return "DCC no cumple"

    def calcular_ganador(self, deportista_1, deportista_2):########
        puntaje_dep_1 = max(PUNTAJE_MINIMO, ((PONDERACION_VELOCIDAD_NATACION*deportista_1.velocidad) + (PONDERACION_RESISTENCIA_NATACION*deportista_1.resistencia) + (PONDERACION_FLEXIBILIDAD_NATACION*deportista_1.flexibilidad)))
        puntaje_dep_2 = max(PUNTAJE_MINIMO, ((PONDERACION_VELOCIDAD_NATACION*deportista_2.velocidad) + (PONDERACION_RESISTENCIA_NATACION*deportista_2.resistencia) + (PONDERACION_FLEXIBILIDAD_NATACION*deportista_2.flexibilidad)))
        if puntaje_dep_1 > puntaje_dep_2:
            return "ganó IEEES"
        elif puntaje_dep_1 < puntaje_dep_2:
            return "ganó DCC"
        else:
            return "Empate"

class Atletismo(Deporte):
    def __init__(self, riesgo, implemento, vel, res, flex):
        super().__init__(riesgo, implemento)
        self.velocidad = vel
        self.resistencia = res
        self.flexibilidad = flex

    def validez_competencia(self, deportista_1, deportista_2):
        if (deportista_1 in IEEES.get_equipo() and deportista_2 in DCC.get_equipo()):
            if (not deportista_1.lesionado) and (not deportista_2.lesionado):
                return "Ambos cumplen"
            else:
                if deportista_1.lesionado and deportista_2.lesionado:
                    return "Ninguno cumple"
                elif deportista_1.lesionado:
                    return "IEEES no cumple"
                elif deportista_2.lesionado:
                    return "DCC no cumple"
        else:
            if IEEES.propio:
                if (deportista_1 not in IEEES.get_equipo() and deportista_2  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_1 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_2 not in DCC.get_equipo()):
                    return "DCC no cumple"
            elif DCC.propio:
                if (deportista_2 not in IEEES.get_equipo() and deportista_1  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_2 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_1 not in DCC.get_equipo()):
                    return "DCC no cumple"

    def calcular_ganador(self, deportista_1, deportista_2):#######
        puntaje_dep_1 = max(PUNTAJE_MINIMO, ((PONDERACION_VELOCIDAD_ATLETISMO*deportista_1.velocidad) + (PONDERACION_RESISTENCIA_ATLETISMO*deportista_1.resistencia) + (PONDERACION_MORAL_ATLETISMO*deportista_1.moral)))
        puntaje_dep_2 = max(PUNTAJE_MINIMO, ((PONDERACION_VELOCIDAD_ATLETISMO*deportista_2.velocidad) + (PONDERACION_RESISTENCIA_ATLETISMO*deportista_2.resistencia) + (PONDERACION_MORAL_ATLETISMO*deportista_2.moral)))
        if puntaje_dep_1 > puntaje_dep_2:
            return "ganó IEEES"
        elif puntaje_dep_1 < puntaje_dep_2:
            return "ganó DCC"
        else:
            return "Empate"

class Gimnasia(Deporte):
    def __init__(self, riesgo, implemento, res, flex, mor):
        super().__init__(riesgo, implemento)
        self.resistencia = res
        self.flexibilidad = flex
        self.moral = mor

    def validez_competencia(self, deportista_1, deportista_2):
        if (deportista_1 in IEEES.get_equipo() and deportista_2 in DCC.get_equipo()):
            if (not deportista_1.lesionado) and (not deportista_2.lesionado):
                if IEEES.propio:
                    if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) > NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) > NIVEL_IMPLEMENTOS):
                        return "Ambos cumplen"
                    else:
                        if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "Ninguno cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "IEEES no cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "DCC no cumple"
                elif DCC.propio:
                    if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) > NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) > NIVEL_IMPLEMENTOS):
                        return "Ambos cumplen"
                    else:
                        if ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS) and ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "Ninguno cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_IEEESPARTA+(BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES*IEEES.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "IEEES no cumple"
                        elif ((IMPLEMENTOS_DEPORTIVOS_DCCROTONA+(BONUS_IMPLEMENTOS_DEPORTIVOS_DCC*DCC.cantidad_bonus)) < NIVEL_IMPLEMENTOS):
                            return "DCC no cumple"
            else:
                if deportista_1.lesionado and deportista_2.lesionado:
                    return "Ninguno cumple"
                elif deportista_1.lesionado:
                    return "IEEES no cumple"
                elif deportista_2.lesionado:
                    return "DCC no cumple"
        else:
            if IEEES.propio:
                if (deportista_1 not in IEEES.get_equipo() and deportista_2  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_1 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_2 not in DCC.get_equipo()):
                    return "DCC no cumple"
            elif DCC.propio:
                if (deportista_2 not in IEEES.get_equipo() and deportista_1  not in DCC.get_equipo()):
                    return "Ninguno cumple"
                elif (deportista_2 not in IEEES.get_equipo()):
                    return "IEEES no cumple"
                elif (deportista_1 not in DCC.get_equipo()):
                    return "DCC no cumple"

    def calcular_ganador(self, deportista_1, deportista_2):###########
        puntaje_dep_1 = max(PUNTAJE_MINIMO, ((PONDERACION_FLEXIBILIDAD_GIMNASIA*deportista_1.flexibilidad) + (PONDERACION_RESISTENCIA_GIMNASIA*deportista_1.resistencia) + (PONDERACION_MORAL_GIMNASIA*deportista_1.moral)))
        puntaje_dep_2 = max(PUNTAJE_MINIMO, ((PONDERACION_FLEXIBILIDAD_GIMNASIA*deportista_2.flexibilidad) + (PONDERACION_RESISTENCIA_GIMNASIA*deportista_2.resistencia) + (PONDERACION_MORAL_GIMNASIA*deportista_2.moral)))
        if puntaje_dep_1 > puntaje_dep_2:
            return "ganó IEEES"
        elif puntaje_dep_1 < puntaje_dep_2:
            return "ganó DCC"
        else:
            return "Empate"

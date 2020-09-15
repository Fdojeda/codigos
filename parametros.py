import random
DIAS_COMPETENCIA = 6

PROBABILIDAD_ACCIDENTARSE_GIMNASIA = 0.3
PROBABILIDAD_ACCIDENTARSE_CICLISMO = 0.35
PROBABILIDAD_ACCIDENTARSE_NATACION = 0.25
PROBABILIDAD_ACCIDENTARSE_ATLETISMO = 0.2

PUNTAJE_MINIMO = 1

NIVEL_IMPLEMENTOS = 0

PUNTOS_ENTRENAMIENTO = 10

GANANCIA_MEDALLAS = 0.01

PRECIO_ENTRENAR_DEPORTISTA = 30
PRECIO_SANAR_LESIONES = 30
PRECIO_COMPRAR_TECNOLOGIA = 20
PRECIO_USAR_HABILIDAD_ESPECIAL = 20

EXCELENCIA_Y_RESPETO_IEEESPARTA = round(random.uniform(0.4,0.8),1)
EXCELENCIA_Y_RESPETO_DCCROTONA = round(random.uniform(0.3,0.7),1)

IMPLEMENTOS_DEPORTIVOS_IEEESPARTA = round(random.uniform(0.3,0.7),1)
IMPLEMENTOS_DEPORTIVOS_DCCROTONA = round(random.uniform(0.2,0.6),1)
BONUS_IMPLEMENTOS_DEPORTIVOS_IEEES = (IMPLEMENTOS_DEPORTIVOS_IEEESPARTA*0.1)
BONUS_IMPLEMENTOS_DEPORTIVOS_DCC = (IMPLEMENTOS_DEPORTIVOS_DCCROTONA*0.1)

IMPLEMENTOS_MEDICOS_IEEESPARTA = round(random.uniform(0.2,0.7),1)
IMPLEMENTOS_MEDICOS_DCCROTONA = round(random.uniform(0.4,0.8),1)
BONUS_IMPEMENTOS_MEDICOS_IEEES = (IMPLEMENTOS_MEDICOS_IEEESPARTA*0.1)
BONUS_IMPEMENTOS_MEDICOS_DCC = (IMPLEMENTOS_MEDICOS_DCCROTONA*0.1)
 
PONDERACION_ENTRENAMIENTO_IEEESPARTA = 1.7


PONDERACION_VELOCIDAD_ATLETISMO = 0.55
PONDERACION_VELOCIDAD_CICLISMO = 0.47
PONDERACION_VELOCIDAD_NATACION = 0.45

PONDERACION_RESISTENCIA_ATLETISMO = 0.2
PONDERACION_RESISTENCIA_CICLISMO = 0.36
PONDERACION_RESISTENCIA_GIMNASIA = 0.3
PONDERACION_RESISTENCIA_NATACION = 0.3

PONDERACION_MORAL_ATLETISMO = 0.25
PONDERACION_MORAL_GIMNASIA = 0.2

PONDERACION_FLEXIBILIDAD_CICLISMO = 0.17
PONDERACION_FLEXIBILIDAD_GIMNASIA = 0.5
PONDERACION_FLEXIBILIDAD_NATACION = 0.25

DIA_ACTUAL = 0

PREMIO_MEDALLA = 20
PREMIO_EQUIPO = 100

CASTIGO_PERDER = 10
CASTIGO_PERDER_EXCELENCIA = 0.02

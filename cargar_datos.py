from entidades import IEEEsparta, DCCrotona, Deportistas

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


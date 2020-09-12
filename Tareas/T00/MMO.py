import random

class Heroe:
    def __init__ (self, tipo, nombre, life, attack):
        self.nombre = nombre
        self.tipo = tipo
        self.life = life
        self.attack = attack
        self.damage = 0
        self.plus_atk = 0
        self.plus_life = 0
        self.inventory = []

    def __str__ (self):
        return "Tu nombre es "+self.nombre+"\nTu vida es "+str(self.life)+"\nTu ataque máximo sería de "+str(self.attack)


class Arma:
    def __init__ (self, nom, atk):
        self.nombre = nom
        self.ataque = atk

class Armadura:
    def __init__(self, nom, deff):
      self.nombre = nom
      self.defensa = deff
    
class Pocion:
    def __init__(self, nom, cura):
      self.nombre = nom
      self.curacion = cura
##########################

J1_nombre = input("Cual es tu nombre?: " )
J1_clase = input ("¿Quieres ser Guerrero, Arquero, Asesino o Mago? " )
if J1_clase == "guerrero":
    J1_tipo = "guerrero"
    J1_life = 550
    J1_atk  = random.randint(30,40)
    J1 = Heroe(J1_tipo, J1_nombre, J1_life, J1_atk)
elif J1_clase == "arquero":
    J1_tipo = "arquero"
    J1_life = 450
    J1_atk  = random.randint(30,45)
    J1 = Heroe(J1_tipo, J1_nombre, J1_life, J1_atk)
elif J1_clase == "asesino":
    J1_tipo = "asesino"
    J1_life = 300
    J1_atk  = random.randint(50,60)
    J1 = Heroe(J1_tipo, J1_nombre, J1_life, J1_atk)
elif J1_clase == "mago":
    J1_tipo = "mago"
    J1_life = 300
    J1_atk  = random.randint(50,65)
    J1 = Heroe(J1_tipo, J1_nombre, J1_life, J1_atk)

print(J1)

J1_arma = input("¿Deseas equiparte un Arma? si/no ")
if J1_arma == "si":
    if J1.tipo == "guerrero":
        print ("Te has equipado con La Lanza del Leon!")
        J1_arma = Arma("La Lanza del Leon", 45)
        J1.inventory.append(J1_arma)
        J1.plus_atk = J1_arma.ataque
    elif J1.tipo == "arquero":
        print ("Te has equipado con El Arco Meteoro!")
        J1_arma = Arma("El Arco Meteoro", 30)
        J1.inventory.append(J1_arma)
        J1.plus_atk = J1_arma.ataque
    elif J1.tipo == "asesino":
        print ("Te has equipado con La Hoja Umbría!")
        J1_arma = Arma("La Hoja Umbría", 25)
        J1.inventory.append(J1_arma)
        J1.plus_atk = J1_arma.ataque
    elif J1.tipo == "mago":
        print ("Te has equipado con La Vara Explosiva!")
        J1_arma = Arma("La Vara Explosiva", 35)
        J1.inventory.append(J1_arma)
        J1.plus_atk = J1_arma.ataque

J1_armadura = input("¿Deseas equiparte una Armadura? si/no ")
if J1_armadura == "si":
    if J1.tipo == "guerrero":
        print ("Te has equipado con La Coraza de Espinas!")
        J1_armadura = Armadura("La Coraza de Espinas", 35)
        J1.inventory.append(J1_armadura)
        J1.plus_life = J1_armadura.defensa
    elif J1.tipo == "arquero":
        print ("Te has equipado con La Capa de Cazador!")
        J1_armadura = Armadura("La Capa de Cazador", 40)
        J1.inventory.append(J1_armadura)
        J1.plus_life = J1_armadura.defensa
    elif J1.tipo == "asesino":
        print ("Te has equipado con La Capucha de Sombras!")
        J1_armadura = Armadura("La Capucha de Sombras", 30)
        J1.inventory.append(J1_armadura)
        J1.plus_life = J1_armadura.defensa
    elif J1.tipo == "mago":
        print ("Te has equipado con El Manto del Sabio!")
        J1_armadura = Armadura("El Manto del Sabio", 20)
        J1.inventory.append(J1_armadura)
        J1.plus_life = J1_armadura.defensa



J2_nombre = input("Cual es tu nombre?: " )
J2_clase = input ("¿Quieres ser Guerrero, Arquero, Asesino o Mago? " )
if J2_clase == "guerrero":
    J2_tipo = "guerrero"
    J2_life = 550
    J2_atk  = random.randint(30,40)
    J2 = Heroe(J2_tipo, J2_nombre, J2_life, J2_atk)
elif J2_clase == "arquero":
    J2_tipo = "arquero"
    J2_life = 450
    J2_atk  = random.randint(30,45)
    J2 = Heroe(J2_tipo, J2_nombre, J2_life, J2_atk)
elif J2_clase == "asesino":
    J2_tipo = "asesino"
    J2_life = 300
    J2_atk  = random.randint(50,60)
    J2 = Heroe(J2_tipo, J2_nombre, J2_life, J2_atk)
elif J2_clase == "mago":
    J2_tipo = "mago"
    J2_life = 300
    J2_atk  = random.randint(50,65)
    J2 = Heroe(J2_tipo, J2_nombre, J2_life, J2_atk)

print(J2)

J2_arma = input("¿Deseas equiparte un Arma? si/no ")
if J2_arma == "si":
    if J2.tipo == "guerrero":
        print ("Te has equipado con La Lanza del Leon!")
        J2_arma = Arma("La Lanza del Leon", 45)
        J2.inventory.append(J2_arma)
        J2.plus_atk = J2_arma.ataque
    elif J2.tipo == "arquero":
        print ("Te has equipado con El Arco Meteoro!")
        J2_arma = Arma("El Arco Meteoro", 30)
        J2.inventory.append(J2_arma)
        J2.plus_atk = J2_arma.ataque
    elif J2.tipo == "asesino":
        print ("Te has equipado con La Hoja Umbría!")
        J2_arma = Arma("La Hoja Umbría", 25)
        J2.inventory.append(J2_arma)
        J2.plus_atk = J2_arma.ataque
    elif J2.tipo == "mago":
        print ("Te has equipado con La Vara Explosiva!")
        J2_arma = Arma("La Vara Explosiva", 35)
        J2.inventory.append(J2_arma)
        J2.plus_atk = J2_arma.ataque

J2_armadura = input("¿Deseas equiparte una Armadura? si/no ")
if J2_armadura == "si":
    if J2.tipo == "guerrero":
        print ("Te has equipado con La Coraza de Espinas!")
        J2_armadura = Armadura("La Coraza de Espinas", 35)
        J2.inventory.append(J2_armadura)
        J2.plus_life = J2_armadura.defensa
    elif J2.tipo == "arquero":
        print ("Te has equipado con La Capa de Cazador!")
        J2_armadura = Armadura("La Capa de Cazador", 40)
        J2.inventory.append(J2_armadura)
        J2.plus_life = J2_armadura.defensa
    elif J2.tipo == "asesino":
        print ("Te has equipado con La Capucha de Sombras!")
        J2_armadura = Armadura("La Capucha de Sombras", 30)
        J2.inventory.append(J2_armadura)
        J2.plus_life = J2_armadura.defensa
    elif J2.tipo == "mago":
        print ("Te has equipado con El Manto del Sabio!")
        J2_armadura = Armadura("El Manto del Sabio", 20)
        J2.inventory.append(J2_armadura)
        J2.plus_life = J2_armadura.defensa

print("QUE COMIENCE LA BATALLA!!")
continuar = True

while continuar:
    a1 = random.randint(0,J1.attack) + J1.plus_atk
    a2 = random.randint(0,J2.attack) + J2.plus_atk
    b1 = J1.life + J1.plus_life
    b2 = J2.life + J2.plus_life
    print (J1.nombre,"ataca con",a1,"a",J2.nombre,", y este responde con",a2)

    if a1 >= a2:
        d= a1 - a2
        print (J2.nombre,"ah recibido",d,"puntos de daño!!")
        J2.life = J2.life - d
        print (J2.nombre,"se mantiene con",J2.life,"puntos de vida!")
        if J2.life <= 0:
            print (J2.nombre,"ha caido en batalla!!")
            continuar = False
            break
        if J1.life <= b1/2:
            pocion = input(J1.nombre+", ¿Quieres consumir una pocion? si/no")
            if pocion == "si":
                J1.life = J1.life + 20
                print ("Has recuperado 20 de vida!")
    elif a1 < a2:
        d = a2 - a1
        print (J1.nombre,"ah recibido",d,"puntos de daño!!")
        J1.life = J1.life - d
        print (J1.nombre,"se mantiene con",J1.life,"puntos de vida!")
        if J1.life <= 0:
            print (J1.nombre,"ha caido en batalla!!")
            continuar = False
            break
        if J2.life <= b2/2:
            pocion2 = input(J2.nombre+", ¿Quieres consumir una pocion? si/no")
            if pocion2 == "si":
                J2.life = J2.life + 20
                print ("Has recuperado 20 de vida!")




            

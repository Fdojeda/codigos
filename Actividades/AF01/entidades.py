class Criatura:

    def __init__(self, nombre, tipo, hp, atk, sp_atk, defense):
        self.nombre = nombre
        self.tipo = tipo
        self.__hp = hp
        self.hp_base = hp
        self.atk = atk
        self.sp_atk = sp_atk
        self.defense = defense
        self.preferencia_combate = ""
        pass

    def preferencia_combate(self):
        if len(self.tipo) > 5:
            self.preferencia_combate = "Especial"
            return "Especial"
        else:
            self.preferencia_combate = "Fisico"
            return "Fisico"

    def get_hp():
        return self.__hp

    def set_hp():
        self.hp = self.hpbase
        pass

    def recibir_ataque(self, dano):
        self.__hp = self.hp_base - dano
        pass

    def __str__(self):
        return self.nombre+", tipo "+self.tipo+"."
        pass


class Entrenador:

    def __init__(self, nombre, bolsillo):
        self.nombre = nombre
        self.bolsillo = []
        pass


if __name__ == "__main__":
    # NO MODIFICAR
    # El siguiente codigo te ayudara a hacer debugging,
    # simplemente ejecútalo para ver cómo vas

    # Instancias de Criatura
    criatura_alonso = Criatura("Alonso", "Dragon", 100, 100, 100, 100)
    criatura_juan = Criatura("Juan", "Normal", 90, 90, 90, 90)
    criatura_lucas = Criatura("Lucas", "Ground", 90, 90, 90, 90)

    # Aqui llamaremos a todos los atributos de la clase Criatura
    # si faltan atributos se indicara un mensaje de error
    # (Veremos try/except en profundidad más adelante en el curso)
    try:
        criatura_alonso.nombre
        criatura_alonso.tipo
        criatura_juan.hp
        criatura_juan.atk
        criatura_lucas.sp_atk
        criatura_lucas.defense
        print("Atributos de Criatura: OK")
    except AttributeError as error:
        print(f"Aún no completas los atributos de Criatura ({error})")

    # Aquí se prueba si el método preferencia_combate esta correctamente implmentado
    if criatura_alonso.preferencia_combate() != "Fisico" or criatura_juan.preferencia_combate() != "Especial":
        print("El método preferencia_combate aún no esta completado correctamente")
    else:
        print("Método preferencia_combate de Criatura: OK")

    # Aquí se prueba si el método recibir_ataque esta correctamente implmentado
    try:
        criatura_juan.recibir_ataque(100)
        if criatura_juan.hp != 0:
            print("El método recibir_ataque aún no esta completado correctamente")
        else:
            print("Método recibir_ataque de Criatura: OK")
    except AttributeError as error:
        print(f"Aún no completas el atributo hp de Criatura ({error})")

    # Instancia de Entrenador
    entrenador_jose = Entrenador("Jose", None)

    # Aqui llamaremos a todos los atributos de la clase Entrenador
    # si faltan atributos se indicara un mensaje de error
    try:
        entrenador_jose.nombre
        entrenador_jose.bolsillo
        print("Atributos de Entrenador: OK")
    except AttributeError as error:
        print("Aún no completas los atributos de Entrenador")

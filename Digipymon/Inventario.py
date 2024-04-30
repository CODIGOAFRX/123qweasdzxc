class Inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos.update({nombre: cantidad})

    def usar_objeto(self, nombre):
        if self.objetos.get(nombre, 0) > 0:
            self.objetos[nombre] -= 1
        else:
            print("No tienes este objeto en tu inventario.")
            print("")

    def mostrar_objetos(self):
        numerador = 0
        for nombre in self.objetos:
            numerador += 1
            print(str(numerador),"~ ",nombre," : " + str(self.objetos[nombre]))
            print("")

   
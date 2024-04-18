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

   
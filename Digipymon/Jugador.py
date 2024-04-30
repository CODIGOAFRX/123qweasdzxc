
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10
        self.contador_victorias_totales = 0
    
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1  
    
    # 
    def consultar_digipymon(self):
        for i, digipymon in enumerate(self.lista_digipymon):  
            print(f"{i+1}. {digipymon.nombre}")  
            print("")
    
    def consultar_digipoints(self):
        print(self.digicoins)  
    
    def consultar_evolucion(self,nombre_digipymon):
        contador_digipymon_evo = 0
        for digipymon in self.lista_digipymon:
            if digipymon.nombre == nombre_digipymon:
                contador_digipymon_evo += 1    
        if contador_digipymon_evo == 2:
            print("")
            print(f"{nombre_digipymon} puede evolucionar")
            return True
        else:
            print("")
            print(f"{nombre_digipymon} no puede evolucionar")
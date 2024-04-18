class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10
    
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1  
    
    # 
    def consultar_digipymon(self):
        for i, digipymon in enumerate(self.lista_digipymon):  
            print(f"{i+1}. {digipymon.nombre}")  
    
    def consultar_digipoints(self):
        print(self.digicoins)  
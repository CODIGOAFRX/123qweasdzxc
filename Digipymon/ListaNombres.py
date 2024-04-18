class ListaNombres:
    def __init__(self):
       self.lista_nombres_digipymons = ["Robertinho", "Folagor","Knekro", "Llanos", "Jaizinho", "Eusebio", "Dosantosaveiro", "Jalando", "Frinpong", "Ramosaurio", 
                                        "Mbapelico", "Benzos"," Zidaneon", "Juan", "Pogbarroso", "Pikete","Eldiablooh", "Tortilla","PEDROISONO","ErJavi" ]
       
       self.lista_nombres_entrenadores = ["Raul", "Pedro", "Hugo", "Ana", "La otra Ana", "Emilio", "Angel","Yerai",
                                          "Paco","Javi","Lucas", "Kratos", "Xian","Paulino", "Elvira", "LuisProfe",
                                          "SergioProfe", "IssakProfe","Berto","Erik"]
    
    def obtener_nombres_digipymon(self):
        import random
        r1 = random.randint(0,19)
        return self.lista_nombres_digipymons[r1]
    
    def obtener_nombre_entrenadores(self):
        import random
        r2 = random.randint(0,19)
        return self.lista_nombres_entrenadores[r2]
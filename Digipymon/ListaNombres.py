class ListaNombres:
    def __init__(self):
       self.lista_nombres_digipymons = ["Robertinho", "Folagor","Knekro", "Llanos", "Jaizinho", "Eusebio", "Dosantosaveiro", "Jalando", "Frinpong", "Ramosaurio", 
                                        "Mbapelico", "Benzos"," Zidaneon", "Juan", "Pogbarroso", "Pikete","Eldiablooh", "Tortilla","PEDROISONO","ErJavi" ]
       
       self.lista_nombres_entrenadores = ["Raul", "Pedro", "Hugo", "Ana", "La otra Ana", "Emilio", "Angel","Yerai",
                                          "Paco","Javi","Lucas", "Kratos", "Xian","Paulino", "Elvira", "LuisProfe",
                                          "SergioProfe", "IssakProfe","Berto","Erik"]
       self.lista_nombres_digipymons_evolucionados = ["Robertosaur", "Folagrow", "Knekraptor","Llanosaurus", "Jaizillia", "Eusebimonite", "Dosantogon", "Jalantos", "Frinponga", "Ramostorm",
                                                      "MbapeliKing","Benzorig","Zidaneonic", "Juanshine", "Pogbarrage", "Piketron", "Eldiabloc", "Tortillatrom", "PEDROISAI", "ErJavinator" ] 
    
    def obtener_nombres_digipymon(self):
        import random
        r1 = random.randint(0,19)
        return self.lista_nombres_digipymons[r1]
    
    def obtener_nombre_entrenadores(self):
        import random
        r2 = random.randint(0,19)
        return self.lista_nombres_entrenadores[r2]
    
    def obtener_nombre_digipymon_evolucionado(self,numero):
        
        return self.lista_nombres_digipymons_evolucionados[numero]
import random
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from ListaNombres import ListaNombres
from Digipymon import Digipymon 

def main():
    print("Bienvenido a Digipymon!! Podrás hacerte con todos?!")
    nombre_jugador = str(input("¿Cúal es tu nombre ser de Luz? "))
    print(f"Bienvenido {nombre_jugador}!!") 
    jugador1 = Jugador(nombre_jugador)
    inventario1 = Inventario()
    inventario1.añadir_objeto("Digipyball",3)
    bucle = True
    while bucle:
        opcion = menu()
        if opcion == 7:
            print("¡Hasta luego!")
            bucle = False
        elif opcion == 1:
            
            digipymon1 = buscar_digipymon(jugador1,inventario1)  
            probabilidad = 100 - (digipymon1.nivel * 50)    
            print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
            captura = str(input("Quieres intentar capturarlo? (y/n)"))  
            cuantas_digipyballs = inventario1.objetos.get("Digipyball")
            if captura == "y" or captura == "Y":
                if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                    bucle1 = True
                    while bucle1:
                        aleatorio = random.randint(1, 100)
                        inventario1.usar_objeto("Digipyball")
                        if aleatorio > 0 and aleatorio <= probabilidad :
                            jugador1.añadir_digipymon(digipymon1)
                            print("Enhorabuena, has capturado este ", str(digipymon1.nombre))  
                            bucle1 = False
                        else:
                            print("No has podido capturar este digipymon")
                            if cuantas_digipyballs > 0:
                                pregunta1 = str(input("Quieres volver a intentarlo? (y/n)"))
                                if pregunta1 == "n" or pregunta1 == "N":
                                    bucle1 = False
                            else: 
                                print("¡Ya no tienes digipyballs!")
                                bucle1 = False
                            
                        
                elif cuantas_digipyballs == 0:
                    print("!!!No tienes suficientes digipyballs¡¡¡")
                elif jugador1.cantidad_digipymon == 6:
                    print("No tienes suficiente espacio para guardar otro digipymon")
            elif captura == "n" or captura == "N":
                print("Has huido con éxito")
            else:
                print("Opción inválida. Intente de nuevo.")
        elif opcion == 2:
            combate(jugador1)
        elif opcion == 6:
            consultar_digipymons(jugador1)
    
    
    
def generar_digipymon_aleatorio():
    vida = random.randint(10, 20)
    ataque = random.randint(1,10)
    nivel = random.randint(1,3)
    tipos = ["Fuego", "Agua", "Planta"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    nombre = lista.obtener_nombres_digipymon()
    digipymon = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon

def menu():
    print("** Digipymon:                  ****")
    print("1. Buscar digipymon            ****")
    print("2. Luchar contra un entrenador ****")
    print("3. Ir a la tienda              ****")
    print("4. Usar objetos")
    print("5. Consultar inventario        ****")
    print("6. Consultar digipymons        ****")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def buscar_digipymon(Jugador,Inventario):
    digipymon1 = generar_digipymon_aleatorio()
    print(digipymon1)
   
    return digipymon1
    
def combate(jugador1):
    lista1 = ListaNombres()
    nombre = lista1.obtener_nombre_entrenadores()
    enemigo1 = Enemigo(nombre)
    for i in range(jugador1.cantidad_digipymon):
        digipymon_enemigo = generar_digipymon_aleatorio()
        enemigo1.añadir_digipymon(digipymon_enemigo)
        
    bucle2 = True
    while bucle2:
        opcion_combate = str(input("¿ Quieres enfrentarte a un enemigo de tu nivel ? (y/n)")) 
        if opcion_combate == "y" or opcion_combate == "Y":
            if jugador1.cantidad_digipymon != 0:
                print("¡Comienza el combate!")
                contador_win = 0
                contador_lose = 0
                for i in range(min(len(jugador1.lista_digipymon), len(enemigo1.lista_digipymon))):
                    print(f"Turno {i+1}:")
                    mi_digipymon = jugador1.lista_digipymon[i]
                    enemigo_digipymon = enemigo1.lista_digipymon[i]

                    print(f"Tu {mi_digipymon.nombre} se enfrenta al {enemigo_digipymon.nombre} del enemigo.")
                    print(f"Tu {mi_digipymon.nombre} tiene {mi_digipymon.ataque} de ataque.")
                    print(f"El {enemigo_digipymon.nombre} del enemigo tiene {enemigo_digipymon.ataque} de ataque.")

                    if mi_digipymon.ataque > enemigo_digipymon.ataque and mi_digipymon.vida != 0 :
                        print("¡Ganas el combate!")
                        diferencia_ataque = mi_digipymon.ataque - enemigo_digipymon.ataque
                        enemigo_digipymon.vida -= diferencia_ataque
                        if enemigo_digipymon.vida < 0 :  
                            enemigo_digipymon.vida = 0
                        contador_win += 1
                        print(f"Tu {mi_digipymon.nombre} ha ganado, pero pierde {diferencia_ataque} de vida.")
                    elif mi_digipymon.ataque < enemigo_digipymon.ataque or mi_digipymon.vida <= 0:
                        if mi_digipymon.vida <= 0:
                            print("¡Pierdes el combate! Tu digipymon está reventao pare")
                            contador_lose += 1
                        else:
                            print("¡Pierdes el combate!")
                            diferencia_ataque = enemigo_digipymon.ataque - mi_digipymon.ataque
                            mi_digipymon.vida -= diferencia_ataque
                            if enemigo_digipymon.vida < 0 :  
                                enemigo_digipymon.vida = 0
                            contador_lose += 1
                        
                        print(f"Tu {mi_digipymon.nombre} ha perdido, y pierde {diferencia_ataque} de vida.")
                    elif mi_digipymon.ataque == enemigo_digipymon.ataque:
                        print("¡Es un empate!")
                    
                    print("------")
                    print("Fin del combate.")
                if contador_win > contador_lose :
                    print("Tu recuento de victorias es favorable!! Enhorabuena ganaste el primer puesto hoy.")
                    jugador1.digicoins += contador_win * 5
                    bucle2 = False
                    
                elif contador_win < contador_lose :
                    print("Hoy ha sido un mal día, vuelve a intentarlo pronto!")
                    jugador1.digicoins -= contador_lose
                    if jugador1.digicoins < 0:
                        jugador1.digicoins = 0
                    bucle2 = False
                else:
                    print("¡Es un empate!")
                    bucle2 = False
                    jugador1.digicoins += contador_win 
            else: 
                print("No tienes digipymons")
                bucle2 = False
        elif opcion_combate == "n"  or opcion_combate == "N":
            print("Nos quedamos con uno de oro por tu cobardía")
            jugador1.digicoins -= 1
            bucle2 = False
            
def digishop():
    print("     TIENDA DIGISHOP:                                          ****")
    print("  1. Digipyball: 5 digicoins                                   ****")
    print("  2. Poción: 3 digicoins (restaura 10p de vida)                ****")
    print("  3. Anabolizantes: 4 digicoins (aumenta 5p de ataque)         ****")
    print("  4. Salir")
    opcion_tienda = int(input("Ingrese una opcion: "))
    return opcion_tienda
    
def consultar_digipymons(jugador1):
    for i in range(len(jugador1.lista_digipymon)):
        print(f"Digipymon numero {i+1}:")
        mi_digipymon = jugador1.lista_digipymon[i]
        print(str(mi_digipymon))

    
main()


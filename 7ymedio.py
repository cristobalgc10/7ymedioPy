import os
import random
import time

clear = lambda: os.system('cls') # Función para limpiar la consola de windows

baraja = list()
palosBaraja = {'O': 'Oro', 'C': 'Copas', 'B': 'Bastos', 'E': 'Espadas'}

puntosJugador   = 0
puntosOrdenador = 0

def menuInicial():
    clear()
    print(51 * "-")
    print(51 * "-")
    print(15 * "-", "JUEGO DEL 7 Y MEDIO", 15 * "-")
    print(51 * "-")
    print(51 * "-")
    print("""
        1.- Nueva Partida
        2.- Salir
    """)
    print(51 * "-")
    while True:
        opcionMenu = input('Elige una de las siguientes opciones: ')
        try:
            opcionMenu = int(opcionMenu)
        except:
            print('Introduce un número, vuelva a intentarlo.')
            continue

        if opcionMenu < 1 or opcionMenu > 3:
            print('La opción', opcionMenu, 'no existe, vuelve a intentarlo')
            continue
        
        if (opcionMenu == 1):
            nuevaPartida()
        elif (opcionMenu == 2):
            break
    exit

def menuPartida():
    clear()
    print(51 * "-")
    print(51 * "-")
    print(15 * "-", "JUEGO DEL 7 Y MEDIO", 15 * "-")
    print(51 * "-")
    print(51 * "-")
    print("""
        1.- Pedir carta
        2.- Pasar
    """)
    print(51 * "-")
    while True:

        opcionMenu = input('Elige una de las siguientes opciones: ')

        try:
            opcionMenu = int(opcionMenu)
        except:
            print('Introduce un número, vuelva a intentarlo.')
            continue

        if opcionMenu < 1 or opcionMenu > 3:
            print('La opción', opcionMenu, 'no existe, vuelve a intentarlo')
            continue
        
        if (opcionMenu == 1):
            pedirCarta(1)
            continue
        elif (opcionMenu == 2):
            pasarTurno()
            break
    
# menuInicial()
def nuevaPartida():
    global baraja
    global puntosJugador
    global puntosOrdenador

    baraja = list()
    crearBaraja()

    puntosJugador   = 0
    puntosOrdenador = 0

    menuPartida()



def crearBaraja():

    for palo in palosBaraja: # Recorro el diccionario de los palos para crear la baraja de cada palo
        for i in range(1,13):
            if i in [ 8,9 ] : continue # Salto los 8 y 9 ya que en este juego no se tiene en cuenta.
            baraja.append(str(i)+palo)

    random.shuffle(baraja) # Utilizo la libreria random para mezclar la lista, así la baraja se genera de forma desordenada.
    return baraja

print(crearBaraja())

def valorCarta( carta ):
    numCarta = int(carta[:-1]) # Extraigo la parte numerica de la carta y la asigna a una variable.
    if (numCarta <= 7):
        valor = numCarta
    else:
        valor = 0.5 
    return valor

# print(valorCarta('10O'))

def extraerCarta():
    # NOTA # Esto podría hacerse como función lambda
    # Tengo que implementar la comprobación del número de cartas disponibles en la baraja, para que no pida carta si no hay.
    carta = baraja.pop(-1) # Extraigo la última carta de la baraja y la asigno a la variable carta.
    return carta
    # print(valor)


# pedirCarta(1)
# print(puntosJugador)

def pasarTurno():
    if (puntosJugador == 0):
        print('Todavía nos pedido ninguna carta, pide una carta al menos para poder pasar.')
        time.sleep(3)
        menuPartida()
    
    print('Tu puntuación es', puntosJugador)
    print('Es turno del ordenador.')
    
    time.sleep(3)

    pedirCarta(0)


def pedirCarta(jugador): # 1 - Jugador, 0 - Ordenador
    
    global puntosJugador
    global puntosOrdenador



    if (jugador == 1):
        
        carta = extraerCarta()
        valor = valorCarta(carta)

        print('Carta para el jugador:', carta)
        puntosJugador += valor
        print('Puntos Jugador:', puntosJugador)
        if ( puntosJugador > 7.5 ):
            print('¡TE HAS PASADO')
            pasarTurno()
        

    if ( jugador == 0 ):
        while puntosOrdenador < puntosJugador:
            carta = extraerCarta()
            valor = valorCarta(carta)

            if (puntosOrdenador == 0):
                print( 'Cartas para el ordenador: ', end="" )
            print(carta, '  \r')
            puntosOrdenador += valor
            time.sleep(3)
            if (puntosJugador > 7.5):
                break
        print('Puntos del Ordenador:', puntosOrdenador)

        if ( puntosJugador == puntosOrdenador ):
            print ('Empate: Gana el ordenador con', puntosOrdenador, 'puntos.')
        elif ( puntosJugador > 7.5 ):
            print ('Te has pasado, gana el ordenador con', puntosOrdenador, 'puntos.')
        elif ( puntosOrdenador > 7.5 ): 
            print('Enhorabuena, has ganado con', puntosJugador, 'puntos.')
        else:
            print('Gana el ordenador con', puntosOrdenador, 'puntos.')

        time.sleep(10)
        menuInicial()        


menuInicial()



        










    
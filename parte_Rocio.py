import numpy as np
import random
import winsound
from icecream import ic

class Tablero:
    
    def __init__(self):
        self.numero_impactos = 0
        self.tablero_barcos  = np.array([["~" for i in range(10)] for j in range(10)])
        self.tablero_jugadas = np.array([["~" for i in range(10)] for j in range(10)])
        self.posiciones = [[(0,2)],[(1,1)],[(3,6)],[(9,5)],
                      [(2,7),(2,8)],[(3,3),(3,4)],[(5,5),(6,5)],
                      [(7,0),(8,0),(9,0)],[(6,8),(7,8),(8,8)],
                      [(8,2),(8,3),(8,4),(8,5)]]
        self.tipos_barcos = {1:4,2:3,3:2,4:1}
        self.posiciones_probadas = []

    def pintar_tablero_barcos(self):
        '''Imprime el tablero donde van a situarse los barcos'''
        ic("Pintar el tablero barcos")
        #print("Tablero barcos")
        for filas in range(10):
            for columnas in range(10):
                print(self.tablero_barcos[filas][columnas],end =" ")
            print(" ")

    def colocar_barcos(self):
        '''Colocamos los barcos en el tablero'''
        ic("Colocar los barcos")
        #print("Colocar barcos")
        for i in self.posiciones:
            self.pintar_barco(i)

    def pintar_barco(self,posiciones):
        '''Pintamos una B donde haya una posición de barco'''
        ic("Pintar barco")
        #print("Pintar barco")
        for i in posiciones:
            posx = i[0]
            posy = i[1]
            self.tablero_barcos[posx][posy] = "B"

    def estado_jugador(self):
        '''Jugador vivo o muerto'''
        ic("Estado jugador")
        #print("Estado jugador")
        vivo=True
        if self.numero_impactos==20:
            vivo=False
            return vivo
        return vivo


jugador = Tablero()
jugador.pintar_tablero_barcos()
jugador.colocar_barcos()
jugador.pintar_tablero_barcos()
jugador.estado_jugador()

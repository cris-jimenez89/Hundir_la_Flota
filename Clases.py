import numpy as np
import random
import winsound
from icecream import ic

class Tablero:
    
    
    def __init__(self) -> None:
        global TAM = 10
        self.numero_impactos = 0 
        self.tablero_barcos  = np.array([["~" for i in range(TAM)] for j in range(TAM)])
        self.tablero_jugadas = np.array([["~" for i in range(TAM)] for j in range(TAM)])
        self.posiciones = [[(0,2)],[(1,1)],[(3,6)],[(9,5)],
                      [(2,7),(2,8)],[(3,3),(3,4)],[(5,5),(6,5)],
                      [(7,0),(8,0),(9,0)],[(6,8),(7,8),(8,8)],
                      [(8,2),(8,3),(8,4),(8,5)]]
        self.tipos_barcos = {1:4,2:3,3:2,4:1}
        self.posiciones_probadas = []
        self.posicionesEnemigas = [] 
        
    
    def colocar_barcos(self):
       pass
    
    def pintar_tablero_barcos(self):
        pass

    def pintar_tablero_jugadas(self):
        pass

    def pintar_barco(self,posiciones):
        pass

    def pintar_resultado_disparo(self,resultado):
        pass

    def recibir_impacto(self,pos):
        pass

    def estado_jugador(self):
        pass

    def disparar(self):
        pass

    def posiciones_de_(self,c):
        '''
        Devuelve las posiciones del caracter c en tablero jugadas
        output: posiciones_enemigas:lista 
        '''
        ic("posiciones_de")
        posiciones = []
        for i in range(TAM):
            for j in range(TAM):
                if(self.tablero_jugadas[i][j] == c ):
                    posiciones.append((i,j))
        return posiciones
    
    def posiciones_cerca_impacto(self,pos):
        '''
        Da las posiciones cercana al impacto 
        output: posiciones:lista
        '''
        posiciones = []
        posx = pos[0]
        posy = pos[1]
        if (posx == 0):
            if(pos == (0,0)):
                if (self.tablero_barcos[0][1] == '~'):
                    posiciones.append((0,1))
                if (self.tablero_barcos[0][1] == '~'):
                    posiciones.append((1,0))
            elif (pos == (0,9)):
                if (self.tablero_barcos[0][8] == '~'):
                    posiciones.append((0,8))
                if (self.tablero_barcos[1][9] == '~'):
                    posiciones.append((1,0))
            else:
                if(self.tablero_barcos[0][posy+1] == '~'):
                    posiciones.append((0,posy+1))
                if(self.tablero_barcos[0][posy-1] == '~'):
                    posiciones.append((0,posy-1))
                if(self.tablero_barcos[1][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posx == 9):
            if(pos == (9,0)):
                if(self.tablero_barcos[8][0] == '~'):
                    posiciones.append((8,0))
                if(self.tablero_barcos[9][1] == '~'):
                    posiciones.append((9,1))
            elif(pos == (9,9)):
                if(self.tablero_barcos[8][9] == '~'):
                    posiciones.append((8,9))
                if(self.tablero_barcos[9][8] == '~'):
                    posiciones.append((9,8))
            else:
                if(self.tablero_barcos[9][posy+1] == '~'):
                    posiciones.append((9,posy+1))
                if(self.tablero_barcos[9][posy-1] == '~'):
                    posiciones.append((9,posy-1))
                if(self.tablero_barcos[8][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posy == 0 and posx != 0 and posx != 9):
            if(self.tablero_barcos[posx-1][0] == '~'):
                posiciones.append((posx-1,0))
            if(self.tablero_barcos[posx+1][0] == '~'):
                posiciones.append((posx+1,0))
            if(self.tablero_barcos[posx][1] == '~'):
                posiciones.append((posx,1))
            
        if(posy == 9 and posx != 0 and posx != 9):
            if(self.tablero_barcos[posx-1][9] == '~'):
                posiciones.append((posx-1,9))
            if(self.tablero_barcos[posx+1][9] == '~'):
                posiciones.append((posx+1,9))
            if(self.tablero_barcos[posx][8] == '~'):
                posiciones.append((posx,8))

        if posx in range(1,8) and posy in range(1,8):
            if(self.tablero_barcos[posx-1][posy] == '~'):
                posiciones.append((posx-1,posy))
            if(self.tablero_barcos[posx+1][posy] == '~'):
                posiciones.append((posx+1,posy))
            if(self.tablero_barcos[posx][posy-1] == '~'):
                posiciones.append((posx,posy-1))
            if(self.tablero_barcos[posx][posy+1] == '~'):
                posiciones.append((posx,posy+1))

        return posiciones
    
    def disparar_random(self):
        '''
        Dispara a posicion seleccionada de forma random
        output: posicion:tupla
        '''
        while True:
            posx = random.randint(0,9)
            posy = random.randint(0,9)
            ic("dispara:",(posx,posy))
            if((posx,posy) not in self.posiciones_probadas()):
                self.posiciones_probadas.append((posx,posy))
                return (posx,posy)

    def calcular_direccion(self,impacto1,impacto2):
        '''
        Calcular si existe relacion entre las 2 ultimas posiciones Enemigas
        output: dir: char (h/v)
        '''
        if(impacto1[0] == impacto2[0]):
            return 'h'
        elif(impacto1[1] == impacto2[1]):
            return 'v'
        else:
            return 'n'

    def disparar_cpu_inteligente(self):
        '''
        Dispara de forma inteligente
        output: (x,y): tupla
        relacion: posiciones_de,posiciones_cerca_impacto
                  disparar_random, calcular_direccion
        '''
        ic("disparar_cpu_inteligente")
        posiciones_cercanas_h = []
        posiciones_cercanas_v = []
        self.posicionesEnemigas = self.posiciones_de_('X')
        if (self.posicionesEnemigas == []):
            ic("dispara random no hay impacto previo")
            return self.disparar_random()
        else:
            if(len(self.posicionesEnemigas) == 1):
                ic("hay un impacto")
                posiciones_cercanas = self.posiciones_cerca_impacto(self.posicionesEnemigas[0])
                if posiciones_cercanas != []:
                    posicion = posiciones_cercanas.pop()
                    self.posiciones_probadas.append(posicion)
                    return posicion
                else:
                    return self.disparar_random() 
            else:
               #existen 2 impactos
               impacto1 = self.posicionesEnemigas[-1]
               impacto2 = self.posicionesEnemigas[-2]
               direccion = self.calcular_direccion(impacto1,impacto2)
               posx = impacto1[0]
               posy = impacto1[1]
               posiciones_cercanas = self.posiciones_cerca_impacto(impacto1)
               if(direccion == 'n'):
                   return self.disparar_random()
               elif(direccion == 'h'):
                   for i in posiciones_cercanas:
                       if(posx == i[0]):
                           posiciones_cercanas_h.append(i)
                   if(len(posiciones_cercanas_h) != 0):
                        posicion = posiciones_cercanas_h.pop()
                        self.posiciones_probadas(posicion)
                        return posicion
                   else:
                       return self.disparar_random()
               else:
                    #
                    for j in posiciones_cercanas:
                        if(posy == j[1]):
                            posiciones_cercanas_v.append(j)
                    if(len(posiciones_cercanas_v) != 0):
                        posicion = posiciones_cercanas_v.pop()
                        self.posiciones_probadas(posicion)
                        return posicion
                    else:
                        return self.disparar_random()
                        
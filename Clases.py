import pygame
import sys
import numpy as np
import random
import winsound
import icecream as ic
from Clases import Tablero
import constantes as c

class Tablero:
    
    
    def __init__(self) -> None:
        
        self.numero_impactos = 0 
        self.tablero_barcos  = np.array([["~" for i in range(c.TAM)] for j in range(c.TAM)])
        self.tablero_jugadas = np.array([["~" for i in range(c.TAM)] for j in range(c.TAM)])
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
        for i in range(c.TAM):
            for j in range(c.TAM):
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
            elif (pos == (0,c.TAM-1)): # (0,9)
                if (self.tablero_barcos[0][c.TAM-2] == '~'):
                    posiciones.append((0,c.TAM-2))
                if (self.tablero_barcos[1][c.TAM-1] == '~'):
                    posiciones.append((1,c.TAM-1))
            else: #en fila 0 pero sin ser extremo
                if(self.tablero_barcos[0][posy+1] == '~'):
                    posiciones.append((0,posy+1))
                if(self.tablero_barcos[0][posy-1] == '~'):
                    posiciones.append((0,posy-1))
                if(self.tablero_barcos[1][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posx == c.TAM-1):
            if(pos == (c.TAM-1,0)): #(9,0)
                if(self.tablero_barcos[c.TAM-2][0] == '~'):
                    posiciones.append((c.TAM-2,0))
                if(self.tablero_barcos[c.TAM-1][1] == '~'):
                    posiciones.append((c.TAM-1,1))
            elif(pos == (c.TAM-1,c.TAM-1)): #(9,9)
                if(self.tablero_barcos[c.TAM-2][c.TAM-1] == '~'):
                    posiciones.append((c.TAM-2,c.TAM-1))
                if(self.tablero_barcos[c.TAM-1][c.TAM-2] == '~'):
                    posiciones.append((c.TAM-1,c.TAM-2))
            else: #fila 9 sin ser extremo
                if(self.tablero_barcos[9][posy+1] == '~'):
                    posiciones.append((9,posy+1))
                if(self.tablero_barcos[9][posy-1] == '~'):
                    posiciones.append((9,posy-1))
                if(self.tablero_barcos[8][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posy == 0 and posx != 0 and posx != c.TAM-1): #en columana 0 pero sin ser extremo
            if(self.tablero_barcos[posx-1][0] == '~'):
                posiciones.append((posx-1,0))
            if(self.tablero_barcos[posx+1][0] == '~'):
                posiciones.append((posx+1,0))
            if(self.tablero_barcos[posx][1] == '~'):
                posiciones.append((posx,1))
            
        if(posy == c.TAM-1 and posx != 0 and posx != c.TAM-1): #en columna c.TAM-1
            if(self.tablero_barcos[posx-1][c.TAM-1] == '~'):
                posiciones.append((posx-1,c.TAM-1))
            if(self.tablero_barcos[posx+1][c.TAM-1] == '~'):
                posiciones.append((posx+1,c.TAM-1))
            if(self.tablero_barcos[posx][c.TAM-2] == '~'):
                posiciones.append((posx,c.TAM-2))

        if posx in range(1,c.TAM-2) and posy in range(1,c.TAM-2): # cualquier otra posicion del tablero
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
            posx = random.randint(0,c.TAM-1)
            posy = random.randint(0,c.TAM-1)
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

    def disparar_cerca_impacto(self):
        '''
        Dispara a una de las posiciones posibles cercanas al impacto existente
        output: posicion:tupla
        relacion: disparar_random
        '''
        posiciones_cercanas = self.posiciones_cerca_impacto(self.posicionesEnemigas[0])
        if posiciones_cercanas != []:
            posicion = posiciones_cercanas.pop()
            self.posiciones_probadas.append(posicion)
            return posicion
        else:
            return self.disparar_random()

    def disparar_cerca_dir_h(self,posiciones_cercanas,impacto1):
        '''
        Dispara cerca de la posicion y solo en direccion horizontal
        input: posiciones_cercanas:lista de tuplas posicion, impacto: tupla
        output: posicion:tupla
        relacion: disparar_random
        '''
        
        posiciones_cercanas_h = []
        posx = impacto1[0]
        posy = impacto1[1]
        for i in posiciones_cercanas:
            if(posx == i[0]):
                posiciones_cercanas_h.append(i)
            # añadir aqui resto de elementos con radio hasta 4 en posy de impacto1
            # hacer lo mismo en cerca_v
            #posiciones_cercanas_h.append((posx,posy))
            if(len(posiciones_cercanas_h) != 0):
                    posicion = posiciones_cercanas_h.pop()
                    self.posiciones_probadas(posicion)
                    return posicion
            else:
                return self.disparar_random() 

    def disparar_cerca_dir_v(self,posiciones_cercanas,impacto1):
        '''
        Dispara cerca de la posicion y solo en direccion vertical
        input: posiciones_cercanas:lista de tuplas posicion, impacto: tupla
        output: posicion:tupla
        relacion: disparar_random
        '''

        posiciones_cercanas_v = []
        posy = impacto1[1]
        for i in posiciones_cercanas:
            if(posy == i[1]):
                posiciones_cercanas_v.append(i)
            
            if(len(posiciones_cercanas_v) != 0):
                posicion = posiciones_cercanas_v.pop()
                self.posiciones_probadas(posicion)
                return posicion
            else:
                return self.disparar_random() 

    def disparar_cpu_inteligente(self):
        '''
        Dispara de forma inteligente
        output: (x,y): tupla
        relacion: posiciones_de,posiciones_cerca_impacto
                  disparar_random, calcular_direccion
        '''
        ic("disparar_cpu_inteligente")
        self.posicionesEnemigas = self.posiciones_de_('X')
        if (self.posicionesEnemigas == []):
            ic("dispara random no hay impacto previo")
            return self.disparar_random()
        else:
            if(len(self.posicionesEnemigas) == 1):
                ic("hay un impacto")
                return self.disparar_cerca_impacto()
            else:
               #existen 2 impactos
               impacto1 = self.posicionesEnemigas[-1]
               impacto2 = self.posicionesEnemigas[-2]
               direccion = self.calcular_direccion(impacto1,impacto2)
               
               posiciones_cercanas = self.posiciones_cerca_impacto(impacto1)
               if(direccion == 'n'):
                   return self.disparar_random()
               elif(direccion == 'h'):
                   return self.disparar_cerca_dir_h(posiciones_cercanas,impacto1)
               else:
                   return self.disparar_cerca_dir_v(posiciones_cercanas,impacto1)

class Juego:

    def __init__(self):
        '''
        Constructor Juego
        '''
        
        self.listaPosicionesHundidas1 = []
        self.listaPosicionesHundidas2 = []
        #iniciacion de pantalla
        # Inicializar pygame
        pygame.init()
        self.pantalla = pygame.display.set_mode((c.ANCHO, c.ALTO))
        self.jugador1 = Tablero()
        self.jugador2 = Tablero()   

    def iniciar_juego(self):
        '''
        Genera la flota para ambos jugadores
        relacion: generar_flota
        '''
        pass

    def jugar(self):
        '''
        En el tiene lugar la logica del juego controlando el turno y las
        acciones de los jugadores
        relacion: jugador.disparar, jugador.marcar_resultado_disparo,
                  pintar_tablero1, comprobar_estado_derrotado,
                  pintar_taablero2, winsound.Playsound,
                  dibujar_tablero
        '''
        pass  # AQUI VA EL BUCLE DEL JUEGO


    def dibujar_tablero(self,tablero, posicionesHundidas,x, y, mensaje):
        '''
        Pinta el tablero en pantalla
        '''
        # Dibujar etiqueta del tablero
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(mensaje, True, c.NEGRO)
        texto_rect = texto.get_rect(center=(x + c.TAM_CASILLA * 5, y - 30))
        self.pantalla.blit(texto, texto_rect)

        # Dibujar números de fila
        for i in range(c.TAM):
            num_fila = fuente.render(str(i), True, c.NEGRO)
            self.pantalla.blit(num_fila, (x - 30, y + i * c.TAM_CASILLA + 5))

            for j in range(c.TAM):
           
                if tablero[i][j] == 'X':
                    pygame.draw.rect(self.pantalla, c.VERDE, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA))
                elif tablero[i][j] == 'O':
                    pygame.draw.rect(self.pantalla, c.NEGRO, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA))
                elif tablero[i][j] == '~':
                    pygame.draw.rect(self.pantalla, c.AZUL, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA))
                else: #Hay una "B", pinta gris porque es un barco
                    pygame.draw.rect(self.pantalla, c.GRIS, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA))
                # Dibujar celdas y bordes de celda
                if((i,j) in posicionesHundidas):
                    pygame.draw.rect(self.pantalla, c.ROJO, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA))
                pygame.draw.rect(self.pantalla, c.BLANCO, (x + j * c.TAM_CASILLA, y + i * c.TAM_CASILLA, c.TAM_CASILLA, c.TAM_CASILLA), 1)
    
        # Dibujar bordes del tablero
        pygame.draw.rect(self.pantalla, c.NEGRO, (x, y, c.TAM_CASILLA * 10, c.TAM_CASILLA * 10), 3)
        # Dibujar números de columna
        for j in range(c.TAM):
            num_columna = fuente.render(str(j), True, c.NEGRO)
            self.pantalla.blit(num_columna, (x + j * c.TAM_CASILLA + 5, y + c.TAM_CASILLA * 10 + 5))

    def jugar_otra_vez(self):
        '''
        Pregunta al usuario si quiere jugar otra vez
        Output: bool
        relacion: winsound.Playsound
        '''
        while True:
          try:
            continuar = str(input("Quieres jugar otra vez (s/n)?"))
            if (continuar == "s"):
                winsound.PlaySound('sonidos/bonus.wav',winsound.SND_FILENAME)
                return True
            
            elif (continuar == "n"):
                winsound.PlaySound('sonidos/Windows Shutdown.wav',winsound.SND_FILENAME)
                return False
            else:
                print("opcion no valida")
          except Exception:
             print("introduzca (s/n)")


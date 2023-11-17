import numpy as np
import random
import winsound
import icecream as ic
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
        self.listaPosicionesHundidas = []
    
    
    
    def colocar_barcos(self):
        print("colocar barcos")
        for i in self.posiciones:
           self.pintar_barco(i)
    
    def pintar_tablero_barcos(self):
        print("pintar tablero barcos")
        for i in range(10):
            for j in range(10):
                print(self.tablero_barcos[i][j],end =" ")
            print(" ")

    def pintar_tablero_jugadas(self):
        print("pintar tablero jugadas")
        for i in range(10):
            for j in range(10):
                print(self.tablero_jugadas[i][j],end =" ")
            print(" ")    

    def pintar_barco(self,posiciones):
        print("pintar barco")
        for i in posiciones:
            self.tablero_barcos[i[0]][i[1]] = 'B'

    def pintar_resultado_disparo(self,resultado):
        print("pintar resultado")
        pos = resultado[0]
        posx = pos[0]
        posy = pos[1]
        caracter = resultado[1]
        self.tablero_jugadas[posx][posy] = caracter
        
    
    def recibir_impacto(self,pos):
        print("recibir_impacto")
        if(self.tablero_barcos[pos[0]][pos[1]] == "~"):
            print("agua")
            winsound.PlaySound("sonidos/splash.wav",winsound.SND_FILENAME)
            return [pos,"O"]
        else:
            print("tocado")
            winsound.PlaySound("sonidos/explosion.wav",winsound.SND_FILENAME)
            self.numero_impactos = self.numero_impactos + 1
            print(self.numero_impactos)
            return [pos,"X"]

    def estado_jugador(self):
        print("estado_jugador")
        vivo = True
        if(self.numero_impactos == 20):
            vivo = False
        return vivo

    def disparar(self):
        print("disparar")
        while True:
            posx = random.randint(0,9)
            posy = random.randint(0,9)
            print((posx,posy))
            if((posx,posy) not in self.posiciones_probadas):
                self.posiciones_probadas.append((posx,posy))
                print(self.posiciones_probadas)
                return(posx,posy)
            else:
                print("posicion repetida")    

    

    def posiciones_de_(self,c):
        '''
        Devuelve las posiciones del caracter c en tablero jugadas
        output: posiciones_enemigas:lista 
        '''
        #ic("posiciones_de")
        posiciones = []
        for i in range(10):
            for j in range(10):
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
                if (self.tablero_jugadas[0][1] == '~'):
                    posiciones.append((0,1))
                if (self.tablero_jugadas[0][1] == '~'):
                    posiciones.append((1,0))
            elif (pos == (0,c.TAM-1)): # (0,9)
                if (self.tablero_jugadas[0][c.TAM-2] == '~'):
                    posiciones.append((0,c.TAM-2))
                if (self.tablero_jugadas[1][c.TAM-1] == '~'):
                    posiciones.append((1,c.TAM-1))
            else: #en fila 0 pero sin ser extremo
                if(self.tablero_barcos[0][posy+1] == '~'):
                    posiciones.append((0,posy+1))
                if(self.tablero_jugadas[0][posy-1] == '~'):
                    posiciones.append((0,posy-1))
                if(self.tablero_jugadas[1][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posx == c.TAM-1):
            if(pos == (c.TAM-1,0)): #(9,0)
                if(self.tablero_jugadas[c.TAM-2][0] == '~'):
                    posiciones.append((c.TAM-2,0))
                if(self.tablero_jugadas[c.TAM-1][1] == '~'):
                    posiciones.append((c.TAM-1,1))
            elif(pos == (c.TAM-1,c.TAM-1)): #(9,9)
                if(self.tablero_jugadas[c.TAM-2][c.TAM-1] == '~'):
                    posiciones.append((c.TAM-2,c.TAM-1))
                if(self.tablero_jugadas[c.TAM-1][c.TAM-2] == '~'):
                    posiciones.append((c.TAM-1,c.TAM-2))
            else: #fila 9 sin ser extremo
                if(self.tablero_jugadas[9][posy+1] == '~'):
                    posiciones.append((9,posy+1))
                if(self.tablero_jugadas[9][posy-1] == '~'):
                    posiciones.append((9,posy-1))
                if(self.tablero_jugadas[8][posy] == '~'):
                    posiciones.append((1,posy))
        
        if(posy == 0 and posx != 0 and posx != c.TAM-1): #en columana 0 pero sin ser extremo
            if(self.tablero_jugadas[posx-1][0] == '~'):
                posiciones.append((posx-1,0))
            if(self.tablero_jugadas[posx+1][0] == '~'):
                posiciones.append((posx+1,0))
            if(self.tablero_jugadas[posx][1] == '~'):
                posiciones.append((posx,1))
            
        if(posy == c.TAM-1 and posx != 0 and posx != c.TAM-1): #en columna c.TAM-1
            if(self.tablero_jugadas[posx-1][c.TAM-1] == '~'):
                posiciones.append((posx-1,c.TAM-1))
            if(self.tablero_jugadas[posx+1][c.TAM-1] == '~'):
                posiciones.append((posx+1,c.TAM-1))
            if(self.tablero_jugadas[posx][c.TAM-2] == '~'):
                posiciones.append((posx,c.TAM-2))

        if posx in range(1,c.TAM-1) and posy in range(1,c.TAM-1): # cualquier otra posicion del tablero
            if(self.tablero_jugadas[posx-1][posy] == '~'):
                posiciones.append((posx-1,posy))
            if(self.tablero_jugadas[posx+1][posy] == '~'):
                posiciones.append((posx+1,posy))
            if(self.tablero_jugadas[posx][posy-1] == '~'):
                posiciones.append((posx,posy-1))
            if(self.tablero_jugadas[posx][posy+1] == '~'):
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
            #ic("dispara:",(posx,posy))
            if(len(self.posiciones_probadas) == 0):
                self.posiciones_probadas.append((posx,posy))
                return (posx,posy)
            else:
                if((posx,posy) not in self.posiciones_probadas):
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
        if posy + 2 < 10 and posy -2 >= 0:    
            posiciones_cercanas_h.append((posx,posy-2))
            posiciones_cercanas_h.append((posx,posy+2))
        if(len(posiciones_cercanas_h) != 0):
            posicion = posiciones_cercanas_h.pop()
            self.posiciones_probadas.append(posicion)
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
        posx = impacto1[0]
        posy = impacto1[1]
        for i in posiciones_cercanas:
            if(posy == i[1]):
                posiciones_cercanas_v.append(i)
            if posx + 2 < 10 and posx -2 >= 0:    
                posiciones_cercanas_v.append((posx-2,posy))
                posiciones_cercanas_v.append((posx+2,posy))
            if(len(posiciones_cercanas_v) != 0):
                posicion = posiciones_cercanas_v.pop()
                self.posiciones_probadas.append(posicion)
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
        #ic("disparar_cpu_inteligente")
        self.posicionesEnemigas = self.posiciones_de_('X')
        if (self.posicionesEnemigas == []):
            #ic("dispara random no hay impacto previo")
            return self.disparar_random()
        else:
            if(len(self.posicionesEnemigas) == 1):
                #ic("hay un impacto")
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



import pygame
import sys
import icecream as ic
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
        self.jugador1.colocar_barcos()
        self.jugador2.colocar_barcos()

    def jugar(self):
        '''
        En el tiene lugar la logica del juego controlando el turno y las
        acciones de los jugadores
        relacion: jugador.disparar, jugador.marcar_resultado_disparo,
                  pintar_tablero1, comprobar_estado_derrotado,
                  pintar_taablero2, winsound.Playsound,
                  dibujar_tablero
        '''
        # AQUI VA EL BUCLE DEL JUEGO
        turno = 1
        while True:
            if ( turno == 1):
                #jugador1 dispara y apunta el resultado
                print("jugador1 dispara")
                posicion = self.jugador1.disparar()
                print(posicion)
                resultado = self.jugador2.recibir_impacto(posicion)
                self.jugador1.pintar_resultado_disparo(resultado)
                print("tablero jugadas jugador1")
                self.jugador1.pintar_tablero_jugadas()
                self.listaPosicionesHundidas2 = self.jugador2.listaPosicionesHundidas
                self.dibujar_tablero(self.jugador1.tablero_jugadas,self.listaPosicionesHundidas2 ,c.MARGEN, 50, "Tablero 1")
                self.dibujar_tablero(self.jugador2.tablero_jugadas,self.listaPosicionesHundidas1 ,c.ANCHO - c.TAM_CASILLA * 10 - c.MARGEN, 50, "Tablero 2")

                if (resultado[1] != "X"):
                    turno = 2
                else:
                    vivo = self.jugador2.estado_jugador()
                    if not vivo:
                        print("has ganado jugador1")
                        winsound.PlaySound("sonidos/tada.wav",winsound.SND_FILENAME)
                        break
       
            else:
                #jugador2 dispara y apunta el resultado
                print("jugador2 dispara")
                posicion2 = self.jugador2.disparar_cpu_inteligente()
                print(posicion2)
                resultado2 = self.jugador1.recibir_impacto(posicion2)
                self.jugador2.pintar_resultado_disparo(resultado2)
                print("tablero jugadas jugador2")
                self.jugador2.pintar_tablero_jugadas()
                self.listaPosicionesHundidas1 = self.jugador1.listaPosicionesHundidas
                # Dibujar tableros
                self.dibujar_tablero(self.jugador1.tablero_jugadas, self.listaPosicionesHundidas2,c.MARGEN, 50, "Tablero 1")
                self.dibujar_tablero(self.jugador2.tablero_jugadas, self.listaPosicionesHundidas1,c.ANCHO - c.TAM_CASILLA * 10 - c.MARGEN, 50, "Tablero 2")
                if(resultado2[1] != "X"):
                    turno = 1
                else:
                    vivo = self.jugador2.estado_jugador()
                    if not vivo:
                        print("has ganado jugador2")
                        winsound.PlaySound("sonidos/tada.wav",winsound.SND_FILENAME)
                        break
            pygame.display.flip()
  


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
            num_fila = fuente.render(str(i), True, c.BLANCO)
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
'''
condicion = True
while (condicion):
    mi_juego = Juego()
    mi_juego.iniciar_juego()
    mi_juego.jugar()
    condicion = mi_juego.jugar_otra_vez()
'''
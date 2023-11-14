import pygame
import sys
import numpy as np
import random
import winsound
from Clases import Tablero
from icecream import ic
import constantes as c

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
    
def main():
    condicion = True
    while (condicion):
        mi_juego = Juego()
        mi_juego.iniciar_juego()
        mi_juego.jugar()
        condicion = mi_juego.jugar_otra_vez()

if __name__ == "__main__":
        main()
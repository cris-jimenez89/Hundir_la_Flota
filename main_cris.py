
import numpy as np
import random
import winsound
from icecream import ic

class Tablero:
    
    def __init__(self) -> None:
        self.numero_impactos 
        self.tablero_barcos 
        self.tablero_jugadas 
        self.posiciones 
        self.tipos_barcos 
        self.posiciones_probadas 
        
 def pintar_tablero_jugadas(self):
        '''Imprime el tablero de las jugadas realizadas para poder visualizarlas
        Entrada: No tiene parametros
        Salida: No tiene salidas'''
        ic("Para pintar el tablero de las jugadas realizadas")
        print("Tablero de jugadas")
        for filas in range(10):
            for columnas in range(10):
                print(self.tablero_jugadas[filas][columnas], end = " ")
            print(" ")
           


        
    

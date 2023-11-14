
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
            

    def pintar_tablero_jugadas(self):
        '''Imprime el tablero de las jugadas realizadas para poder visualizarlas
        Entrada: No tiene parametros
        Salida: No tiene salidas
        Relacion con otros metodos: con el metodo DEF PINTAR_RESULTADO_DISPARO, que actualiza el tablero de jugadas '''
        ic("Para pintar el tablero de las jugadas realizadas")
        print("Tablero de jugadas")
        for filas in range(10):
            for columnas in range(10):
                print(self.tablero_jugadas[filas][columnas],end = " ")
            print(" ")     
        
    
    def disparar(self):
        '''Realiza un disparo en el juego, en un primer momento de forma aleatoria
        Entrada: No tiene
        Return: Posicion disparo, coordenadas en filas y columnas, tupla de int''' 
        ic("Disparar de forma aleatoria a un punto del tablero usando random")
        print("Disparamos")
        while True: # Para que se siga ejecutando HASTA QUE ENCUENTRE UNA POSICION QUE NO ESTE EN POSICIONES PROBADAS
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            posicion_disparo = (fila,columna)
            if posicion_disparo not in self.posiciones_probadas:
                self.posiciones_probadas.append(posicion_disparo)
                print(self.posiciones_probadas)
                return posicion_disparo
            else:
                print("Disparo en posición ya marcada")
    
    def disparar_ELEGIDO(self): # O AÑADIR (SELF,FILA, COLUMNA)
        '''Realiza un disparo en el juego, en un primer momento de forma aleatoria
        Entrada: No tiene
        Return: Posicion disparo, coordenadas en filas y columnas, tupla de int''' 
        ic("Disparar, pero esta vez ELIGIENDO COORDENADAS a un punto del tablero")
        print("Disparamos")
        fila = int(input("Por favor, ingrese la fila donde desea efectuar el disparo, entre 0 y 9"))
        columna = int(input("Ahora, ingrese la columna entre 0 y 9, por favor"))
        ic("Importante que las coordenadas esten entre 0 y 9, tanto las filas como las columnas")           
        if 0 <= fila <= 9 and 0 <= columna <= 9:
            posicion_disparo = (fila,columna)
            if posicion_disparo not in self.posiciones_probadas:
                ic("Si los datos ya se probaron anteriormente, estarán en self.posiciones_probadas")
                self.posiciones_probadas.append(posicion_disparo)
                print(self.posiciones_probadas)
                return posicion_disparo
            else:
                print("Disparo en posición ya marcada")
            
        else: 
            ic("HABRA QUE LLAMAR OTRA VEZ A LA FUNCION O USAR UN BUCLE WHILE TRUE")
            print("COORDENADAS ERRONEAS, INGRESE VALORES VALIDOS ENTRE 0 Y 9")
           
    
    def pintar_resultado_disparo(self,resultado):
        '''Marca en el tablero de jugadas el disparo realizado
        Entrada: RESULTADO(tupla): compuesto por una tupla con posicion de fila y columna (x,y)[posicion 0]
        a la que se disparó y con el resultado del disparo("X" SI HAY IMPACTO, "O" SI ES AGUA)[posicion 1]
        Salida: No tiene
        Relacion con otros metodos: Resultado = return de la funcion de metodo DEF RECIBIR_IMPACTO'''
        print("PINTAMOS RESULTADO DISPARO")
        ic("Para pintar resultado del disparo, actualizando asi el tablero de jugadas")
        pos = resultado[0] # Primera posicion de la tupla RESULTADO(fila y columna de resultado)
        fila = pos[0] # Primera posicion en la tupla "pos" (donde se disparó)
        columna = pos[1] # segunda posicion en la tupla "pos" (donde se disparó)
        marca_en_tablero = resultado [1] # X o O
        self.tablero_jugadas[fila][columna] = marca_en_tablero
        
        
    
    def recibir_impacto(self,pos):
        '''Sirve para verificar si hay un barco en esa posición.
         Si hay un barco, marca la posición como tocada (X) y actualiza el número de impactos.
        Si no hay un barco, marca la posición como agua.
        Entrada: POS (UNA TUPLA): Una tupla que contiene las coordenadas (fila, columna) del impacto.
        Salida: Una tupla que contiene la posición del impacto y el resultado del mismo.
            La posición es una tupla (fila, columna) y el resultado es "O" para agua o "X" para impacto.'''
        ic("analizamos resultado de disparo y actualizamos el numero de impactos que quedan para ganar")
        if (self.tablero_barcos[pos[0]][pos[1]] == "~"):
            print("AGUA")
            return (pos,"O")
        else:
            print("TOCADO")
            self.numero_impactos = self.numero_impactos + 1
            print("LLEVAMOS",self.numero_impactos)
            return(pos,"X")



            
        
        

        
    

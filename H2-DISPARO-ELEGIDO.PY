# MODIFICAMOS EL METODO DE DISPARO, PARA PODER ELEGIR COORDENADAS (podemos o bien poner 
# que las introduzca por inputs o como argumentos en el metodo (self,fila,columna))
def disparar_ELEGIDO(self): # O AÑADIR (SELF,FILA, COLUMNA)
        '''Realiza un disparo en el juego, en un primer momento de forma aleatoria
        Entrada: No tiene
        Return: Posicion disparo, coordenadas en filas y columnas, tupla de int''' 
        ic("Disparar, pero esta vez ELIGIENDO COORDENADAS a un punto del tablero")
        print("Disparamos")
    while True:
        try:
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
                        print("COORDENADAS ERRONEAS, INGRESE VALORES VALIDOS ENTRE 0 Y 9")
            
        except ValueError: 
            print("Por favor, ingrese valores numericos")

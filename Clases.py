import numpy as np
import random
import winsound
import icecream as ic
import constantes as c


class Tablero:
    
    def __init__(self) -> None:
        self.TAM = c.TAM 
        self.numero_impactos = 0 
        self.tablero_barcos  = np.array([["~" for i in range(c.TAM)] for j in range(c.TAM)])
        self.tablero_jugadas = np.array([["~" for i in range(c.TAM)] for j in range(c.TAM)])
        self.posiciones_fijas = [[(0,2)],[(1,1)],[(3,6)],[(9,5)],
                      [(2,7),(2,8)],[(3,3),(3,4)],[(5,5),(6,5)],
                      [(7,0),(8,0),(9,0)],[(6,8),(7,8),(8,8)],
                      [(8,2),(8,3),(8,4),(8,5)]]
        self.posiciones = []
        self.tipos_barcos = {1:4,2:3,3:2,4:1}
        self.posiciones_probadas = []
        self.posicionesEnemigas = [] 
        self.listaPosicionesHundidas = []
        self.listaposiciones = []  # Lista de tuplas, todas las B que hay en el tablero
    

    
    def pintar_tablero_barcos(self):
        '''
        Imprime el tablero donde van a situarse los barcos
        '''
        #ic("Pintar el tablero barcos")
        print("Tablero barcos")
        for filas in range(10):
            for columnas in range(10):
                print(self.tablero_barcos[filas][columnas],end =" ")
            print(" ")

    # NOS HA SERVIDO PARA CUANDO TENIAMOS POSICIONES FIJOS, PARA ULTIMOS HITOS YA NO SIRVE
    def colocar_barcos(self): 
        '''
        Colocamos los barcos en el tablero barcos
        '''
        #ic("Colocar los barcos")
        print("Colocar barcos")
        for i in self.posiciones_fijas:
            self.pintar_barco(i)

        
    def pintar_barco(self,posiciones):
        '''
        Pintamos una B donde haya una posición de barco
        '''
        #ic("Pintar barco")
        print("Pintar barco")
        for i in posiciones:
            posx = i[0]
            posy = i[1]
            self.tablero_barcos[posx][posy] = "B"

    def colocar_barco_aleatorio_o_elegido(self):
        '''Método para colocar los barcos en el tablero barcos tras elegir posicion
        o tras generarlos de forma aleatoria
        Input: No tiene
        Output:No tiene, sirve para pintar los barcos tras  generar sus posiciones
        Relacion con otros métodos: Depende directamente del método def pintar_barco() y se sirve del atributo 
        de clase Tablero SELF.POSICIONES para colocarlos en el tablero de los barcos'''
        #ic("Colocar los barcos")
        print("Colocar barcos")
        for i in self.posiciones:
            self.pintar_barco(i)

    # NUEVOS METODOS PARA LA COLOCACION DE BARCOS


    def colocar_barco_aleatorio_o_elegido(self):
        '''Método para colocar los barcos en el tablero barcos tras elegir posicion
        Input: No tiene
        Output:No tiene, sirve para pintar los barcos tras  generar sus posiciones
        Relacion con otros métodos: Depende directamente del método def pintar_barco() y se sirve del atributo 
        de clase Tablero SELF.POSICIONES para colocarlos en el tablero de los barcos'''
        #ic("Colocar los barcos")
        print("Colocar barcos")
        for i in self.posiciones:
            self.pintar_barco(i)

    def generar_barco_elegido(self,tamanio,direccion):
        '''Genera los barcos
        Entradas: tamanio: Tamaño del barco.
        direccion: Dirección en la que se generará el barco.
        Salidas:No tiene salidas explícitas, ya que simplemente actualiza las listas de posiciones (self.posiciones y self.listaposiciones).
        Relaciones:Utiliza el tamaño del barco y la dirección para generar posiciones elegidas por el jugador que se almacenan en self.posiciones.
        Actualiza self.listaposiciones con las nuevas posiciones generadas.'''
    
<<<<<<< HEAD
        if (tamanio == 1):
=======
    if (tamanio == 1):
        while True:
            posx = int(input("Introduce posición x (0-9): "))
            posy = int(input("Introduce posición y (0-9): "))
            if 0<= posx <=9 and 0<= posy <=9:
                break
        if((posx,posy) not in self.listaposiciones):
            self.posiciones.append([(posx,posy)])
            self.listaposiciones.append((posx,posy))
            return [self.posiciones,self.listaposiciones]
    elif(tamanio == 2):
        while True:
            posx = int(input("Introduce posición x (1-8): "))
            posy = int(input("Introduce posición y (1-8): "))
            if 1<= posx <=8 and 1<= posy <=8:
                break
        if(direccion == 'n'):
            posx2 = posx - 1
            posy2 = posy
        elif(direccion == 's'):
            posx2 = posx + 1
            posy2 = posy
        elif(direccion == 'e'):
            posx2 = posx
            posy2 = posy + 1
        else:
            posx2 = posx
            posy2 = posy - 1
        if((posx,posy) not in self.listaposiciones and (posx2,posy2) not in self.listaposiciones):
            self.posiciones.append([(posx,posy),(posx2,posy2)])
            self.listaposiciones.append((posx,posy))
            self.listaposiciones.append((posx2,posy2))
            return [self.posiciones,self.listaposiciones]
    elif (tamanio == 3):
        while True:
            posx = int(input("Introduce posición x (2-7): "))
            posy = int(input("Introduce posición y (2-7): "))
            if 2<= posx <=7 and 2<= posy <=7:
                break
        if(direccion == 'n'):
            posx2 = posx - 1
            posy2 = posy
            posx3 = posx - 2
            posy3 = posy
        elif(direccion == 's'):
            posx2 = posx + 1
            posy2 = posy
            posx3 = posx + 2
            posy3 = posy
        elif(direccion == 'e'):
            posx2 = posx
            posy2 = posy + 1
            posx3 = posx
            posy3 = posy + 2
        else:
            posx2 = posx
            posy2 = posy - 1
            posx3 = posx
            posy3 = posy - 2
        if((posx,posy) not in self.listaposiciones
            and (posx2,posy2) not in self.listaposiciones
            and (posx3,posy3) not in self.listaposiciones):
            self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3)])
            self.listaposiciones.append((posx,posy))
            self.listaposiciones.append((posx2,posy2))
            self.listaposiciones.append((posx3,posy3))
            return [self.posiciones,self.listaposiciones]
    else:
        while True:
            posx = int(input("Introduce posición x (3-6): "))
            posy = int(input("Introduce posición y (3-6): "))
            if 3<= posx <=6 and 3<= posy <=6:
                break
        if(direccion == 'n'):
            posx2 = posx - 1
            posy2 = posy
            posx3 = posx - 2
            posy3 = posy
            posx4 = posx - 3
            posy4 = posy
        elif(direccion == 's'):
            posx2 = posx + 1
            posy2 = posy
            posx3 = posx + 2
            posy3 = posy
            posx4 = posx + 3
            posy4 = posy
        elif(direccion == 'e'):
            posx2 = posx
            posy2 = posy + 1
            posx3 = posx
            posy3 = posy + 2
            posx4 = posx
            posy4 = posy + 3
        else:
            posx2 = posx
            posy2 = posy - 1
            posx3 = posx
            posy3 = posy - 2
            posx4 = posx
            posy4 = posy - 3
        if((posx,posy) not in self.listaposiciones
            and (posx2,posy2) not in self.listaposiciones
            and (posx3,posy3) not in self.listaposiciones
            and (posx4,posy4) not in self.listaposiciones):
            self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3),(posx4,posy4)])
            self.listaposiciones.append((posx,posy))
            self.listaposiciones.append((posx2,posy2))
            self.listaposiciones.append((posx3,posy3))
            self.listaposiciones.append((posx4,posy4))
            return[self.posiciones,self.listaposiciones]
            
def generar_flota_elegida(self):
    '''
    Genera la flota que elija el jugador
    Input: No tiene
    Output: No tiene salidas, solo introduce en self.posiciones y self.listas posiciones los barcos que se necesitan
    Relacion con otros metodos: Utiliza el diccionario self.tipos_barcos que contiene información sobre el tamaño y la cantidad de cada tipo de barco.
    Llama al método generar_barco_elegido para cada tipo de barco y dirección elegida, lo que afecta las listas de posiciones (self.posiciones y self.listaposiciones).
    Imprime las posiciones de los barcos y las listas de posiciones después de generar cada barco.
    '''
    for i in self.tipos_barcos.keys():
        for j in range(self.tipos_barcos[i]):
>>>>>>> 428cf7272578ad0c25fb64295e33cbe62d78f4fe
            while True:
                posx = int(input("Introduce posición x (0-9): "))
                posy = int(input("Introduce posición y (0-9): "))
                if 0<= posx <=9 and 0<= posy <=9:
                    break
            if((posx,posy) not in self.listaposiciones):
                self.posiciones.append([(posx,posy)])
                self.listaposiciones.append((posx,posy))
                return [self.posiciones,self.listaposiciones]
        elif(tamanio == 2):
            while True:
                posx = int(input("Introduce posición x (1-8): "))
                posy = int(input("Introduce posición y (1-8): "))
                if 1<= posx <=8 and 1<= posy <=8:
                    break
            if(direccion == 'n'):
                posx2 = posx - 1
                posy2 = posy
            elif(direccion == 's'):
                posx2 = posx + 1
                posy2 = posy
            elif(direccion == 'e'):
                posx2 = posx
                posy2 = posy + 1
            else:
                posx2 = posx
                posy2 = posy - 1
            if((posx,posy) not in self.listaposiciones and (posx2,posy2) not in self.listaposiciones):
                self.posiciones.append([(posx,posy),(posx2,posy2)])
                self.listaposiciones.append((posx,posy))
                self.listaposiciones.append((posx2,posy2))
                return [self.posiciones,self.listaposiciones]
        elif (tamanio == 3):
            while True:
                posx = int(input("Introduce posición x (2-7): "))
                posy = int(input("Introduce posición y (2-7): "))
                if 2<= posx <=7 and 2<= posy <=7:
                    break
            if(direccion == 'n'):
                posx2 = posx - 1
                posy2 = posy
                posx3 = posx - 2
                posy3 = posy
            elif(direccion == 's'):
                posx2 = posx + 1
                posy2 = posy
                posx3 = posx + 2
                posy3 = posy
            elif(direccion == 'e'):
                posx2 = posx
                posy2 = posy + 1
                posx3 = posx
                posy3 = posy + 2
            else:
                posx2 = posx
                posy2 = posy - 1
                posx3 = posx
                posy3 = posy - 2
            if((posx,posy) not in self.listaposiciones
                and (posx2,posy2) not in self.listaposiciones
                and (posx3,posy3) not in self.listaposiciones):
                self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3)])
                self.listaposiciones.append((posx,posy))
                self.listaposiciones.append((posx2,posy2))
                self.listaposiciones.append((posx3,posy3))
                return [self.posiciones,self.listaposiciones]
        else:
            while True:
                posx = int(input("Introduce posición x (3-6): "))
                posy = int(input("Introduce posición y (3-6): "))
                if 3<= posx <=6 and 3<= posy <=6:
                    break
            if(direccion == 'n'):
                posx2 = posx - 1
                posy2 = posy
                posx3 = posx - 2
                posy3 = posy
                posx4 = posx - 3
                posy4 = posy
            elif(direccion == 's'):
                posx2 = posx + 1
                posy2 = posy
                posx3 = posx + 2
                posy3 = posy
                posx4 = posx + 3
                posy4 = posy
            elif(direccion == 'e'):
                posx2 = posx
                posy2 = posy + 1
                posx3 = posx
                posy3 = posy + 2
                posx4 = posx
                posy4 = posy + 3
            else:
                posx2 = posx
                posy2 = posy - 1
                posx3 = posx
                posy3 = posy - 2
                posx4 = posx
                posy4 = posy - 3
            if((posx,posy) not in self.listaposiciones
                and (posx2,posy2) not in self.listaposiciones
                and (posx3,posy3) not in self.listaposiciones
                and (posx4,posy4) not in self.listaposiciones):
                self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3),(posx4,posy4)])
                self.listaposiciones.append((posx,posy))
                self.listaposiciones.append((posx2,posy2))
                self.listaposiciones.append((posx3,posy3))
                self.listaposiciones.append((posx4,posy4))
                return[self.posiciones,self.listaposiciones]
            
    def generar_flota_elegida(self):
        '''
        Genera la flota que elija el jugador
        Input: No tiene
        Output: No tiene salidas, solo introduce en self.posiciones y self.listas posiciones los barcos que se necesitan
        Relacion con otros metodos: Utiliza el diccionario self.tipos_barcos que contiene información sobre el tamaño y la cantidad de cada tipo de barco.
        Llama al método generar_barco_elegido para cada tipo de barco y dirección elegida, lo que afecta las listas de posiciones (self.posiciones y self.listaposiciones).
        Imprime las posiciones de los barcos y las listas de posiciones después de generar cada barco.
        '''
        for i in self.tipos_barcos.keys():
            for j in range(self.tipos_barcos[i]):
                while True:
                    print("barco ",j+1,"tamaño ",i)
                    direccion = input("Seleccione una dirección para el barco n/s/e/o")
                    if direccion=="n" or direccion=="s" or direccion=="e" or direccion=="o":
                        break
                tamanio = i
                res= self.generar_barco_elegido(tamanio,direccion)
                self.posiciones = res[0]
                self.listaposiciones = res[1]

    def generar_barco_aleatorio(self,tamanio,direccion):
        '''Genera los barcos
        Entradas: tamanio: Tamaño del barco.
        direccion: Dirección en la que se generará el barco.
        Salidas:No tiene salidas explícitas, ya que simplemente actualiza las listas de posiciones (self.posiciones y self.listaposiciones).
        Relaciones con otros metodos:Utiliza el tamaño del barco y la dirección para generar posiciones aleatorias que se almacenan en self.posiciones.
        Actualiza self.listaposiciones con las nuevas posiciones generadas.'''
    
        if (tamanio == 1):
            while True:
                posx = random.randint(0,9)
                posy = random.randint(0,9)
                if((posx,posy) not in self.listaposiciones):
                    self.posiciones.append([(posx,posy)])
                    self.listaposiciones.append((posx,posy))
                    return [self.posiciones,self.listaposiciones]
        elif(tamanio == 2):
            while True:
                posx = random.randint(1,8)
                posy = random.randint(1,8)
                if(direccion == 'n'):
                    posx2 = posx - 1
                    posy2 = posy
                elif(direccion == 's'):
                    posx2 = posx + 1
                    posy2 = posy
                elif(direccion == 'e'):
                    posx2 = posx
                    posy2 = posy + 1
                else:
                    posx2 = posx
                    posy2 = posy - 1
                if((posx,posy) not in self.listaposiciones and (posx2,posy2) not in self.listaposiciones):
                    self.posiciones.append([(posx,posy),(posx2,posy2)])
                    self.listaposiciones.append((posx,posy))
                    self.listaposiciones.append((posx2,posy2))
                    return [self.posiciones,self.listaposiciones]
        elif (tamanio == 3):
            while True:
                posx = random.randint(2,7)
                posy = random.randint(2,7)
                if(direccion == 'n'):
                    posx2 = posx - 1
                    posy2 = posy
                    posx3 = posx - 2
                    posy3 = posy
                elif(direccion == 's'):
                    posx2 = posx + 1
                    posy2 = posy
                    posx3 = posx + 2
                    posy3 = posy
                elif(direccion == 'e'):
                    posx2 = posx
                    posy2 = posy + 1
                    posx3 = posx
                    posy3 = posy + 2
                else:
                    posx2 = posx
                    posy2 = posy - 1
                    posx3 = posx
                    posy3 = posy - 2
                if((posx,posy) not in self.listaposiciones
                    and (posx2,posy2) not in self.listaposiciones
                    and (posx3,posy3) not in self.listaposiciones):
                    self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3)])
                    self.listaposiciones.append((posx,posy))
                    self.listaposiciones.append((posx2,posy2))
                    self.listaposiciones.append((posx3,posy3))
                    return [self.posiciones,self.listaposiciones]
        else:
            while True:
                posx = random.randint(3,6)
                posy = random.randint(3,6)
                if(direccion == 'n'):
                    posx2 = posx - 1
                    posy2 = posy
                    posx3 = posx - 2
                    posy3 = posy
                    posx4 = posx - 3
                    posy4 = posy
                elif(direccion == 's'):
                    posx2 = posx + 1
                    posy2 = posy
                    posx3 = posx + 2
                    posy3 = posy
                    posx4 = posx + 3
                    posy4 = posy
                elif(direccion == 'e'):
                    posx2 = posx
                    posy2 = posy + 1
                    posx3 = posx
                    posy3 = posy + 2
                    posx4 = posx
                    posy4 = posy + 3
                else:
                    posx2 = posx
                    posy2 = posy - 1
                    posx3 = posx
                    posy3 = posy - 2
                    posx4 = posx
                    posy4 = posy - 3
                if((posx,posy) not in self.listaposiciones
                    and (posx2,posy2) not in self.listaposiciones
                    and (posx3,posy3) not in self.listaposiciones
                    and (posx4,posy4) not in self.listaposiciones):
                    self.posiciones.append([(posx,posy),(posx2,posy2),(posx3,posy3),(posx4,posy4)])
                    self.listaposiciones.append((posx,posy))
                    self.listaposiciones.append((posx2,posy2))
                    self.listaposiciones.append((posx3,posy3))
                    self.listaposiciones.append((posx4,posy4))
                    return[self.posiciones,self.listaposiciones]
            
    def generar_flota_random(self):
        ''' Genera la flota de forma aleatoria
        Input: No tiene
        Output: No tiene salidas, solo introduce en self.posiciones y self.listas posiciones los barcos que se necesitan
        Relacion con otros metodos: Utiliza el diccionario self.tipos_barcos que contiene información sobre el tamaño y la cantidad de cada tipo de barco.
        Llama al método generar_barco_aleatorio para cada tipo de barco y dirección aleatoria, lo que afecta las listas de posiciones (self.posiciones y self.listaposiciones).
        Imprime las posiciones de los barcos y las listas de posiciones después de generar cada barco.'''
        for i in self.tipos_barcos.keys():
            for j in range(self.tipos_barcos[i]):
                direccion = random.choices(['n','s','e','o'])
                tamanio = i
                res= self.generar_barco_aleatorio(tamanio,direccion)
                self.posiciones = res[0]
                self.listaposiciones = res[1]
       



    def estado_jugador(self):
        '''
        Jugador vivo o muerto
        '''
        #ic("Estado jugador")
        print("Estado jugador")
        vivo=True
        if self.numero_impactos==20:
            vivo=False
            return vivo
        return vivo


    def pintar_tablero_jugadas(self):
        '''
        Imprime el tablero de las jugadas realizadas para poder visualizarlas
        Entrada: No tiene parametros
        Salida: No tiene salidas
        Relacion con otros metodos: con el metodo DEF PINTAR_RESULTADO_DISPARO, que actualiza el tablero de jugadas
        '''
        #ic("Para pintar el tablero de las jugadas realizadas")
        print("Tablero de jugadas")
        for filas in range(10):
            for columnas in range(10):
                print(self.tablero_jugadas[filas][columnas],end = " ")
            print(" ")     
        
    
    def disparar(self):
        '''
        Realiza un disparo en el juego, en un primer momento de forma aleatoria
        Entrada: No tiene
        Return: Posicion disparo, coordenadas en filas y columnas, tupla de int
        ''' 
        #ic("Disparar de forma aleatoria a un punto del tablero usando random")
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
        '''
        Realiza un disparo en el juego, en un primer momento de forma aleatoria
        Entrada: No tiene
        Return: Posicion disparo, coordenadas en filas y columnas, tupla de int
        ''' 
        #ic("Disparar, pero esta vez ELIGIENDO COORDENADAS a un punto del tablero")
        print("Disparamos")
        while True:
            try:
                fila = int(input("Por favor, ingrese la fila donde desea efectuar el disparo, entre 0 y 9:"))
                columna = int(input("Ahora, ingrese la columna entre 0 y 9, por favor:"))
                #ic("Importante que las coordenadas esten entre 0 y 9, tanto las filas como las columnas")           
                if 0 <= fila <= 9 and 0 <= columna <= 9:
                    posicion_disparo = (fila,columna)
                    if posicion_disparo not in self.posiciones_probadas:
                        #ic("Si los datos ya se probaron anteriormente, estarán en self.posiciones_probadas")
                        self.posiciones_probadas.append(posicion_disparo)
                        print(self.posiciones_probadas)
                        return posicion_disparo
                    else:
                        print("Disparo en posición ya marcada")
            
                else: 
                    #ic("HABRIA QUE LLAMAR OTRA VEZ A LA FUNCION, PERO USAMOS MEJOR UN BUCLE WHILE TRUE PARA QUE NO PARE DE BUSCAR COORDENADAS HASTA QUE SEAN VALIDAS")
                    print("COORDENADAS ERRONEAS, INGRESE VALORES VALIDOS ENTRE 0 Y 9")
            except Exception:
                pass
           
    
    def pintar_resultado_disparo(self,resultado):
        '''
        Marca en el tablero de jugadas el disparo realizado
        Entrada: RESULTADO(tupla): compuesto por una tupla con posicion de fila y columna (x,y)[posicion 0]
        a la que se disparó y con el resultado del disparo("X" SI HAY IMPACTO, "O" SI ES AGUA)[posicion 1]
        Salida: No tiene
        Relacion con otros metodos: Resultado = return de la funcion de metodo DEF RECIBIR_IMPACTO
        '''
        print("PINTAMOS RESULTADO DISPARO")
        #ic("Para pintar resultado del disparo, actualizando asi el tablero de jugadas")
        pos = resultado[0] # Primera posicion de la tupla RESULTADO(fila y columna de resultado)
        fila = pos[0] # Primera posicion en la tupla "pos" (donde se disparó)
        columna = pos[1] # segunda posicion en la tupla "pos" (donde se disparó)
        marca_en_tablero = resultado [1] # X o O
        self.tablero_jugadas[fila][columna] = marca_en_tablero
        
        
    
    def recibir_impacto(self,pos):
        '''
        Sirve para verificar si hay un barco en esa posición.
        Si hay un barco, marca la posición como tocada (X) y actualiza el número de impactos.
        Si no hay un barco, marca la posición como agua.
        Entrada: POS (UNA TUPLA): Una tupla que contiene las coordenadas (fila, columna) del impacto.
        Salida: Una tupla que contiene la posición del impacto y el resultado del mismo.
        La posición es una tupla (fila, columna) y el resultado es "O" para agua o "X" para impacto.
        '''
        #ic("analizamos resultado de disparo y actualizamos el numero de impactos que quedan para ganar")
        if (self.tablero_barcos[pos[0]][pos[1]] == "~"):
            print("AGUA")
            winsound.PlaySound('sonidos/splash.wav',winsound.SND_FILENAME)
            return (pos,"O")
        else:
            print("TOCADO")
            winsound.PlaySound('sonidos/explosion.wav',winsound.SND_FILENAME)
            self.numero_impactos = self.numero_impactos + 1
            print("LLEVAMOS",self.numero_impactos)
            return(pos,"X")

    

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
        
        for i in posiciones_cercanas:
            if(posx == i[0]):
                posiciones_cercanas_h.append(i)
        
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
        posy = impacto1[1]
        for i in posiciones_cercanas:
            if(posy == i[1]):
                posiciones_cercanas_v.append(i)
            
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
               posiciones_cercanas1 = self.posiciones_cerca_impacto(impacto1)
               posiciones_cercanas2 = self.posiciones_cerca_impacto(impacto2)
               posiciones_cercanas = posiciones_cercanas1 + posiciones_cercanas2
               if(direccion == 'n'):
                   return self.disparar_random()
               elif(direccion == 'h'):
                   return self.disparar_cerca_dir_h(posiciones_cercanas,impacto1)
               else:
                   return self.disparar_cerca_dir_v(posiciones_cercanas,impacto1)

import pygame
import sys
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
        self.barcos_colocados = []
        self.nivel_dificultad = 0
    
    def elegir_nivel(self):
        '''
        Da a elegir el nivel de dificultad (0,1)
        El nivel 0 es el juego normal, el jugador cpu dispara random
        El nivel 1 el jugador cpu realiza disparos mas inteligentes y el jugador 1 en sus turnos
        puede decidir que hacer: disparar, salir de la partida o ver sus barcos
        output: nivel: int (0 ó 1)
        '''
        while True:
            try:
                nivel = int(input("seleccione el nivel (0 ó 1)"))
                if nivel == 0 or nivel == 1:
                    return nivel
                else:
                    print("entrada invalida, introduzca 0 ó 1")
            except Exception:
                pass

    def elegir_metodo_colocacion(self):
        '''Metodo para elegir el tipo de colocacion que deseamos para nuestros barcos.
        Input: No tiene
        Output: opcion elegida, dato int'''
        while True:
            try:
                print("Por favor, Elige un método de colocación:")
                print("1. Aleatorio")
                print("2. Posiciones fijas")
                print("3. Posiciones elegidas por jugador")
                opcion = int(input("Ingresa el número de la opción elegida: "))
                if opcion == 1 or opcion == 2 or opcion == 3:
                    return opcion
            except:
                pass

    def iniciar_juego(self):
        '''
        Genera la flota para ambos jugadores
        Aqui tambien podra influir el nivel
        relacion: 
        '''
        #ic("Para elegir nivel de dificultad deseado")
        self.nivel_dificultad = self.elegir_nivel()
        #ic("Para que jugador 1 elija que tipo de metodo usará para colocar los barcos")
        opcion_colocacion = self.elegir_metodo_colocacion()
        if opcion_colocacion == 1:
            self.jugador1.generar_flota_random()# Posiciones aleatorias
            self.jugador1.colocar_barco_aleatorio_o_elegido()
            self.jugador2.generar_flota_random()# Posiciones aleatorias
            self.jugador2.colocar_barco_aleatorio_o_elegido()
        elif opcion_colocacion == 2:
            self.jugador1.colocar_barcos()# Posiciones fijas
            self.jugador2.colocar_barcos() # Posiciones fijas            
        elif opcion_colocacion == 3:
            self.jugador1.generar_flota_elegida() # Posicion elegida
            self.jugador1.colocar_barco_aleatorio_o_elegido() 
            self.jugador2.generar_flota_random()# Posiciones aleatorias
            self.jugador2.colocar_barco_aleatorio_o_elegido()
            
        else:
            print("Opción no válida.")
            return

             

    def elegir_opcion_en_turno(self):
        '''
        Ofrece un menu de opcion al jugador para que elija
            1- Ejecutar disparo
            2- Salir de la partida
            3- Mostrar mis barcos'''
        while True:
            try:
                print("MENU")
                print("1- Ejecutar disparo")
                print("2- Salir de la partida")
                print("3- Mostrar mis barcos")
                opcion = int(input("seleccione opcion (1, 2 ó 3)"))
                if opcion == 1 or opcion == 2 or opcion == 3:
                    return opcion
                else:
                    print("entrada invalida, introduzca 1,2 ó 3")
            except Exception:
                pass


    def ejecutar_disparo_en_turno_jugador(self):
        '''
        Efectua las acciones del turno disparar. Devuelve al final el truno del siguiente en jugar
        1 si le vuelve a tocar a el por haber realizado un disparo exitoso previo
        2 si falla el tiro
        3 si acierta y gana la partida
        output: int (1,2 ó 3)'''
        
        #ic("Empieza J1, DISPARO A JUGADOR 2")
        print("J1 dispara")
        disparoJ1 = self.jugador1.disparar_ELEGIDO() # Usamos funcion def disparar_ELEGIDO() contra J2(ACTUALIZACION)
        print("DISPARO A ", disparoJ1)
        resultado = self.jugador2.recibir_impacto(disparoJ1)
        #ic("USAMOS LA POSICION DEL DISPARO PARA COMPROBAR SI HA HABIDO IMPACTO EN EL TABLERO DE J2")
        self.jugador1.pintar_resultado_disparo(resultado)
        #ic("Actualizamos resultado de disparo en tablero de jugadas")
        self.jugador1.pintar_tablero_jugadas()
        self.listaPosicionesHundidas2 = self.jugador2.listaPosicionesHundidas
        self.dibujar_tablero(self.jugador1.tablero_jugadas,self.listaPosicionesHundidas2 ,c.MARGEN, 50, "Tablero 1")
        self.dibujar_tablero(self.jugador2.tablero_jugadas,self.listaPosicionesHundidas1 ,c.ANCHO - c.TAM_CASILLA * 10 - c.MARGEN, 50, "Tablero 2") 
        if (resultado[1] == "X"): # DISPARO POSITIVO, O TENEMOS OTRO TURNO O PODEMOS HABER GANADO
            vivo = self.jugador2.estado_jugador()
            #ic("PRIMERO CONFIRMAMOS SI HEMOS GANADO, SI HEMOS DADO LOS IMPACTOS SUFICIENTES")
            if not vivo:
                print("J1 HA GANADO, ¡¡FELICIDADES!!")
                winsound.PlaySound("sonidos/tada.wav",winsound.SND_FILENAME)
                return 3
            else:
                print("J1 ha impactado, le toca nuevamente")
                #ic("El bucle del turno de jugador 1 se reinicia, volvemos a turno 1")
                return 1
        else:
            #ic("Cambiamos de turno para que le toque al otro jugador")
            return 2

    def ejecutar_disparo_en_turno_cpu(self):       
        '''
        Efectua las acciones del turno disparar. Devuelve al final el truno del siguiente en jugar
        1 si le vuelve a tocar a el por haber realizado un disparo exitoso previo
        2 si falla el tiro
        3 si acierta y gana la partida
        output: int (1,2 ó 3)
        '''
        #ic("TURNO DE J2")
        print("J2 dispara")
        if(self.nivel_dificultad == 0):
            disparoJ2 = self.jugador2.disparar_random()
        else:    
            disparoJ2 = self.jugador2.disparar_cpu_inteligente()
        print("DISPARO A", disparoJ2)
        resultado2 = self.jugador1.recibir_impacto(disparoJ2)
        #ic("USAMOS LA POSICION DEL DISPARO PARA COMPROBAR SI HA IMPACTADO EN EL TABLERO DE J1")
        self.jugador2.pintar_resultado_disparo(resultado2)
        #ic("Actualizamos resultado de disparo en tablero de jugadas")
        self.jugador2.pintar_tablero_jugadas()
        self.listaPosicionesHundidas1 = self.jugador1.listaPosicionesHundidas
        # Dibujar tableros
        self.dibujar_tablero(self.jugador1.tablero_jugadas, self.listaPosicionesHundidas2,c.MARGEN, 50, "Tablero 1")
        self.dibujar_tablero(self.jugador2.tablero_jugadas, self.listaPosicionesHundidas1,c.ANCHO - c.TAM_CASILLA * 10 - c.MARGEN, 50, "Tablero 2")
        if(resultado2[1] == "X"): # Si hemos impactado
            vivo = self.jugador1.estado_jugador()
            #ic("PRIMERO CONFIRMAMOS SI HEMOS GANADO, SI HEMOS DADO LOS IMPACTOS SUFICIENTES")
            if not vivo:
                print("J2 HA GANADO, ¡¡FELICIDADES!!")
                winsound.PlaySound("sonidos/tada.wav",winsound.SND_FILENAME)
                return 3
            else:
                print("J2 ha impactado, le toca nuevamente")
                #ic("Si no hemos ganado, vuelve a tocarle al turno = 2")
                return 2
        else:
            return 1

    def jugar(self):
        '''
        En el tiene lugar la logica del juego controlando el turno y las
        acciones de los jugadores
        relacion: jugador.disparar, jugador.marcar_resultado_disparo,
                  pintar_tablero1, comprobar_estado_derrotado,
                  pintar_taablero2, winsound.Playsound,
                  dibujar_tablero
        '''
        salir = False
        turno = 1
        while not salir:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            self.pantalla.fill(c.BLANCO)
            
            if ( turno == 1):
                
                if(self.nivel_dificultad == 1):
                    opcion = self.elegir_opcion_en_turno()
                    if(opcion == 1):
                        turno = self.ejecutar_disparo_en_turno_jugador()
                        if(turno == 3):
                            salir = True
                            break
                    elif(opcion == 2):
                        salir = True
                        break
                    else:
                        self.dibujar_tablero(self.jugador1.tablero_barcos,self.listaPosicionesHundidas2 ,c.MARGEN, 50, "Tablero 1")
                        self.dibujar_tablero(self.jugador2.tablero_jugadas,self.listaPosicionesHundidas1 ,c.ANCHO - c.TAM_CASILLA * 10 - c.MARGEN, 50, "Tablero 2")
                        self.jugador1.pintar_tablero_barcos()
                        pygame.display.flip()
                else:
                    turno = self.ejecutar_disparo_en_turno_jugador()
            else:
                turno = self.ejecutar_disparo_en_turno_cpu()
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




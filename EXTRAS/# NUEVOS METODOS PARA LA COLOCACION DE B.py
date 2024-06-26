# NUEVOS METODOS PARA LA COLOCACION DE BARCOS
import random
class Tablero:
    def __init__(self):
        self.posiciones = []  # Contiene las posiciones relacionadas
        self.listaposiciones = []  # Lista de tuplas, todas las B que hay en el tablero
        self.tipos_barcos = {1: 4, 2: 3, 3: 2, 4: 1}

def colocar_barco_aleatorio_o_elegido(self):
    '''Método para colocar los barcos en el tablero barcos tras elegir posicion
    o tras generarlos de forma aleatoria
    Input: No tiene
    Output:No tiene, sirve para pintar los barcos tras  generar sus posiciones
    Relacion con otros métodos: Depende directamente del método def pintar_barco() y se sirve del atributo 
    de clase Tablero SELF.POSICIONES para colocarlos en el tablero de los barcos'''
    ic("Colocar los barcos")
    print("Colocar barcos")
    for i in self.posiciones:
        self.pintar_barco(i)

def generar_barco_aleatorio(self,tamanio,direccion):
    '''Genera los barcos
    Entradas: tamanio: Tamaño del barco.
    direccion: Dirección en la que se generará el barco.
    Salidas:No tiene salidas explícitas, ya que simplemente actualiza las listas de posiciones (self.posiciones y self.listaposiciones).
    Relaciones:Utiliza el tamaño del barco y la dirección para generar posiciones aleatorias que se almacenan en self.posiciones.
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
            if((posx,posy) not in self.self.listaposiciones
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
    '''
    Genera la flota de forma aleatoria
    Input: No tiene
    Output: No tiene salidas, solo introduce en self.posiciones y self.listas posiciones los barcos que se necesitan
    Relacion con otros metodos: Utiliza el diccionario self.tipos_barcos que contiene información sobre el tamaño y la cantidad de cada tipo de barco.
    Llama al método generar_barco_aleatorio para cada tipo de barco y dirección aleatoria, lo que afecta las listas de posiciones (self.posiciones y self.listaposiciones).
    Imprime las posiciones de los barcos y las listas de posiciones después de generar cada barco.
    '''
    for i in self.tipos_barcos.keys():
        for j in range(self.tipos_barcos[i]):
            direccion = random.choices(['n','s','e','o'])
            tamanio = i
            res= self.generar_barco_aleatorio(tamanio,direccion.self.posiciones,self.listaposiciones)
            self.posiciones = res[0]
            self.listaposiciones = res[1]
           
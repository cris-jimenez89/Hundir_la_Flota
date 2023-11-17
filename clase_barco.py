class Barco: 
    def __init__(self, tamano, posiciones):
        self.tamano = tamano
        self.posiciones = posiciones # POSICIONES DE LOS BARCOS, LAS QUEREMOS ELEGIDAS 
        #PARA EL J1 Y ALEATORIOS PARA LA MAQUINA
        self.estado = [False] * tamano  # Lista que indica si cada parte del barco ha sido impactada

    def esta_hundido(self):
        '''Metodo para confirmar si algun barco está hundido tras disparo, afecta SOLO
        AL BARCO TOCADO,AL OBJETO BARCO CREADO, Y SOLO DEVOLVERA TRUE SI TODAS LAS PARTES DE NUESTRO BARCO IMPACTADO
        SE HAN HUNDIDO
        Input: No tiene
        Output: True or False, dato booleano'''
        return all(self.estado)

    def recibir_impacto(self, posicion):
        '''Metodo para comprobar si le han dado a nuestro barco tras un disparo del enemigo
        Input: posicion del disparo del enemigo, recibida del metodo DISPARAR, tipo de dato TUPLA INT
        Output: True or False, según haya impactado en nuestros barcos o no, dato bool
        Relacion con otros métodos: estará relacionado con el método DEF DISPARAR(), que nos dará donde se ha disparado
        y tambien con donde hemos colocado nosotros los barcos, con el DEF COLOCAR_MANUALMENTE() en caso de 
        J1 y con DEF COLOCAR_ALEATORIO() para J2'''
        for i, pos in enumerate(self.posiciones):# RECURREMOS CON UN ENUMERATE INDICE Y POSICIONES DE NUESTROS BARCOS(EN SELF.POSICIONES)
            if pos == posicion:
                self.estado[i] = True
                return True  # El impacto fue exitoso
        return False  # El impacto no afectó al barco
    
    def validar_coordenada(self, nueva_posicion, otros_barcos):# IMPORTANTE, COMO VER LA LISTA DE OTROS BARCOS YA COLOCADOS, DONDE METERLA??
        '''Valida si es posible colocar el barco en la nueva posición.
        Input:
            - nueva_posicion: La nueva posición a validar (fila, columna).
            - otros_barcos: Una lista de otros barcos en el tablero. VER COMO VISUALIZARLA Y DONDE METER ESTA LISTA!!
        Output:
            - True si es posible colocar el barco, False de lo contrario
        Relacion con otros metodos: Esta relacionado con los metodos DEF COLOCAR_BARCOS()[MANUAL O ALEATORIAMENTE]'''
        for barco in otros_barcos:
            for pos in barco.posiciones:
                if pos == nueva_posicion:
                    return False  # La posición está ocupada por otro barco
        return True  # La posición está disponible para colocar el barco

# METODO PARA COLOCAR LOS BARCOS DE FORMA ALEATORIA, PARA LA MAQUINA
    def colocar_aleatorio(self, tablero_size): 
        '''Coloca el barco de forma aleatoria en el tablero.
        Input: Tamaño del tablero (tupla), tipo de dato tuple (10,10)
        Output: No tiene'''
        orientacion = random.choice(['horizontal', 'vertical'])
        if orientacion == 'horizontal':
            fila = random.randint(0, tablero_size[0] - 1)
            columna = random.randint(0, tablero_size[1] - self.tamano)
            self.posiciones = [(fila, columna + i) for i in range(self.tamano)]
        else:  # orientacion == 'vertical'
            fila = random.randint(0, tablero_size[0] - self.tamano)
            columna = random.randint(0, tablero_size[1] - 1)
            self.posiciones = [(fila + i, columna) for i in range(self.tamano)]

# METODO PARA ELEGIR LA COLOCACION DE LOS BARCOS Y LA ORIENTACION(colocarlo al principio)
    def colocar_manualmente(self, orientacion, posicion_inicial):
        '''Coloca el barco manualmente en el tablero.
        Input:
            - orientacion: La orientación del barco ('norte', 'sur', 'este' u 'oeste').
            - posicion_inicial: La posición inicial del barco (fila, columna), en forma de tupla
        Output: No tiene
        Relacion con otros metodos: con DEF VALIDAR_COORDENADA(), para confirmar que no hay ningun otro barco ahí'''
        if orientacion == 'norte':
            self.posiciones = [(posicion_inicial[0] - i, posicion_inicial[1]) for i in range(self.tamano)]
        elif orientacion == 'sur':
            self.posiciones = [(posicion_inicial[0] + i, posicion_inicial[1]) for i in range(self.tamano)]
        elif orientacion == 'este':
            self.posiciones = [(posicion_inicial[0], posicion_inicial[1] + i) for i in range(self.tamano)]
        elif orientacion == 'oeste':
            self.posiciones = [(posicion_inicial[0], posicion_inicial[1] - i) for i in range(self.tamano)]

# Otro metodo con numpy
    def colocar_manualmente(self, orientacion, posicion_inicial):
        '''Coloca el barco manualmente en el tablero.
        Input:
            - orientacion: La orientación del barco ('norte', 'sur', 'este' u 'oeste'),dato str
            - posicion_inicial: La posición inicial del barco (fila, columna).
        Output: No tiene
        Relacion con otros metodos: Con DEF VALIDAR_COORDENADA(), para confirmar que no hay ningun
        barco ya colocado'''
        direcciones = {'norte': (-1, 0), 'sur': (1, 0), 'este': (0, 1), 'oeste': (0, -1)}
        fila, columna = posicion_inicial
        dy, dx = direcciones[orientacion]

        # Generar las posiciones utilizando NumPy
        posiciones_fila = fila + np.arange(self.tamano) * dy
        posiciones_columna = columna + np.arange(self.tamano) * dx
        self.posiciones = list(zip(posiciones_fila, posiciones_columna))
        
'''Ejemplo de uso
barco = Barco(tamano=3, posiciones=[])  # Inicializas el barco con posiciones vacías
barco.colocar_manualmente(orientacion='norte', posicion_inicial=(5, 5))
print("Posiciones del barco:", barco.posiciones)'''
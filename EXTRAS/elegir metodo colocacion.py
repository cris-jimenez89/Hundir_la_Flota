def elegir_metodo_colocacion(self):
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


# DEF INICIAR_JUEGO()
# TRAS NIVEL DE DIFICULTAD
self.nivel_dificultad = self.elegir_nivel()
opcion_colocacion = self.elegir_metodo_colocacion()
if opcion_colocacion == "1":
            self.generar_flota_random()# Posiciones aleatorias
            self.colocar_barco_aleatorio_o_elegido()
        elif opcion_colocacion == "2":
            self.colocar_barcos()# Posiciones fijas            
        elif opcion_colocacion == "3":
            self.colocar_barcos_fijos() #NOMBRE DE METODO ROCIO# eligiendo nosotros la posicion
            self.colocar_barco_aleatorio_o_elegido()
        else:
            print("Opción no válida.")
            return




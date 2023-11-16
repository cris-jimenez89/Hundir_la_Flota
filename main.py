from Clases import Juego
from icecream import ic
import constantes as c


    
def main():
    condicion = True
    while (condicion):
        mi_juego = Juego()
        mi_juego.iniciar_juego()
        mi_juego.jugar()
        condicion = mi_juego.jugar_otra_vez()

if __name__ == "__main__":
        main()
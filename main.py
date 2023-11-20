from Clases import Juego
    
def main():
    condicion = True
    while (condicion):
        mi_juego = Juego()
        mi_juego.iniciar_juego()
        mi_juego.jugar()
        condicion = mi_juego.jugar_otra_vez()

if __name__ == "__main__":
        main()
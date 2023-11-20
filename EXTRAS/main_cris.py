# CREAMOS EL BUCLE PARA PODER HACER OPERATIVO EL JUEGO 

J1 = Tablero() 
ic("Asignamos tablero vacío a jugador 1")
# SI QUEREMOS VER TABLERO VACIO, DEF PINTAR_TABLERO_BARCOS
J1.pintar_tablero_barcos()
J1.colocar_barcos()
ic("Colocamos los barcos del primer jugador, en primer momento en posiciones fijas")
# SI QUEREMOS VISUALIZAR LAS POSICIONES DE LOS BARCOS, LAS IMPRIMIMOS CON EL METODO PINTAR_TABLERO_BARCOS DE NUEVO
J1.pintar_tablero_barcos()

J2 = Tablero()
ic("Asignamos tablero vacío a jugador 2")
# SI QUEREMOS VER TABLERO VACÍO, DEF PINTAR_TABLERO_BARCOS
J2.pintar_tablero_barcos()
J2.colocar_barcos()
ic("Colocamos los barcos del segundo jugador, en un primer momento en posiciones fijas")
# HACEMOS UN PRINT SI QUEREMOS DEL TABLERO CON LOS BARCOS, CON EL DEF PINTAR_TABLERO_BARCOS DE NUEVO
J2.pintar_tablero_barcos()


turno = 1
while True:
    if ( turno == 1):
        ic("Empieza J1, DISPARO A JUGADOR 2")
        print("J1 dispara")
        disparoJ1 = J1.disparar_ELEGIDO() # Usamos funcion def disparar_ELEGIDO() contra J2(ACTUALIZACION)
        print("DISPARO A ", disparoJ1)
        resultado = J2.recibir_impacto(disparoJ1)
        ic("USAMOS LA POSICION DEL DISPARO PARA COMPROBAR SI HA HABIDO IMPACTO EN EL TABLERO DE J2")
        J1.pintar_resultado_disparo(resultado)
        ic("Actualizamos resultado de disparo en tablero de jugadas")
        J1.pintar_tablero_jugadas() 
        if (resultado[1] == "X"): # DISPARO POSITIVO, O TENEMOS OTRO TURNO O PODEMOS HABER GANADO
            vivo = J2.estado_jugador()
            ic("PRIMERO CONFIRMAMOS SI HEMOS GANADO, SI HEMOS DADO LOS IMPACTOS SUFICIENTES")
            if not vivo:
                print("J1 HA GANADO, ¡¡FELICIDADES!!")
                break
            else:
                print("J1 ha impactado, le toca nuevamente")
                ic("El bucle del turno de jugador 1 se reinicia, volvemos a turno 1")
        else:
            turno = 2
            ic("Cambiamos de turno para que le toque al otro jugador")
       
    else:
        ic("TURNO DE J2")
        print("J2 dispara")
        disparoJ2 = J2.disparar()
        print("DISPARO A", disparoJ2)
        resultado2 = J1.recibir_impacto(disparoJ2)
        ic("USAMOS LA POSICION DEL DISPARO PARA COMPROBAR SI HA IMPACTADO EN EL TABLERO DE J1")
        J2.pintar_resultado_disparo(resultado2)
        ic("Actualizamos resultado de disparo en tablero de jugadas")
        J2.pintar_tablero_jugadas()
        if(resultado2[1] == "X"): # Si hemos impactado
            vivo = J1.estado_jugador()
            ic("PRIMERO CONFIRMAMOS SI HEMOS GANADO, SI HEMOS DADO LOS IMPACTOS SUFICIENTES")
            if not vivo:
                print("J2 HA GANADO, ¡¡FELICIDADES!!")
                break
            else:
                print("J2 ha impactado, le toca nuevamente")
                ic("Si no hemos ganado, vuelve a tocarle al turno = 2")
        else:
            turno = 1

    

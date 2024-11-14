import random
from clases.jugador import Jugador
from clases.enemigo import Enemigo


def main():
    nombreJugador = input(
        "Bienvenido a la aventura en las mazmorras, porfavor ingresa tu nombre"
    )

    jugador = Jugador(nombreJugador)

    enemigos = [
        Enemigo("alien", 50, 1),
        Enemigo("Robot", 30, 1),
        Enemigo("Mountruo", 70, 1),
    ]

    enemigosDerrotados = []

    print("¡¡Comienza la aventura!!")

    while enemigos:
        enemigosActual = random.choice(enemigos)
        if enemigosActual in enemigosDerrotados:
            continue
        print(f"Te encuentras con un {enemigosActual.nombre} en tu camino")

        while enemigosActual.salud > 0:
            accion = input("¿Que deseas hacer? (atacar/huir):").lower()

            if accion == "atacar":
                danoJugador = jugador.atacar()
                print(
                    f"Has atacado a {enemigosActual.nombre} y le has causado {danoJugador} de daño"
                )
                enemigosActual.recibirdano(danoJugador)

                if enemigosActual.salud > 0:
                    danoEnemigo = enemigosActual.atacar()
                    print(
                        f"El {enemigosActual.nombre} te ataco y causo {danoEnemigo} de daño"
                    )
                    jugador.recibirDano(danoEnemigo)

                if jugador.salud <= 0:
                 enemigosActual.salud = 0

            elif accion == "huir":
                print("¡¡Has huido del combate!!")
                break
        

        if accion == "huir":
                print("¡¡Te fuiste de la mazmorra!!")
                break

        if jugador.salud <= 0:
            print("¡¡Has perdido la partida!!")
            break
        
        if enemigosActual.salud <= 0:
            enemigosDerrotados.append(enemigosActual)
            enemigos.remove(enemigosActual)
        
        
        
       
        
        if enemigosActual.salud <= 0 :
            jugador.ganarExperiencia(25)
        
       
        
        continuar = input("Quieres seguir Explorando? (s/n):").lower()

        if continuar != "s":
            print("¡¡Gracias por haber jugado!! ")
            break
    if not enemigos:
        print("¡¡Felicidades has derrotado a todos los enemigos!!")  
        print("¡¡Gracias por haber jugado!! ")     

if __name__ == "__main__":
    main()

import random
import random
import random

# creame codigo que solicite a uruario meter un texto y lo compare con un texto que sea rock, paper o scissors
# si el texto es igual a rock, paper o scissors, imprime "you win"
# si el texto no es igual a rock, paper o scissors, imprime "you lose"
# si el texto es igual a rock, paper o scissors, imprime "it's a tie"
# el valor de rock, paper o scissors debe ser generado aleatoriamente
# mostrar en la salida el valor que a elegido el sistema aleatoriamente
# mostrar un contador con las partidas ganadas y perdidas
# para salir del juego, el usuario debe escribir "exit"
# genera todos los textos en castellano

ganadas = 0
perdidas = 0
opciones = ["piedra", "papel", "tijeras"]
while True:
    eleccion_computadora = random.choice(opciones)
    eleccion_usuario = input("Ingresa tu elección (piedra, papel, tijeras) o escribe 'salir' para salir: ")
    if eleccion_usuario == "salir":
        break
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
        ganadas += 1
    else:
        print("¡Perdiste!")
        perdidas += 1
    print("La computadora eligió:", eleccion_computadora)
    print("Partidas ganadas:", ganadas)
    print("Partidas perdidas:", perdidas)
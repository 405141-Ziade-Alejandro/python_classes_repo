import time
import sys

def typewritter_printing(text, speed=0.03) -> None:
    """
    esta funcion que permite imprimir el texto de forma mas lenta y natural
    :param text: este es el texto que se quiere imprimir
    :param speed: parametro opcional que determina la velocidad de escritura, mas chico es mas rapido
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print() # this is to jump the line, don't delete it dumbass
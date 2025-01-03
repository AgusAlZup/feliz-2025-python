from colorama import Fore, Style
import pyfiglet
import time

texto = "FELIZ 2025!!"
fuente = "rounded"
color = Fore.GREEN

def animacion(texto, fuente, color):
    for caracter in texto:
        print(Style.BRIGHT + color, pyfiglet.figlet_format(caracter, font=fuente), end="")
        time.sleep(0.2)

animacion(texto, fuente, color)
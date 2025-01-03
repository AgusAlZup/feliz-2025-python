# Importaciones 
from colorama import Fore, Style
import pyfiglet

# Convertir texto en arte ASCII con fuente personalizada y color
fuente = pyfiglet.figlet_format("FELIZ 2025!!", font="slant")

# Agregar estilo y color
print(Style.BRIGHT + Fore.GREEN, fuente)

print(Fore.RED, "éxitos y felicidad 🥳")

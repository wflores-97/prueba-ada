import platform
import os
import keyboard

rep = 0

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while rep <= 50:
    key_event = keyboard.read_event()
    key = key_event.name
    if key == 'n':
        limpiar_pantalla()
        rep += 1
        print(rep)
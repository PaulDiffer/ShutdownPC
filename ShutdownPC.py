import os

shutdown = input("¿Quieres apagar el ordenador? (si/no) ")

if shutdown.lower() == "si":
    os.system("shutdown /s /t 1") # El 1 especifica los segundo de apagado
else :
    exit()
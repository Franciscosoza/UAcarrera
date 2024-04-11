#paso 1 : incorporar las librerias necesarias
import random
import os 
os.system("cls")
#paso 2: uso de variables de mi proceso
vdado=0
#paso 3: realizar el proceso
while True:
    vdado=random.randint(1,6)
    print("el resultado del lanzamiento:",vdado)
    vletra=input("presione (L)->Volver a lanzar,ENTER->Salir")
    vletra=vletra.upper()
    if vletra!='L':
        break   
    #paso 4:mostrar el resultado esperado
 
